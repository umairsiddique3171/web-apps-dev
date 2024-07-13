import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import set_background

st.set_page_config(page_title='data-visualizer',page_icon='📈')

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

plt.style.use('seaborn-darkgrid')

st.markdown("<h1 style='text-align:center;'>Data Visualizer</h1>",unsafe_allow_html=True)
st.markdown("---")
files = st.file_uploader("Upload Multiple Files",type=["xlsx","csv"],accept_multiple_files=True)
file_names = list()
data_frames = list()

if files: 
    for file in files:
        file_names.append(file.name)
        if file.name.endswith('.csv'):
            data_frames.append(pd.read_csv(file))
        elif file.name.endswith('.xlsx'):
            data_frames.append(pd.read_excel(file))
    selected_files = st.multiselect("Select Files",options=file_names)
    if selected_files:
        option = st.radio("Select Any Product",options=["None"] + list(data_frames[0].columns)[1:])
        if option != "None":
            plt.figure(figsize=(10, 5))
            for selected_file in selected_files:
                idx = file_names.index(selected_file)
                df = data_frames[idx]
                dates = [i.split('T')[0] for i in df['Date'].values]
                option_values = df[option].values
                plt.plot(dates, option_values, marker='o', linestyle='-', label=selected_file)
            plt.xlabel('Date')
            plt.ylabel(option)
            plt.title(f'{option} Over Time')
            plt.legend()
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(plt)
            plt.clf()