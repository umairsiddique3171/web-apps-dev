import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time 
import datetime

df = pd.DataFrame({"col1":[1,2,3,4],"col2":[5,6,7,8]})

# hidding not useful stuff
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

st.title("Tutorial")

st.header("header")

st.subheader("subheader")

st.markdown("###### This is markdown text")

st.text("This is text")

st.caption("These are caption")

# mathematics
st.latex(r"\begin{matrix}a & b \\c & d\end{matrix}")

st.markdown("[latex-cheatsheet](https://katex.org/docs/supported)")

json = {"a":2,"b":2}
st.json(json)

code = """
a = 2
b = 3
print(a+b)
"""
st.code(code,language="python")

st.write("writing text")
st.markdown("---")

st.metric(label="wind speed",value="23.1 ms⁻¹",delta = "1.8ms⁻¹")
st.markdown("---")

st.table(df)
st.markdown("---")

st.dataframe(df)
st.markdown("---")

# checkbox
def change():
    print("changed")
    print(st.session_state.check)
    print("-----------------------------------------------------------")
state = st.checkbox("task",on_change=change,key="check")
if state:
    st.caption("Done!!!")
else:
    st.caption("Not Done!!!")
st.markdown("---")

# radio
radio_bn = st.radio("What is ur native language?",options=('english','russian','arabic','urdu'))
st.markdown("---")

# button
def submitted():
    print("submitted")
button = st.button('Submit',on_click=submitted)
st.markdown("---")

# select
select = st.selectbox("What's ur favourite laptop?",options=("Alienware","Victus","Spectre","XPS"))
st.markdown("---")

# multi-select
multi_select = st.multiselect("What's ur favourite car?",options=("Benz","BMW","Audi","RollsRoyce"))
st.markdown("---")

# uploading img
img = st.file_uploader("please upload an image",type=['png','jpeg','jpg'])
if img is not None:
    st.image(img)

# uploading multiimages
imgs = st.file_uploader("please upload multiple images",type=['png','jpeg','jpg'],accept_multiple_files=True)
if imgs is not None:
    for img in imgs:
        st.image(img)
st.markdown("---")

# slider
val = st.slider("Length(m)",min_value=50,max_value=100,step=2)
st.markdown("---")

# text user input
input = st.text_input("Enter your phone no.",max_chars = 11)
descriptive_input = st.text_area("Enter your address")
st.markdown("---")

# date input
val = st.date_input("Enter your date of birth")
st.markdown("---")

# time input
val = st.time_input("Enter current time")
st.markdown("---")

# progress bar
def converter(val):
    h,m,s = val.split(":")
    ts = (int(h)*3600) + (int(m)*60) + int(s)
    return ts
val = st.time_input("Timer",value=datetime.time(0,0,0))
if str(val) == "00:00:00":
    st.write("Please Set Timer")
else: 
    bar = st.progress(0)
    progress_status = st.empty()
    for i in range(100):
        bar.progress((i+1))
        progress_status.write(str(i+1) + "%")
        time.sleep(converter(str(val))/100)
st.markdown("---")

# forms
form = st.form("Form 1")
first_name = form.text_input("First Name")
last_name = form.text_input("Last Name")
em = form.text_input("Email")
ps = form.text_input("Password")
cps = form.text_input("Confirm Password")
bt = form.form_submit_button("Submit")
if bt :
    if ps == cps: 
        print(first_name + " " + last_name + " - " + em + " - " + ps)
        st.success("Form Submitted Successfully")
    else: 
        st.warning("Passwords are not matched. Please try signing up again.")
st.markdown("---")

# forms with multicolumns
with st.form("Form 2"):
    col1,col2 = st.columns(2)
    with col1: 
        first_name = st.text_input("First Name")
    with col2: 
        last_name = st.text_input("Last Name")
    em = st.text_input("Email")
    col1,col2,col3 = st.columns(3)
    with col1:
        day = st.text_input("Day")
    with col2:
        month = st.text_input("Month")
    with col3:
        year = st.text_input("Year")
    ps = st.text_input("Password")
    cps = st.text_input("Confirm Password")
    bt = st.form_submit_button("Submit")
    if bt :
        if ps==cps:
            print(first_name + " " + last_name + " - " + em + " - " + ps)
            st.success("Form Submitted Successfully")
        else:
            st.warning("Passwords are not matched. Please try signing up again.")
st.markdown("---")

# sidebar and charts
x = np.linspace(0,10,100)
bar_x = np.array([1,2,3,4,5])
opt = st.sidebar.radio("Select Any Graph",options=["Bar","Line"])
if opt=="Line":
    fig = plt.figure()
    plt.plot(x,np.sin(x))
    st.write(fig)
elif opt=="Bar":
    fig = plt.figure()
    plt.bar(bar_x,bar_x*10)
    st.write(fig)
