import streamlit as st
text = "yes"
if "click" not in st.session_state:
    st.session_state.click=False
else: 
    if st.session_state.click == False:
        text = "no"
        st.session_state.click = True
    else: 
        text = "yes"
        st.session_state.click = False

st.button(text)