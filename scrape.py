# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from bs4 import BeautifulSoup
# from webdriver_manager.chrome import ChromeDriverManager
# # pip install webdriver-manager

# def scrape_website(website):
#     print("Launching local Chrome browser...")
#     options = Options()
#     options.add_argument("--headless")  # bỏ nếu muốn xem trình duyệt
#     options.add_argument("--disable-gpu")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--window-size=1920,1080")

#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#     try:
#         driver.get(website)
#         print("Navigated! Scraping page content...")
#         html = driver.page_source
#         return html
#     finally:
#         driver.quit()


# def extract_body_content(html_content):
#     soup = BeautifulSoup(html_content, "html.parser")
#     body_content = soup.body
#     return str(body_content) if body_content else ""


# def clean_body_content(body_content):
#     soup = BeautifulSoup(body_content, "html.parser")

#     for script_or_style in soup(["script", "style"]):
#         script_or_style.extract()

#     cleaned_content = soup.get_text(separator="\n")
#     cleaned_content = "\n".join(
#         line.strip() for line in cleaned_content.splitlines() if line.strip()
#     )
#     return cleaned_content


# def split_dom_content(dom_content, max_length=6000):
#     return [
#         dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
#     ]


#scrape.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time

# Cấu hình Selenium (headless + nhanh)
def get_driver():
    options = Options()
    options.add_argument("--headless=new")  # 'new' giúp tránh cảnh báo
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Truy cập trang và trả lại HTML
def scrape_website(website, delay=3):
    print(f"[INFO] Truy cập {website}")
    driver = get_driver()

    try:
        driver.get(website)
        time.sleep(delay)  # chờ tải nội dung động
        html = driver.page_source
        return html
    except Exception as e:
        print(f"[ERROR] Không thể tải trang: {e}")
        return ""
    finally:
        driver.quit()

# Trích nội dung <body>
def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    return str(body_content) if body_content else ""

# Làm sạch thẻ HTML: bỏ script/style
def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    return cleaned_content

# Chia nhỏ nội dung nếu quá dài
def split_dom_content(dom_content, max_length=4000):
    return [
        dom_content[i : i + max_length]
        for i in range(0, len(dom_content), max_length)
    ]
