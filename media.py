#Gambar
import streamlit as st
from PIL import Image


st.text("Kelas awan pintar")

st.header("Ayo Belajar cara untuk menampilkan media element di streamlit")

st.markdown("""

1. Image
            
2. Audio
            
3. Video
            
========================== Contohnya ========================
""", True)
#image
image1 = Image.open('image/img1.png')

st.image(image1, caption='Ini logo ITG')

import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")
   
#Audio
audio = open('image/audio.mp3', 'rb')
audio = audio.read()

st.audio(audio)

#vidio
video = open('image/vidio1.mp4', 'rb')
vidio1 = video.read()

st.video(vidio1)