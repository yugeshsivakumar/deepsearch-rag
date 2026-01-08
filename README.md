<div align="center">

# 🔍 DeepSearch RAG

![Typing SVG](https://readme-typing-svg.demolab.com/?font=Fira+Code&weight=600&size=32&duration=3000&pause=1000&color=3B82F6&center=true&vCenter=true&multiline=true&repeat=true&width=800&height=120&lines=AI-Powered+Search+Engine+🤖;Google+Custom+Search+%2B+Gemini+AI+💡;Real-time+RAG+Implementation+⚡;Beautiful+Web+Interface+🎨)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web_Server-000000?style=for-the-badge&logo=flask&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-2.0_Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Google](https://img.shields.io/badge/Google-Custom_Search-4285F4?style=for-the-badge&logo=google&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<p align="center">
  <strong>🚀 Advanced search engine combining Google Custom Search with Gemini AI for intelligent, context-aware answers with verified sources</strong>
</p>

<p align="center">
  <a href="#-features"><strong>Features</strong></a> ·
  <a href="#-installation"><strong>Installation</strong></a> ·
  <a href="#-setup-guide"><strong>Setup</strong></a> ·
  <a href="#-usage"><strong>Usage</strong></a> ·
  <a href="#-how-it-works"><strong>How It Works</strong></a> ·
  <a href="#-api-documentation"><strong>API</strong></a>
</p>

<br/>

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" alt="line" width="100%">

</div>

---

## 🎯 Features

<div align="center">

|            Feature            | Description                                                      | Status |
| :----------------------------: | :--------------------------------------------------------------- | :----: |
|    🔍**Smart Search**    | Google Custom Search API integration with real-time results      |   ✅   |
| 🤖**AI-Powered Answers** | Gemini 2.0 Flash generates comprehensive, sourced responses      |   ✅   |
| 📚**RAG Implementation** | Retrieval-Augmented Generation for accurate, current information |   ✅   |
|    🌐**Web Scraping**    | Automatic content extraction from search result pages            |   ✅   |
|    🎨**Beautiful UI**    | Modern, responsive web interface with Tailwind CSS               |   ✅   |
| 📱**Mobile Responsive** | Works seamlessly on desktop, tablet, and mobile devices          |   ✅   |
| 🔗**Source Attribution** | All answers include numbered source references                   |   ✅   |
|  📖**Markdown Support**  | Rich text formatting in AI responses                             |   ✅   |
|   🔄**Search History**   | Recent searches saved for quick access                           |   ✅   |
|  ⚡**Fast Performance**  | Optimized API calls and caching mechanisms                       |   ✅   |

</div>

<br/>

## 🎬 Demo

### Search Interface

The clean, modern interface makes it easy to ask any question and get AI-powered answers with sources.

### Example Query

**Query:** "What are the best laptops in 2024?"

**Result:**

- AI-generated comprehensive answer with specific recommendations
- Numbered sources from reputable tech websites
- Links to full articles for deeper reading
- Markdown-formatted response with proper structure

<br/>

## 📦 Installation

### Prerequisites

Before you begin, ensure you have:

* **Python 3.8+** installed
* **pip** package manager
* **Stable internet connection**
* **Modern web browser** (Chrome, Firefox, Safari, Edge)
* **Google Cloud Account** (for API keys)
* **Google AI Studio Account** (for Gemini API)

### Step 1: Install Python

1. Download Python from [python.org](https://www.python.org/downloads/)
2. **✅ CHECK "Add Python to PATH"** during installation
3. Verify installation:
   ```bash
   python --version
   # Should output: Python 3.x.x
   ```

### Step 2: Install pip (if not already installed)

```bash
# Check if pip is installed
pip --version

# If not installed, download get-pip.py
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

<br/>

## 🚀 Setup Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yugeshsivakumar/deepsearch-rag.git
cd deepsearch-rag
```

### 2️⃣ Install Python Dependencies

```bash
pip install -r requirements.txt
```

**Required packages:**

```
flask==3.0.0              # Web framework
flask-cors==4.0.0         # Cross-Origin Resource Sharing
google-genai==1.0.0       # Google Gemini AI SDK
requests==2.31.0          # HTTP library
beautifulsoup4==4.12.0    # Web scraping
python-dotenv==1.0.0      # Environment variable management
```

If you don't have a `requirements.txt`, create one with:

```bash
echo "flask==3.0.0
flask-cors==4.0.0
google-genai
requests==2.31.0
beautifulsoup4==4.12.0
python-dotenv==1.0.0" > requirements.txt

pip install -r requirements.txt
```

### 3️⃣ Get Google Gemini API Key

#### Step-by-Step Guide:

1. **Visit Google AI Studio**

   - Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Sign in with your Google account
2. **Create API Key**

   - Click **"Get API Key"** button
   - Click **"Create API Key"**
   - Choose **"Create API key in new project"** (or select existing project)
3. **Copy Your API Key**

   - Copy the generated API key (format: `AIzaSy...`)
   - ⚠️ **Keep this key secret!** Never commit it to GitHub
4. **Free Tier Limits:**

   - 60 requests per minute
   - 1,500 requests per day
   - Perfect for personal use and testing

### 4️⃣ Get Google Custom Search API Credentials

You need **TWO** things: API Key and Search Engine ID (CX)

#### A. Create Google Custom Search API Key

1. **Go to Google Cloud Console**

   - Visit [Google Cloud Console](https://console.cloud.google.com/)
   - Sign in with your Google account
2. **Create New Project** (if you don't have one)

   - Click project dropdown at the top
   - Click **"NEW PROJECT"**
   - Enter project name: `DeepSearch-RAG`
   - Click **"CREATE"**
3. **Enable Custom Search API**

   - Go to [API Library](https://console.cloud.google.com/apis/library)
   - Search for **"Custom Search API"**
   - Click on it and press **"ENABLE"**
4. **Create API Credentials**

   - Go to [Credentials](https://console.cloud.google.com/apis/credentials)
   - Click **"+ CREATE CREDENTIALS"**
   - Select **"API Key"**
   - Copy the API key (format: `AIzaSy...`)
   - Click **"RESTRICT KEY"** (optional but recommended)
     - Under **"API restrictions"**, select **"Custom Search API"**
     - Click **"SAVE"**

#### B. Create Custom Search Engine (Get CX ID)

1. **Visit Programmable Search Engine**

   - Go to [Google Programmable Search Engine](https://programmablesearchengine.google.com/controlpanel/all)
   - Sign in with your Google account
2. **Create New Search Engine**

   - Click **"Add"** or **"Create"**
   - **Search engine name:** `DeepSearch`
   - **What to search:** Select **"Search the entire web"**
   - Click **"CREATE"**
3. **Get Search Engine ID (CX)**

   - Click on your newly created search engine
   - Go to **"Setup"** or **"Basic"** section
   - Find **"Search engine ID"** (format: `a1b2c3d4e5...`)
   - Copy this ID
4. **Enable Image Search (Optional)**

   - In **"Setup"** → **"Basic"**
   - Turn on **"Image search"**
   - Turn on **"Search the entire web"**
   - Click **"UPDATE"**

#### Free Tier Limits for Custom Search:

- **100 queries per day** (free)
- For more queries: $5 per 1000 queries up to 10k queries/day

### 5️⃣ Configure Environment Variables

Create a `.env` file in the project root directory:

```bash
# Windows
copy _env .env

# macOS/Linux
cp _env .env
```

Edit `.env` file with your credentials:

```env
# Gemini AI API Key (from Google AI Studio)
GEMINI_API_KEY=your_gemini_api_key_here

# Google Custom Search API Key (from Google Cloud Console)
GOOGLE_CSE_KEY=your_google_cse_api_key_here

# Google Custom Search Engine ID (from Programmable Search Engine)
GOOGLE_CSE_CX=your_search_engine_id_here
```

**Example `.env` file:**

```env
GEMINI_API_KEY=AIzaSyA1B2C3D4E5F6G7H8I9J0K1L2M3N4O5P6Q
GOOGLE_CSE_KEY=AIzaSyX9Y8Z7W6V5U4T3S2R1Q0P9O8N7M6L5K4J
GOOGLE_CSE_CX=a1b2c3d4e5f6g7h8i
```

⚠️ **IMPORTANT:**

- Never share your API keys publicly
- Add `.env` to `.gitignore` (already included)
- Use different keys for development and production

<br/>

## 🎮 Usage

### Starting the Server

#### Option 1: Direct Python Execution

```bash
python main.py
```

#### Option 2: Using Flask Command

```bash
# Set Flask app
export FLASK_APP=main.py  # macOS/Linux
set FLASK_APP=main.py     # Windows

# Run in development mode
flask run
```

#### Option 3: Production Server with Gunicorn (Linux/macOS)

```bash
# Install gunicorn
pip install gunicorn

# Run with gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 main:app
```

### Accessing the Application

Once the server starts, you'll see:

```
============================================================
🚀 Google RAG Server Starting...
============================================================

📱 Open your browser and go to: http://localhost:5000

ℹ️  Press CTRL+C to stop the server
```

**Access URLs:**

- **Local:** `http://localhost:5000`
- **Local Network:** `http://YOUR_IP:5000` (replace YOUR_IP with your machine's IP)
- **Example:** `http://192.168.1.100:5000`

### Using the Search Interface

1. **Open your browser** and navigate to `http://localhost:5000`
2. **Enter your question** in the search box:

   - "What are the best laptops in 2024?"
   - "How does photosynthesis work?"
   - "Latest news about SpaceX"
   - "Compare Python vs JavaScript for web development"
3. **Click Search** or press **Enter**
4. **View Results:**

   - AI-generated answer on the left
   - Numbered sources on the right
   - Click sources to visit original websites
5. **Search History:**

   - Recent searches appear below the search box
   - Click any previous search to repeat it

### Example Queries to Try

```
✅ General Knowledge:
   - "What is quantum computing?"
   - "History of the Roman Empire"

✅ Current Events:
   - "Latest developments in AI technology"
   - "Current weather in New York"

✅ Product Research:
   - "Best smartphones under $500"
   - "Gaming laptop recommendations 2024"

✅ How-To Guides:
   - "How to learn Python programming"
   - "Steps to start a business"

✅ Comparisons:
   - "React vs Vue.js comparison"
   - "Electric cars vs hybrid cars"
```

<br/>

## 🔧 How It Works

### System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         User Interface                       │
│              (HTML + Tailwind CSS + JavaScript)              │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                      Flask Web Server                        │
│                     (main.py - API Layer)                    │
└──────────────────┬──────────────────────┬───────────────────┘
                   │                      │
                   ▼                      ▼
    ┌──────────────────────┐  ┌──────────────────────┐
    │  Google Custom       │  │   Gemini 2.0 Flash   │
    │  Search API          │  │   AI Model           │
    │  (Search Results)    │  │   (Answer Gen)       │
    └──────┬───────────────┘  └──────────────────────┘
           │
           ▼
    ┌──────────────────────┐
    │  Web Scraping        │
    │  (BeautifulSoup)     │
    │  (Extract Content)   │
    └──────────────────────┘
```

### RAG Pipeline

1. **User Query** → User enters question in search box
2. **Google Search** → Query sent to Google Custom Search API

   - Returns top 5 relevant URLs
   - Includes title, snippet, and link for each result
3. **Content Extraction** → Web scraping for each result

   - Fetch webpage HTML
   - Parse with BeautifulSoup
   - Extract clean text (remove scripts, styles)
   - Limit to 4000 characters per page
4. **Context Building** → Combine all sources

   - Format as numbered sources [Source 1], [Source 2], etc.
   - Include title, URL, snippet, and extracted content
   - Create structured context for AI
5. **AI Generation** → Gemini AI processes context

   - Analyzes all source materials
   - Generates comprehensive answer
   - Cites sources by number
   - Formats response in markdown
6. **Response Display** → Return to user

   - AI answer with markdown formatting
   - Clickable source cards
   - Interactive, responsive UI

### Key Technologies

**Backend:**

- **Flask:** Lightweight Python web framework
- **google-genai:** Official Google Gemini AI SDK
- **BeautifulSoup4:** HTML parsing and web scraping
- **Requests:** HTTP library for API calls
- **python-dotenv:** Environment variable management

**Frontend:**

- **HTML5:** Semantic markup
- **Tailwind CSS:** Utility-first CSS framework
- **Vanilla JavaScript:** No frameworks for better performance
- **Responsive Design:** Mobile-first approach

**APIs:**

- **Google Custom Search API:** Web search functionality
- **Gemini 2.0 Flash:** Advanced AI language model

<br/>

## 📡 API Documentation

### Endpoints

#### `GET /`

Returns the main HTML interface.

**Response:** HTML page

---

#### `POST /api/search`

Performs RAG search and returns AI-generated answer with sources.

**Request Body:**

```json
{
  "query": "What are the best laptops in 2024?",
  "top_k": 5
}
```

**Parameters:**

- `query` (string, required): The search query
- `top_k` (integer, optional): Number of search results to fetch (default: 5, max: 10)

**Response:**

```json
{
  "answer": "# Best Laptops in 2024\n\nBased on current reviews...",
  "sources": [
    {
      "title": "Top 10 Laptops of 2024 - TechRadar",
      "snippet": "Comprehensive review of the year's best laptops...",
      "link": "https://www.techradar.com/best-laptops-2024",
      "content": "Full extracted text from the page..."
    }
  ]
}
```

**Response Codes:**

- `200 OK`: Successful search
- `400 Bad Request`: Missing or invalid query
- `500 Internal Server Error`: Server error (API issues, network problems)

### Example API Usage

#### Using cURL:

```bash
curl -X POST http://localhost:5000/api/search \
  -H "Content-Type: application/json" \
  -d '{"query": "Best programming languages 2024", "top_k": 5}'
```

#### Using Python Requests:

```python
import requests

url = "http://localhost:5000/api/search"
data = {
    "query": "What is machine learning?",
    "top_k": 5
}

response = requests.post(url, json=data)
result = response.json()

print("Answer:", result["answer"])
print("Sources:", len(result["sources"]))
```

#### Using JavaScript Fetch:

```javascript
fetch('http://localhost:5000/api/search', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    query: 'Best practices for REST APIs',
    top_k: 5
  })
})
.then(res => res.json())
.then(data => {
  console.log('Answer:', data.answer);
  console.log('Sources:', data.sources);
});
```

<br/>

## ⚙️ Configuration

### Customizing Search Parameters

Edit `main.py` to modify search behavior:

```python
# Line ~70-80: Adjust search count
def search_google_cse(query, count=5):  # Change default count
    # Increase for more comprehensive results
    # Decrease for faster responses
```

### Adjusting Content Extraction

```python
# Line ~95-105: Modify text extraction length
def fetch_page_text(url, max_chars=4000):  # Adjust max_chars
    # Increase: More context, slower processing
    # Decrease: Less context, faster processing
```

### Changing AI Model

```python
# Line ~115: Switch Gemini model
def call_gemini(prompt, model="gemini-2.0-flash"):
    # Options:
    # - "gemini-2.0-flash" (fast, efficient)
    # - "gemini-1.5-pro" (more capable, slower)
    # - "gemini-1.5-flash" (older, still good)
```

### Customizing AI Prompt

Edit the prompt template in `main.py` (line ~145):

```python
prompt = f"""
The user asked: "{query}"

Here are some current web results from Google:

{context_blob}

[Modify instructions here]
- Change tone (formal/casual)
- Adjust detail level
- Add specific formatting requirements
- Request different citation styles
"""
```

### Server Configuration

```python
# Line ~180: Change host and port
app.run(host='0.0.0.0', port=5000, debug=True)
#            ^^^^^^^^      ^^^^   ^^^^^^^^^^
#            Any IP        Port   Debug mode
```

**Options:**

- `host='127.0.0.1'`: Local only
- `host='0.0.0.0'`: Accessible on network
- `port=5000`: Default port (change if occupied)
- `debug=True`: Development mode (disable in production)

<br/>

## 🐛 Troubleshooting

<details>
<summary><strong>❌ "Missing keys" error on startup</strong></summary>

**Error:**

```
❌ Missing keys. Fill GEMINI_API_KEY, GOOGLE_CSE_KEY, GOOGLE_CSE_CX in .env
```

**Solutions:**

1. Verify `.env` file exists in project root
2. Check all three API keys are filled in
3. Remove any quotes around API keys
4. Ensure no spaces before/after the `=` sign
5. Restart the server after editing `.env`

**Correct `.env` format:**

```env
GEMINI_API_KEY=AIzaSyA1B2C3D4E5F6G7H8I9J0
GOOGLE_CSE_KEY=AIzaSyX9Y8Z7W6V5U4T3S2R1Q0
GOOGLE_CSE_CX=a1b2c3d4e5f6g7h8i
```

</details>

<details>
<summary><strong>❌ "Failed to perform search" error</strong></summary>

**Possible causes:**

1. **API Key Issues:**

   - Invalid or expired API keys
   - API not enabled in Google Cloud Console
   - Daily quota exceeded
2. **Network Issues:**

   - No internet connection
   - Firewall blocking API requests
   - VPN/proxy interference
3. **Search Engine Issues:**

   - Invalid Search Engine ID (CX)
   - Search engine not configured properly

**Solutions:**

1. Test API keys independently:

   ```bash
   # Test Gemini API
   curl "https://generativelanguage.googleapis.com/v1/models?key=YOUR_GEMINI_KEY"

   # Test Custom Search API
   curl "https://www.googleapis.com/customsearch/v1?key=YOUR_CSE_KEY&cx=YOUR_CX&q=test"
   ```
2. Check Google Cloud Console:

   - Verify Custom Search API is enabled
   - Check quota usage
   - Review API restrictions
3. Verify Search Engine configuration:

   - Go to [Programmable Search Engine](https://programmablesearchengine.google.com/)
   - Confirm "Search the entire web" is enabled
   - Check Search Engine ID matches `.env`

</details>

<details>
<summary><strong>❌ "Install with: pip install google-genai" error</strong></summary>

**Error:**

```python
ImportError: No module named 'google.genai'
```

**Solutions:**

1. Install the package:

   ```bash
   pip install google-genai
   ```
2. If using virtual environment:

   ```bash
   # Create venv
   python -m venv venv

   # Activate
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows

   # Install packages
   pip install -r requirements.txt
   ```
3. Verify installation:

   ```bash
   pip list | grep google-genai
   ```

</details>

<details>
<summary><strong>❌ Port 5000 already in use</strong></summary>

**Error:**

```
OSError: [Errno 48] Address already in use
```

**Solutions:**

1. **Use different port:**
   Edit `main.py` line 180:

   ```python
   app.run(host='0.0.0.0', port=5001, debug=True)  # Changed to 5001
   ```
2. **Kill existing process:**

   ```bash
   # Find process using port 5000
   # macOS/Linux:
   lsof -ti:5000 | xargs kill -9

   # Windows:
   netstat -ano | findstr :5000
   taskkill /PID <PID_NUMBER> /F
   ```
3. **Common port conflicts:**

   - Port 5000: AirPlay Receiver (macOS), Flask default
   - Solution: Disable AirPlay in System Preferences or use different port

</details>

<details>
<summary><strong>❌ Quota exceeded errors</strong></summary>

**Error messages:**

- "Quota exceeded for quota metric 'Queries' and limit 'Queries per day'"
- "Resource exhausted"

**Solutions:**

1. **Check quota usage:**

   - [Google Cloud Console - APIs &amp; Services](https://console.cloud.google.com/apis/dashboard)
   - View quota limits and current usage
2. **Free tier limits:**

   - **Gemini AI:** 60 requests/minute, 1,500 requests/day
   - **Custom Search:** 100 queries/day (free)
3. **Upgrade options:**

   - Custom Search: $5 per 1000 queries (up to 10k/day)
   - Gemini: Paid tier for higher limits
4. **Reduce usage:**

   - Cache results locally
   - Reduce `top_k` parameter
   - Implement rate limiting

</details>

<details>
<summary><strong>❌ Web scraping fails for certain sites</strong></summary>

**Issue:**
Some websites block scraping or require authentication.

**Error in logs:**

```
(error fetching page: 403 Forbidden)
```

**Solutions:**

1. **Expected behavior:**

   - Some sites block automated access
   - AI will still use snippet from search results
   - Not all sources need full content
2. **Improve success rate:**
   Edit `main.py` around line 95:

   ```python
   def fetch_page_text(url, max_chars=4000):
       try:
           headers = {
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
               "Accept": "text/html,application/xhtml+xml",
               "Accept-Language": "en-US,en;q=0.9"
           }
           r = requests.get(url, headers=headers, timeout=10)
   ```
3. **Alternative:**

   - Increase timeout value
   - Add retry logic
   - Skip problematic sources

</details>

<details>
<summary><strong>❌ Markdown not rendering properly</strong></summary>

**Issue:**
AI response shows markdown syntax instead of formatted text.

**Solutions:**

1. **Check browser console:**

   - Press F12 → Console tab
   - Look for JavaScript errors
2. **Clear browser cache:**

   - Hard refresh: Ctrl+Shift+R (Windows/Linux) or Cmd+Shift+R (macOS)
3. **Verify JavaScript is enabled:**

   - Should see formatted text with headers, bold, lists
   - If still seeing raw markdown, check browser settings
4. **Test with different browser:**

   - Try Chrome, Firefox, or Edge
   - Mobile browsers should also work

</details>

<br/>

## 🚀 Deployment

### Deploy to Production

#### Option 1: Deploy with Gunicorn (Linux)

```bash
# Install gunicorn
pip install gunicorn

# Run with multiple workers
gunicorn -w 4 -b 0.0.0.0:5000 main:app

# Run as background service
gunicorn -w 4 -b 0.0.0.0:5000 main:app --daemon
```

#### Option 2: Deploy with Docker

Create `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "main:app"]
```

Build and run:

```bash
# Build image
docker build -t deepsearch-rag .

# Run container
docker run -d -p 5000:5000 --env-file .env deepsearch-rag
```

#### Option 3: Deploy to Heroku

```bash
# Install Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# Login
heroku login

# Create app
heroku create deepsearch-rag

# Set environment variables
heroku config:set GEMINI_API_KEY=your_key_here
heroku config:set GOOGLE_CSE_KEY=your_key_here
heroku config:set GOOGLE_CSE_CX=your_cx_here

# Deploy
git push heroku main
```

Create `Procfile`:

```
web: gunicorn main:app
```

#### Option 4: Deploy to Railway/Render

1. Connect GitHub repository
2. Add environment variables in dashboard
3. Deploy automatically on push

### Security Considerations

**Production checklist:**

- [ ] Set `debug=False` in `main.py`
- [ ] Use HTTPS (SSL certificate)
- [ ] Implement rate limiting
- [ ] Add authentication if needed
- [ ] Use environment variables for secrets
- [ ] Enable CORS only for trusted domains
- [ ] Monitor API usage and costs
- [ ] Set up error logging
- [ ] Implement caching
- [ ] Use CDN for static files

<br/>

## 📊 Performance Tips

### Optimize for Speed

1. **Reduce `top_k` parameter:**

   ```python
   # Faster: top_k=3 (3 sources)
   # Balanced: top_k=5 (default)
   # Comprehensive: top_k=10 (slower)
   ```
2. **Implement caching:**

   ```python
   from functools import lru_cache

   @lru_cache(maxsize=100)
   def search_google_cse(query, count=5):
       # Cache recent searches
   ```
3. **Parallel processing:**

   ```python
   from concurrent.futures import ThreadPoolExecutor

   with ThreadPoolExecutor(max_workers=5) as executor:
       futures = [executor.submit(fetch_page_text, r['link']) for r in results]
   ```

### Monitor Usage

Track API calls to stay within free tier:

```python
import time

call_count = 0
last_reset = time.time()

def rate_limit_check():
    global call_count, last_reset
  
    # Reset counter every hour
    if time.time() - last_reset > 3600:
        call_count = 0
        last_reset = time.time()
  
    if call_count >= 60:  # Gemini limit: 60/minute
        time.sleep(60)
        call_count = 0
  
    call_count += 1
```

<br/>

## 🤝 Contributing

Contributions are welcome! Here's how:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Make your changes**
   - Add new features
   - Fix bugs
   - Improve documentation
   - Enhance UI/UX
   - Optimize performance
4. **Commit your changes**
   ```bash
   git commit -m '✨ Add AmazingFeature'
   ```
5. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
6. **Open a Pull Request**

### Contribution Ideas

- 🎨 UI improvements and themes
- 🔍 Advanced search filters
- 📊 Analytics dashboard
- 🌍 Multi-language support
- 💾 Search history database
- 🔐 User authentication
- 📱 Mobile app version
- 🤖 Additional AI models
- 📈 Performance optimizations
- 🧪 Unit tests and CI/CD

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable names
- Add comments for complex logic
- Write docstrings for functions
- Keep functions small and focused
- Test thoroughly before submitting

<br/>

## 📝 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

<br/>

## 🙏 Acknowledgments

* **Google AI** - [Gemini AI](https://ai.google.dev/) - Advanced language model
* **Google Cloud** - [Custom Search API](https://developers.google.com/custom-search) - Web search functionality
* **Flask** - [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/) - Web framework
* **BeautifulSoup** - [https://www.crummy.com/software/BeautifulSoup/](https://www.crummy.com/software/BeautifulSoup/) - Web scraping
* **Tailwind CSS** - [https://tailwindcss.com/](https://tailwindcss.com/) - Styling framework
* **Python Community** - For amazing libraries and support

<br/>

## 📧 Contact & Support

<div align="center">

**Yugesh S** - Developer & Creator

[![Website](https://img.shields.io/badge/Website-yugesh.me-blue?style=for-the-badge)](https://yugesh.me)
[![GitHub](https://img.shields.io/badge/GitHub-yugeshsivakumar-181717?style=for-the-badge&logo=github)](https://github.com/yugeshsivakumar)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-yugeshsivakumar-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/yugeshsivakumar)
[![Email](https://img.shields.io/badge/Email-contact@yugesh.me-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:contact@yugesh.me)

**Project Link:** [https://github.com/yugeshsivakumar/deepsearch-rag](https://github.com/yugeshsivakumar/deepsearch-rag)

</div>

### Get Help

* 🐛 **Bug Reports:** [Open an Issue](https://github.com/yugeshsivakumar/deepsearch-rag/issues/new)
* 💡 **Feature Requests:** [Start a Discussion](https://github.com/yugeshsivakumar/deepsearch-rag/discussions)
* 📧 **Email Support:** [contact@yugesh.me](mailto:contact@yugesh.me)
* 💬 **Questions:** Open an issue with the "question" label

<br/>

## ⭐ Show Your Support

If this project helped you, please consider:

* ⭐ **Starring the repository**
* 🍴 **Forking for your own projects**
* 📢 **Sharing with friends and colleagues**
* 💬 **Providing feedback and suggestions**
* 🐛 **Reporting bugs and issues**
* 🤝 **Contributing code improvements**

<div align="center">

### ⭐ Star this repository if you found it helpful!

<br/>

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" alt="line" width="100%">

<br/>

![GitHub stars](https://img.shields.io/github/stars/yugeshsivakumar/deepsearch-rag?style=social)
![GitHub forks](https://img.shields.io/github/forks/yugeshsivakumar/deepsearch-rag?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/yugeshsivakumar/deepsearch-rag?style=social)
![GitHub issues](https://img.shields.io/github/issues/yugeshsivakumar/deepsearch-rag?style=social)

<br/>

**Made with ❤️ and ☕ by [Yugesh S](https://yugesh.me)**

*Powered by Google Custom Search API & Gemini AI*

</div>

---

<div align="center">

### 🚀 Ready to get started?

[⬆️ Back to Top](#-deepsearch-rag)

</div>
