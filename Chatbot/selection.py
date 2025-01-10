import os
import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def get_llm(api_type, api_key):
    if api_type == 'google':
        return GoogleGenerativeAI(model='gemini-pro', api_key=api_key)
    elif api_type == 'openai':
        return ChatOpenAI(api_key=api_key)
    else:
        raise ValueError("Unsupported API type")

st.set_page_config('Chatbot Application', layout='centered')
st.title('Chatbot Application')
st.divider()
st.caption('What can I help with?')
st.sidebar.title('settings')
st.sidebar.slider("temperature", min_value=0.0, max_value=1.0, value=0.7)
st.sidebar.slider("max_token", min_value=50, max_value=200, value=100)

open_api_key = os.getenv('OPENAI_KEY')   
google_api_key = os.getenv('GOOGLE_API_KEY') 

query=st.text_input("Enter your query here...")

if st.button('OpenAI'):
    llm= ChatOpenAI(api_key=open_api_key)
    User='User'
    Chatbot='Chatbot'
    response = llm.invoke(query)
    st.write(f'{response.content}')

elif st.button('GoogleAI'):
    llm= GoogleGenerativeAI(model='gemini-pro', api_key=google_api_key)
    User='User'
    Chatbot='Chatbot'
    response = llm.invoke(query)
    st.write(f'{response}')

