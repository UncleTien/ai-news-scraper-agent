# import streamlit as st
# from scrape import (
#     scrape_website,
#     extract_body_content,
#     clean_body_content,
#     split_dom_content,
# )
# from parse import parse_with_ollama

# # Streamlit UI
# st.title("Demo Scraper")
# url = st.text_input("Enter Website URL")

# # Step 1: Scrape the Website
# if st.button("Scrape Website"):
#     if url:
#         st.write("Scraping the website...")

#         # Scrape the website
#         dom_content = scrape_website(url)
#         body_content = extract_body_content(dom_content)
#         cleaned_content = clean_body_content(body_content)

#         # Store the DOM content in Streamlit session state
#         st.session_state.dom_content = cleaned_content

#         # Display the DOM content in an expandable text box
#         with st.expander("View DOM Content"):
#             st.text_area("DOM Content", cleaned_content, height=300)


# # Step 2: Ask Questions About the DOM Content
# if "dom_content" in st.session_state:
#     parse_description = st.text_area("Describe what you want to parse")

#     if st.button("Parse Content"):
#         if parse_description:
#             st.write("Parsing the content...")

#             # Parse the content with Ollama
#             dom_chunks = split_dom_content(st.session_state.dom_content)
#             parsed_result = parse_with_ollama(dom_chunks, parse_description)
#             st.write(parsed_result)



# main.py
import streamlit as st
from scrape import scrape_website, extract_body_content, clean_body_content, split_dom_content
from parse import parse_with_ollama, analyze_articles_with_llm
from vnexpress_agent import auto_scrape_vnexpress

st.set_page_config(layout="wide")
st.title("AI Web Agent - Phân tích tin tức tự động")

mode = st.radio("Chọn chế độ hoạt động:", ["Thủ công với URL", "Tự động từ VnExpress"])

#CHẾ ĐỘ 1: THỦ CÔNG VỚI URL
if mode == "Thủ công với URL":
    url = st.text_input("Nhập URL bài viết")

    if st.button("Scrape Website") and url:
        st.write("Đang lấy nội dung từ website...")
        dom_content = scrape_website(url)
        body_content = extract_body_content(dom_content)
        cleaned_content = clean_body_content(body_content)
        st.session_state.dom_content = cleaned_content

        with st.expander("Xem nội dung đã trích xuất"):
            st.text_area("DOM Content", cleaned_content, height=300)

    if "dom_content" in st.session_state:
        parse_description = st.text_area("Bạn muốn trích xuất thông tin gì?")
        if st.button("Phân tích Nội dung") and parse_description:
            st.write("Đang phân tích với mô hình LLM...")
            dom_chunks = split_dom_content(st.session_state.dom_content)
            parsed_result = parse_with_ollama(dom_chunks, parse_description)
            st.subheader("Kết quả phân tích:")
            st.write(parsed_result)

#CHẾ ĐỘ 2: TỰ ĐỘNG TỪ VNEXPRESS
elif mode == "Tự động từ VnExpress":
    query = st.text_input("Nhập câu hỏi hoặc chủ đề bạn quan tâm:")
    if st.button("Tìm và Phân tích") and query:
        with st.spinner("Đang thu thập và phân tích bài viết từ VnExpress..."):
            result = auto_scrape_vnexpress(query)
            st.subheader("Kết quả phân tích:")
            
            st.write(result)  # Xem kết quả thực tế để biết có gì trong result
            if 'analysis' in result:
                st.write(result['analysis'])
            else:
                st.warning("Không tìm thấy phân tích trong kết quả.")

            st.write(result['analysis'])

            if result['titles']:
                with st.expander("Các tiêu đề bài viết liên quan"):
                    for title in result['titles']:
                        st.markdown(f"- {title}")
            else:
                st.warning("Không tìm thấy bài viết liên quan phù hợp với truy vấn.")
