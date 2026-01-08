#!/usr/bin/env python3
"""
Vercel serverless function for Google RAG Search
"""
import os
import json
import time
import requests
from bs4 import BeautifulSoup

try:
    from google import genai
except ImportError:
    raise SystemExit("Install with: pip install google-genai")

# Load API keys from environment
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
GOOGLE_CSE_KEY = os.environ.get("GOOGLE_CSE_KEY")
GOOGLE_CSE_CX = os.environ.get("GOOGLE_CSE_CX")

if not all([GEMINI_API_KEY, GOOGLE_CSE_KEY, GOOGLE_CSE_CX]):
    raise SystemExit("❌ Missing API keys in environment variables")

# --- Google Search ---
def search_google_cse(query, count=5):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_CSE_KEY,
        "cx": GOOGLE_CSE_CX,
        "q": query,
        "num": count
    }
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    results = []
    for item in data.get("items", []):
        results.append({
            "title": item.get("title"),
            "snippet": item.get("snippet"),
            "link": item.get("link")
        })
    return results

# --- Fetch web page text ---
def fetch_page_text(url, max_chars=4000):
    try:
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        for tag in soup(["script", "style", "noscript", "svg"]):
            tag.decompose()
        text = " ".join([t.strip() for t in soup.get_text().splitlines() if t.strip()])
        return text[:max_chars]
    except Exception as e:
        return f"(error fetching page: {e})"

# --- Gemini call ---
def call_gemini(prompt, model="gemini-2.0-flash"):
    client = genai.Client(api_key=GEMINI_API_KEY)
    response = client.models.generate_content(model=model, contents=prompt)
    return getattr(response, "text", str(response))

# --- Combine search + Gemini ---
def google_rag(query, top_k=4):
    results = search_google_cse(query, count=top_k)
    pages = []

    for r in results:
        text = fetch_page_text(r["link"])
        pages.append({
            "title": r["title"],
            "snippet": r["snippet"],
            "link": r["link"],
            "content": text
        })
        time.sleep(0.3)

    # Prepare context
    context_parts = []
    for i, p in enumerate(pages, start=1):
        context_parts.append(
            f"[Source {i}] {p['title']}\n"
            f"URL: {p['link']}\n"
            f"Snippet: {p['snippet']}\n\n"
            f"Extract:\n{p['content'][:1500]}"
        )

    context_blob = "\n\n---\n\n".join(context_parts)
    prompt = f"""
The user asked: "{query}"

Here are some current web results from Google:

{context_blob}

Use this information to give a clear, concise answer in markdown. Include the most relevant items and mention the sources (by number) next to your points.
If the question asks for products or prices, list a few examples with brief notes.
"""

    answer = call_gemini(prompt)
    return answer, pages

# --- Vercel Serverless Handler ---
def handler(request):
    """
    Main handler for Vercel serverless function
    """
    # Set CORS headers
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
    }
    
    # Handle OPTIONS request (CORS preflight)
    if request.method == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': headers,
            'body': ''
        }
    
    # Handle POST request
    if request.method == 'POST':
        try:
            # Parse request body
            body = json.loads(request.body) if isinstance(request.body, str) else request.body
            query = body.get('query')
            top_k = body.get('top_k', 5)
            
            if not query:
                return {
                    'statusCode': 400,
                    'headers': headers,
                    'body': json.dumps({'error': 'Query is required'})
                }
            
            # Perform RAG search
            answer, sources = google_rag(query, top_k)
            
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps({
                    'answer': answer,
                    'sources': sources
                })
            }
            
        except Exception as e:
            return {
                'statusCode': 500,
                'headers': headers,
                'body': json.dumps({'error': str(e)})
            }
    
    # Method not allowed
    return {
        'statusCode': 405,
        'headers': headers,
        'body': json.dumps({'error': 'Method not allowed'})
    }

# Export for Vercel
def lambda_handler(event, context):
    """AWS Lambda compatible handler"""
    class Request:
        def __init__(self, event):
            self.method = event.get('httpMethod', 'GET')
            self.body = event.get('body', '{}')
    
    return handler(Request(event))
