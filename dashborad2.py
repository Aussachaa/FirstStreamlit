import plotly.figure_factory as ff
import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')


st.set_page_config(page_title="Superstore!!!",
                   page_icon=":bar_chart:",
                   layout="wide")

st.title(" :bar_chart: Sample SuperStore EDA")
st.markdown(
    '<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

fl = st.file_uploader(":file_folder: Upload a file",
                      type=(["csv", "txt", "xlsx", "xls"]))

path_file = r"https://raw.githubusercontent.com/Aussachaa/FirstStreamlit/main/Sample%20-%20Superstore.csv"
if fl is not None:
    filename = fl.name
    st.write(filename)
    df = pd.read_csv(filename, encoding="ISO-8859-1")
else:
    # os.chdir(r"C:\Users\aussa\OneDrive\เดสก์ท็อป\Python\Streamlit\FirstStreamlit")
    df = pd.read_csv(path_file, encoding="ISO-8859-1")

st.write(df)

col1, col2 = st.columns((2))

# Getting the min and max date

with col1:
    date1 = pd.to_datetime(st.date_input("Start Date", '2023-10-14'))

with col2:
    date2 = pd.to_datetime(st.date_input("End Date", '2033-10-14'))
