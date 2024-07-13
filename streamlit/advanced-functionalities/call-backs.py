import streamlit as st 

input = st.number_input("Please enter your numbers?")
bt = st.button("Submit")
def calculator(numbers):
    st.write(f"{(numbers/1100)*100:.2f}%")
if bt:
    st.checkbox("Show me my percentage",on_change=calculator,args=(input,))