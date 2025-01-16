import os
from dotenv import load_dotenv
import streamlit as st


load_dotenv()

def main():
    pages= { 
        "Text generation": [st.Page("app.py", title="Text to Text")],
        "Image generation": [st.Page("chatbot_image.py", title="Image to Text")],
        "Audio generation": [st.Page("chatbot_audio.py", title="Audio to Text")],
    }
                                     
    selected_page= st.navigation(pages)
    selected_page.run()

if __name__ == "__main__":
    main()

