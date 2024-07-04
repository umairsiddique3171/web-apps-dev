import streamlit as st
from bs4 import BeautifulSoup
import requests
import webbrowser
from utils import set_background

st.set_page_config(
    page_title="Scraper",
    page_icon="〽",
    layout="wide")
st.markdown("<h1 style='text-align:center;'>Web Scraper</h1>",unsafe_allow_html=True)
set_background("background_img.jpg")
cl1,_,_ = st.columns(3)
with cl1:
    key_word = st.text_input("Enter your keyword")
btn = st.button("Search")
if key_word is not None: 
    placeholder = st.empty()
    col1,col2,col3 = placeholder.columns(3)
    page = requests.get(f"https://unsplash.com/s/photos/{key_word}")
    soup = BeautifulSoup(page.content,"lxml")
    tables = soup.find_all("div",class_ = "d95fI")
    img_urls = []
    for table in tables:
        if len(img_urls) <= 12:
            figures = table.find_all("figure")
            img_urls_renew = []
            for figure in figures: 
                if len(img_urls_renew) <= 3:
                    img_url = figure.find('img',class_ = "ApbSI z1piP vkrMA")["srcset"].split("?")[0]
                    download_url = "https://unsplash.com/" + figure.find('a',class_="Prxeh")["href"]
                    if img_url not in img_urls: 
                        img_urls.append(img_url)
                        img_urls_renew.append(img_url)
                        if len(img_urls_renew) == 3 : 
                            col1.image(img_urls_renew[0])
                            col2.image(img_urls_renew[1])
                            col3.image(img_urls_renew[2])
                            with col1: 
                                btn1 = st.button("Download",key = str(img_urls.index(img_urls_renew[0])))
                                if btn1:
                                    webbrowser.open_new_tab(download_url)  
                            with col2: 
                                btn2 = st.button("Download",key = str(img_urls.index(img_urls_renew[1])))
                                if btn2:
                                    webbrowser.open_new_tab(download_url)

                            with col3:
                                btn3 = st.button("Download",key = str(img_urls.index(img_urls_renew[2])))
                                if btn3:
                                    webbrowser.open_new_tab(download_url)           
                    else: 
                        pass
                else:
                    break
        else:
            break
