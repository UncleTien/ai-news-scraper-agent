# 🧠 AI News Scraper Agent

**AI News Scraper Agent** is an intelligent system that can **automatically collect and analyze news articles from VnExpress.net**. It allows users to:

- Input queries in **Vietnamese or English**
- **Automatically search** for relevant news articles
- **Extract and clean** article content
- **Analyze** using a Large Language Model (LLaMA3 via Ollama)
- Return results **in the same language** as the user's input

---

## 🧰 Technologies Used

- **Python 3.10+**
- [Streamlit](https://streamlit.io/) – Interactive web UI
- [Selenium](https://www.selenium.dev/) + [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) – Web scraping
- [LangChain](https://www.langchain.com/) + [Ollama](https://ollama.com/) – LLM integration and reasoning
- [webdriver-manager](https://pypi.org/project/webdriver-manager/) – ChromeDriver management

---

## 📁 Project Structure

```
.
├── main.py               # Streamlit user interface
├── scrape.py             # Web scraping utilities
├── parse.py              # LLM content analysis logic
├── vnexpress_agent.py    # Auto-agent for VnExpress
├── requirements.txt      # List of dependencies
└── README.md             # Project documentation
```

---

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/UncleTien/ai-news-scraper-agent.git
cd ai-news-scraper-agent

# 2. Create and activate a virtual environment
python -m venv ai
source ai/bin/activate        # macOS/Linux
# ai\Scripts\activate         # Windows

# 3. Install required packages
pip install -r requirements.txt

# 4. Launch the application
streamlit run main.py
```

---

## 🚀 Usage Guide

### 🔎 Manual Mode (URL Input)

1. Paste the URL of a news article from VnExpress  
2. The agent scrapes and displays the article content  
3. Enter your question to analyze the article  
4. The result will appear below, generated by the LLaMA3 model  

---

### 🤖 Auto Mode (AI-Powered Search & Analysis)

1. Type your question or topic (e.g., `"Vietnam's economy in 2025"`)  
2. The system will:
   - Visit **VnExpress.net**
   - Search for articles relevant to your query
   - Extract article content
   - Analyze it using **LLM (LLaMA3)**  
3. The result will be displayed in the same language as your input

---

## 💬 Example Queries

- **Vietnamese**:  
  `"Người trẻ ở New York đang gặp khó khăn gì?"`

- **English**:  
  `"What challenges are young people in New York facing?"`

---

## ⚠️ Notes

- Results **depend on real articles found** on VnExpress.net  
- The system **does not generate new information** — it only analyzes what is found  
- If no relevant article is found, the result will be **empty**

---

📌 **Feedback & Contributions**:  
Feel free to open a pull request or issue on GitHub to improve this project!
