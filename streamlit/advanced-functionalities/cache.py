import streamlit as st 
import time
import warnings
warnings.filterwarnings("ignore")

# @st.cache_data
# def func():
#     time.sleep(5)
#     return "Message"

# st.write(func())

@st.cache(suppress_st_warning=True)
def printer():
    st.write("Please wait...")
    time.sleep(3)
    return "Message"

st.write(printer())