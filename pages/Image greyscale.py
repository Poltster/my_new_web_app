import streamlit
import streamlit as sg
from PIL import Image

sg.subheader("Color to Grayscale converter")

uploaded_image = streamlit.file_uploader("Upload image")

if uploaded_image:
    img = Image.open(uploaded_image)
    gray_uploaded_image = img.convert("L")
    sg.image(gray_uploaded_image)