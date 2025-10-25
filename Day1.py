import streamlit as st

st.title("Welcome to Day 1 of Streamlit ")
st.subheader("Getting Started with Streamlit")
st.text("This is a simple Streamlit app to help you get started with building web applications using Streamlit.")
st.write("Streamlit makes it easy to create and share beautiful, custom web apps for machine learning and data science.")

sub=st.selectbox("Your fav subject",["Maths","Science","English","History","Geography"])
st.write("Your fav sub : ", sub)

st.success("You have successfully completed Day 1 of Streamlit!")