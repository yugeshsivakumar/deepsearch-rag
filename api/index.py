from http.server import BaseHTTPRequestHandler
import os
import json
import sys
import traceback
import requests
from bs4 import BeautifulSoup
from google import genai

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
GOOGLE_CSE_KEY = os.environ.get("GOOGLE_CSE_KEY")
GOOGLE_CSE_CX = os.environ.get("GOOGLE_CSE_CX")

def search_google_cse(query, count=3):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {"key": GOOGLE_CSE_KEY, "cx": GOOGLE_CSE_CX, "q": query, "num": count}
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    items = resp.json().get("items", [])
    return [{"title": item.get("title", ""), "snippet": item.get("snippet", ""), "link": item.get("link", "")} for item in items]

def fetch_page_text(url):
    try:
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        for tag in soup(["script", "style"]):
            tag.decompose()
        return " ".join(soup.stripped_strings)[:1000]
    except:
        return ""

def google_rag(query, top_k=3):
    results = search_google_cse(query, count=top_k)
    pages = []
    
    for r in results[:top_k]:
        pages.append({
            "title": r["title"],
            "snippet": r["snippet"],
            "link": r["link"],
            "content": fetch_page_text(r["link"])
        })
    
    context = "\n\n".join([f"[{i}] {p['title']}\n{p['snippet']}\n{p['content'][:500]}" for i, p in enumerate(pages, 1)])
    
    client = genai.Client(api_key=GEMINI_API_KEY)
    response = client.models.generate_content(
        model="gemini-2.0-flash-exp",
        contents=f'User asked: "{query}"\n\nWeb results:\n{context}\n\nAnswer in markdown, cite sources:'
    )
    
    return response.text, pages

class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def do_POST(self):
        try:
            print("=== Starting request ===", file=sys.stderr)
            
            length = int(self.headers.get('Content-Length', 0))
            body = json.loads(self.rfile.read(length).decode())
            query = body.get('query', '').strip()
            
            print(f"Query: {query}", file=sys.stderr)
            
            if not query:
                raise ValueError('No query')
            
            answer, sources = google_rag(query, 3)
            
            print(f"Got answer, {len(sources)} sources", file=sys.stderr)
            
            result = json.dumps({'answer': answer, 'sources': sources}, ensure_ascii=False)
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(result.encode('utf-8'))
            
            print("=== Success ===", file=sys.stderr)
            
        except Exception as e:
            print(f"ERROR: {str(e)}", file=sys.stderr)
            print(traceback.format_exc(), file=sys.stderr)
            
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode())