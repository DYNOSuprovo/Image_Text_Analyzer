
### Streamlit App (Model 2 - LLM Processing)
import streamlit as st
import requests
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

st.title("Image Text Analysis with LLM")

uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    files = {'image': uploaded_file.getvalue()}
    response = requests.post("http://127.0.0.1:5000/extract-text", files=files)
    
    if response.status_code == 200:
        extracted_text = response.json().get("extracted_text", "")
        st.subheader("Extracted Text:")
        st.write(extracted_text)
        
        # LLM Processing
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a instructor or explainer wo explain in simple terms like a guide part by part and answer question also "),
            ("user", "Question:{question}")
        ])
        llm = Ollama(model="llama3")
        output_parser = StrOutputParser()
        chain = prompt | llm | output_parser
        
        result = chain.invoke({"question": extracted_text})
        st.subheader("LLM Analysis:")
        st.write(result)
    else:
        st.error("Error extracting text from image")
