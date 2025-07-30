from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
from parse import analyze_articles_with_llm

def auto_scrape_vnexpress(query):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.set_page_load_timeout(20)
        driver.get("https://vnexpress.net/")
        time.sleep(5)

        soup = BeautifulSoup(driver.page_source, "html.parser")

        articles = []
        seen = set()

        # Thu thập các link bài viết chứa từ khóa
        for a in soup.select("a[href*='vnexpress.net']"):
            title = a.text.strip()
            href = a["href"]

            if query.lower() in title.lower() and href not in seen and href.startswith("https://vnexpress.net/"):
                seen.add(href)
                articles.append({"title": title, "url": href})

            if len(articles) >= 5:
                break

        if not articles:
            return {
                "titles": [],
                "analysis": "Không tìm thấy bài viết phù hợp."
            }

        article_texts = []
        article_titles = []

        # Truy cập từng bài và thu thập nội dung
        for article in articles:
            try:
                driver.set_page_load_timeout(15)
                driver.get(article["url"])
                time.sleep(3)

                page_soup = BeautifulSoup(driver.page_source, "html.parser")
                paragraphs = page_soup.select("article p")

                text = "\n".join(p.text.strip() for p in paragraphs if len(p.text.strip()) > 30)

                if text:
                    article_texts.append(text)
                    article_titles.append(article["title"])
            except Exception as e:
                print(f"[Bỏ qua bài viết lỗi]: {article['url']}")
                print(f"Lỗi: {e}")
                continue

        if not article_texts:
            return {
                "titles": article_titles,
                "analysis": "Không thể phân tích vì không trích xuất được nội dung từ các bài báo."
            }

        analysis = analyze_articles_with_llm(article_texts, query)

        return {
            "titles": article_titles,
            "analysis": analysis
        }

    finally:
        driver.quit()
