import os
from langchain_openai import ChatOpenAI
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# openai_api_key = os.getenv('OPENAI_KEY')

# llm= ChatOpenAI(api_key=openai_api_key)    #created llm model

google_api_key = os.getenv('Google_API_KEY')

llm = GoogleGenerativeAI(model='gemini-1.5-flash',api_key=google_api_key)  # created llm model

while True:
    query= input("Enter the query:")    #access model
    result= llm.invoke(query)
    print(result)
                                     


