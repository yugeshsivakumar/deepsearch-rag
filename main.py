#!/usr/bin/env python3
"""
Flask server for Google RAG with web interface
"""
import os, json, time, requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

try:
    from google import genai
except ImportError:
    raise SystemExit("Install with: pip install google-genai")

# Load API keys
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GOOGLE_CSE_KEY = os.getenv("GOOGLE_CSE_KEY")
GOOGLE_CSE_CX = os.getenv("GOOGLE_CSE_CX")

if not all([GEMINI_API_KEY, GOOGLE_CSE_KEY, GOOGLE_CSE_CX]):
    raise SystemExit("❌ Missing keys. Fill GEMINI_API_KEY, GOOGLE_CSE_KEY, GOOGLE_CSE_CX in .env")

app = Flask(__name__, static_folder='.')
CORS(app)

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

# --- Fetch web page text (simple) ---
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
    print(f"\n🔍 Searching Google for: {query}\n")
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
        time.sleep(0.3)  # be polite

    # Prepare context
    context_parts = []
    for i, p in enumerate(pages, start=1):
        context_parts.append(f"[Source {i}] {p['title']}\nURL: {p['link']}\nSnippet: {p['snippet']}\n\nExtract:\n{p['content'][:1500]}")

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

# --- API Routes ---
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/search', methods=['POST'])
def search():
    try:
        data = request.json
        query = data.get('query')
        top_k = data.get('top_k', 5)
        
        if not query:
            return jsonify({'error': 'Query is required'}), 400
        
        answer, sources = google_rag(query, top_k)
        
        return jsonify({
            'answer': answer,
            'sources': sources
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 Google RAG Server Starting...")
    print("="*60)
    print("\n📱 Open your browser and go to: http://localhost:5000")
    print("\n⏹️  Press CTRL+C to stop the server\n")
    app.run(host='0.0.0.0', port=5000, debug=True)