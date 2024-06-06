from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
import requests
import os
import streamlit as st

load_dotenv(find_dotenv())
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")


def img2text(url):
    image_to_text = pipeline("image-to-text",model="Salesforce/blip-image-captioning-base")

    text = image_to_text(url)[0]["generated_text"]
    print("------------------------------------------------------\n")
    print(text)
    return text

# outputText = img2text("https://huggingface.co/datasets/Narsil/image_dummy/resolve/main/parrots.png")


def text2speech(message):
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"}
    payloads = {
        "inputs": message
    }
    
    response = requests.post(API_URL, headers=headers, json=payloads)
    with open('audio.flac', 'wb') as file:
        file.write(response.content)

# text2speech("This is is a great college")

def main():
    st.set_page_config(page_title="img 2 text 2 audio")
    st.header("Scan image to text and read out loud")
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        print(uploaded_file)
        bytes_data = uploaded_file.getvalue()
        with open(uploaded_file.name, "wb") as file:
            file.write(bytes_data)
        st.image(uploaded_file, caption="Uploaded image", use_column_width=True)
        scenario = img2text(uploaded_file.name)
        text2speech(scenario)

        with st.expander("scenario"):
            st.write(scenario)

        st.audio("audio.flac")
if __name__ == '__main__':
    main()