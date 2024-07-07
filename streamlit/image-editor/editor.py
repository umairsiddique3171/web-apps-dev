from PIL import Image, ImageFilter
import streamlit as st
from utils import set_background

st.set_page_config(
    page_title="Image Editor",
    page_icon="🖌")
set_background("background_img.jpg")
st.markdown("<h1 style='text-align:center;' >Image Editor</h1>",unsafe_allow_html=True)
st.markdown("---")
img = st.file_uploader("Upload your image",type=['jpg','jpeg','png'])
if img:
    st.image(img)
    form = st.form("Form 1")
    info = form.empty()
    size = form.empty()
    mode = form.empty()
    format_ = form.empty()
    img = Image.open(img)
    info.header("Info")
    size.text(img.size)
    mode.text(img.mode)
    format_.text(img.format)
    form.markdown("---")
    form.header("Resizing")
    col1,col2 = form.columns(2)
    with col1:
        width = st.number_input("Width",value=img.width)
    with col2: 
        height = st.number_input("Height",value=img.height)
    form.markdown("---")
    form.header("Rotate")
    degree = form.slider("Rotation°",
                         min_value=0,
                         max_value=360,
                         step=1,
                         value=0)
    form.markdown("---")
    form.header("Filters")
    filters = form.selectbox("Filters",
                             options=("None","Blur","Contour","Detail","Sharpen","Smooth"),
                             index=0)
    btn = form.form_submit_button("Submit")
    if btn:
        st.success("Form Submitted Successfully")
        edited = img.resize((width,height)).rotate(degree)
        filtered = edited
        if filters != "None":
            if filters == "Blur":
                filtered = edited.filter(ImageFilter.BLUR)
            elif filters == "Contour":
                filtered = edited.filter(ImageFilter.CONTOUR)
            elif filters == "Detail":
                filtered = edited.filter(ImageFilter.DETAIL)
            elif filters == "Sharpen":
                filtered = edited.filter(ImageFilter.SHARPEN)
            elif filters == "Smooth":
                filtered = edited.filter(ImageFilter.SMOOTH)
        st.image(filtered)
