import httpx
import base64
import google.generativeai as genai
import streamlit as st
from PIL import Image

genai.configure(api_key="AIzaSyB5F3mRxEOlbyyq0ZlE_pmGCkqPlVdzJo8")

st.title("Animal Species Identifier")

user_input = st.text_input("Enter some text (optional):")
if user_input:
    st.write(f"You entered: {user_input}")

uploaded_file = st.file_uploader("Choose an animal image file:", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    img_data = uploaded_file.getvalue()
    img_base64 = base64.b64encode(img_data).decode('utf-8')

    def get_species_and_name(img_base64: str):
        model = genai.GenerativeModel(model_name="gemini-1.5-pro")

        prompt = "Identify the animal species in this image and provide its Domain Kingdom Phylum Mirorder Order"

        try:
            response = model.generate_content([{
                'mime_type': f'image/{uploaded_file.name.split(".")[-1]}',
                'data': img_base64
            }, prompt])

            response_text = response.text
            st.write("Response from AI: ", response_text)

        except Exception as e:
            st.error(f"Error occurred: {e}")

    get_species_and_name(img_base64) 
