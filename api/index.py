from http.server import BaseHTTPRequestHandler
import os
import json
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

def fetch_page_text(url, max_chars=1500):
    try:
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=5)
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
    return response.text if hasattr(response, 'text') else str(response)

def google_rag(query, top_k=3):
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
    
    context_parts = []
    for i, p in enumerate(pages, 1):
        context_parts.append(f"[Source {i}] {p['title']}\nURL: {p['link']}\nSnippet: {p['snippet']}\nExtract: {p['content'][:800]}")
    
    prompt = f"""The user asked: "{query}"

Here are web results:

{chr(10).join(context_parts)}

Give a clear answer in markdown. Cite sources by number."""
    
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
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')
            data = json.loads(body)
            
            query = data.get('query', '').strip()
            top_k = min(int(data.get('top_k', 3)), 3)
            
            if not query:
                raise ValueError('Query is required')
            
            answer, sources = google_rag(query, top_k)
            
            response_data = {
                'answer': answer,
                'sources': sources
            }
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response_json = json.dumps(response_data, ensure_ascii=False)
            self.wfile.write(response_json.encode('utf-8'))
            
        except Exception as e:
            error_response = {'error': str(e)}
            
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            self.wfile.write(json.dumps(error_response).encode('utf-8'))