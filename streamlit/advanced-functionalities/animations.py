import streamlit as st
import json
import streamlit.components.v1 as com
from streamlit_lottie import st_lottie

# using iframe for animation
com.iframe(src="https://lottie.host/embed/6ddaa577-e6e0-43d5-a659-f7ffb2d7522a/XPRMpbP3pw.json") 
# acquired from lottiefiles

st.markdown("---",unsafe_allow_html=True)

# using json for animation
with open("animation.json") as file:
    animation = json.load(file)
st_lottie(animation,reverse=True,speed=2)

