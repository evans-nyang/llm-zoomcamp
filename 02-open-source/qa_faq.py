import streamlit as st
import time

from openai import OpenAI
from elasticsearch import Elasticsearch

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama'
)

es_client = Elasticsearch('http://localhost:9200')

def elastic_search(query, index_name = 'course-questions'):
    search_query = {
        "size": 5,
        "query": {
            "bool": {
                "must": {
                    "multi_match": {
                        "query": query,
                        "fields": ["question^3", "text", "section"],
                        "type": "best_fields"
                    }
                },
                "filter": {
                    "term": {
                        "course": "data-engineering-zoomcamp"
                    }
                }
            }
        }
    }

    response = es_client.search(index=index_name, body=search_query)

    result_docs = []

    for hit in response['hits']['hits']:
        result_docs.append(hit['_source'])

    return result_docs

def build_prompt(query, search_results):
    prompt_template = """
        You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database. 
        Use only the facts from the CONTEXT when answering the QUESTION.

        QUESTION: {question}

        CONTEXT: {context}
    """.strip()

    context_str = ""

    for doc in search_results:
        context_str = context_str + f"section: {doc['section']}\nquestion: {doc['question']}\nanswer: {doc['text']}\n\n"

    prompt = prompt_template.format(question=query, context=context_str).strip()
    return prompt 

def llm(prompt):
    response = client.chat.completions.create(
        model = 'phi3',
        messages = [{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

def rag(query):
    search_results = elastic_search(query)
    prompt = build_prompt(query, search_results)
    answer = llm(prompt)
    return answer

# Streamlit app
def main():
    st.title("RAG Function Invocation")

    # Input box
    user_input = st.text_input("Enter your input: ")

    # Button to invoke the RAG function
    if st.button("Ask"):
        with st.spinner('Processing your input...'):
            # Call the RAG function
            output = rag(user_input)
            st.success('Completed!')
            st.write(output)

if __name__ == "__main__":
    main()
