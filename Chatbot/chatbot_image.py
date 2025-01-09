import os
from langchain_google_genai import GoogleGenerativeAI
import streamlit as st
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai
from langchain_openai import ChatOpenAI

load_dotenv()

google_api_key = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=google_api_key)

llm= genai.GenerativeModel('gemini-1.5-flash')

def get_response(query, image):
    response= llm.generate_content([query, image])
    return response.text

st.set_page_config('Chatbot Application', layout='centered')

st.title('Chatbot Application')

st.divider()

image_uploader= st.file_uploader("Upload Image")

if image_uploader:
    image = Image.open(image_uploader)

query = st.text_input('Enter the query...')

if st.button('Submit'):
    response= get_response(query, image)
    st.write(response)

# open_api_key = os.getenv('OPENAI_KEY')

# llm= ChatOpenAI(model= 'gpt-4o-mini', api_key=open_api_key)

# def get_response(query, image):
#     response= llm.generate_content([query, image])
#     return response.text

# st.set_page_config('Chatbot Application', layout='centered')

# st.title('Chatbot Application')

# st.divider()

# image_uploader= st.file_uploader("Upload Image")

# if image_uploader:
#     image = Image.open(image_uploader)

# query = st.text_input('Enter the query...')

# if st.button('Submit'):
#     response= get_response(query, image)
#     st.write(response)