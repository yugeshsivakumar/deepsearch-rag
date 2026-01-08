from http.server import BaseHTTPRequestHandler
import os
import json
import time
import requests
from bs4 import BeautifulSoup
from google import genai

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
GOOGLE_CSE_KEY = os.environ.get("GOOGLE_CSE_KEY")
GOOGLE_CSE_CX = os.environ.get("GOOGLE_CSE_CX")

def search_google_cse(query, count=5):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {"key": GOOGLE_CSE_KEY, "cx": GOOGLE_CSE_CX, "q": query, "num": count}
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    return [{"title": i.get("title"), "snippet": i.get("snippet"), "link": i.get("link")} 
            for i in resp.json().get("items", [])]

def fetch_page_text(url, max_chars=2000):
    try:
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=8)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        for tag in soup(["script", "style", "noscript", "svg"]):
            tag.decompose()
        text = " ".join([t.strip() for t in soup.get_text().splitlines() if t.strip()])
        return text[:max_chars]
    except:
        return ""

def call_gemini(prompt):
    client = genai.Client(api_key=GEMINI_API_KEY)
    response = client.models.generate_content(model="gemini-2.0-flash-exp", contents=prompt)
    return getattr(response, "text", str(response))

def google_rag(query, top_k=3):
    results = search_google_cse(query, count=top_k)
    pages = []
    for r in results:
        text = fetch_page_text(r["link"])
        pages.append({"title": r["title"], "snippet": r["snippet"], "link": r["link"], "content": text})
    
    context_parts = [f"[Source {i}] {p['title']}\nURL: {p['link']}\nSnippet: {p['snippet']}\n\nExtract:\n{p['content'][:1000]}" 
                     for i, p in enumerate(pages, 1)]
    
    prompt = f"""The user asked: "{query}"

Here are web results from Google:

{chr(10).join(context_parts)}

Give a clear, concise answer in markdown. Mention sources by number."""
    
    answer = call_gemini(prompt)
    return answer, pages

class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            body = json.loads(self.rfile.read(content_length))
            query = body.get('query')
            top_k = body.get('top_k', 3)
            
            if not query:
                raise ValueError('Query required')
            
            answer, sources = google_rag(query, top_k)
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'answer': answer, 'sources': sources}).encode())
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode())