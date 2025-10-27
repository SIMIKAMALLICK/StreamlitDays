import streamlit as st
import pandas as pd
st.title("Day 4: Data Visualization with Streamlit")

file=st.file_uploader("Upload your CSV file", type=["csv"])
if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview of Netflix Movies and TV Shows")
    st.dataframe(df)

if file:
    st.subheader("Summary Statistics")
    st.write(df.describe())

if file:
    tp=df['type'].unique()
    selected_type=st.selectbox("Filter by Type", tp)
    filtered_data=df[df["type"]==selected_type]
    st.dataframe(filtered_data)