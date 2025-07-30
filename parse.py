# from langchain_ollama import OllamaLLM
# from langchain_core.prompts import ChatPromptTemplate

# template = (
#     "You are tasked with extracting specific information from the following text content: {dom_content}. "
#     "Please follow these instructions carefully: \n\n"
#     "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
#     "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
#     "3. **Empty Response:** If no information matches the description, return an empty string ('')."
#     "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
# )

# model = OllamaLLM(model="llama3")


# def parse_with_ollama(dom_chunks, parse_description):
#     prompt = ChatPromptTemplate.from_template(template)
#     chain = prompt | model

#     parsed_results = []

#     for i, chunk in enumerate(dom_chunks, start=1):
#         response = chain.invoke(
#             {"dom_content": chunk, "parse_description": parse_description}
#         )
#         print(f"Parsed batch: {i} of {len(dom_chunks)}")
#         parsed_results.append(response)

#     return "\n".join(parsed_results)


#parse.py
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Prompt tối ưu cho yêu cầu truy vấn tiếng Việt/Anh
template = (
    "You are an AI assistant that analyzes news articles and responds in the same language as the user's query.\n\n"
    "Here are one or more article contents:\n"
    "{dom_content}\n\n"
    "User's request:\n"
    "\"{parse_description}\"\n\n"
    "Instructions:\n"
    "1. Answer based only on the provided article content.\n"
    "2. Respond in the same language as the query.\n"
    "3. Do not add explanations, summaries, or opinions.\n"
    "4. If the content does not contain the requested information, return an empty string (\"\")."
)

model = OllamaLLM(model="llama3")

def parse_with_ollama(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    results = []

    for chunk in dom_chunks:
        response = chain.invoke({
            "dom_content": chunk,
            "parse_description": parse_description
        })
        if response.strip():
            results.append(response.strip())

    return "\n\n".join(results)

def analyze_articles_with_llm(article_texts, query):
    # Ghép các bài thành một khối phân tích
    dom_content = "\n\n---\n\n".join(article_texts)
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    return chain.invoke({
        "dom_content": dom_content,
        "parse_description": query
    })
