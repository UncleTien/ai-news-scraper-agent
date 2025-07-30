# 🧠 AI News Scraper Agent

## 📌 Introduction

The **AI News Scraper Agent** is an AI-powered system that can **automatically collect and analyze news articles from VnExpress.net**. The system allows users to:

- Enter queries in either Vietnamese or English
- Automatically search for related articles
- Extract and clean content
- Analyze using LLM (LLaMA3 via Ollama)
- Return answers in the same language as the user’s query

---

## 🧰 Technologies Used

- Python 3.10+
- [Streamlit](https://streamlit.io/)
- [Selenium](https://www.selenium.dev/) + [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [LangChain](https://www.langchain.com/) + [Ollama](https://ollama.com/)
- [ChromeDriverManager](https://pypi.org/project/webdriver-manager/)

---

## 📁 Project Structure

.
├── main.py # Streamlit interface
├── scrape.py # Web scraping utilities
├── parse.py # LLM parsing logic
├── vnexpress_agent.py # Auto-agent for VnExpress
├── requirements.txt # Required packages
└── README.md # Project documentation


---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/UncleTien/ai-news-scraper-agent.git
cd ai-news-scraper-agent

# Create and activate a virtual environment
python -m venv ai
source ai/bin/activate        # For macOS/Linux
# ai\Scripts\activate         # For Windows

# Install dependencies
pip install -r requirements.txt

# Launch the app
streamlit run main.py

🚀 Usage Guide
🔎 Manual Mode (URL Input)
1. Copy and paste the URL of a news article

2. The agent scrapes and displays the article's content

3. Enter a query to analyze the content

4. Result is shown below using LLaMA3 model

🤖 Auto Mode (Intelligent Agent)
1. Enter your question or topic (e.g., "Vietnam's economy in 2025")

2. The system will:

    .Visit VnExpress.net

    .Search for articles that match your query

    .Extract content and analyze with LLM

3. The result is shown in the same language as your input

💬 Example Queries
.Vietnamese:
    "Người trẻ ở New York đang gặp khó khăn gì?"

.English:
    "What challenges are young people in New York facing?"

⚠️ Notes
    .Results depend on the actual content found on VnExpress.net

    .The system does not generate new information, only analyzes based on found articles

    .If no relevant article is found, the result will be empty