import streamlit as st
import pyshorteners as pystr
import pyperclip as pclp
from utils import set_background

st.set_page_config(page_title='url-shortener',page_icon='🔗')

set_background('background_img.jpg')

st.markdown("""
<style>
.stDeployButton
{
    visibility : hidden;
}
.st-emotion-cache-czk5ss.e16jpq800
{
    visibility : hidden;
}
</style>
""", unsafe_allow_html=True)

def copying():
    pclp.copy(shorted_url)

shortener = pystr.Shortener()
st.markdown("<h1 style = 'text-align: center;'>URL Shortener</h1>",unsafe_allow_html=True)
form = st.form("url_shortener")
url = form.text_input("URL here")
bt = form.form_submit_button("short")

if bt: 
    shorted_url = shortener.tinyurl.short(url)
    st.subheader("Shorted URL")
    _,col2,col3 = st.columns(3)
    with col2: 
        st.markdown(f"""<div style='display: flex; align-items: center; justify-content: center; height: 10vh;'>
                    <h6>{shorted_url}</h6></div>""", unsafe_allow_html=True)
    with col3: 
        st.button("Copy",on_click=copying)