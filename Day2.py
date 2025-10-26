import streamlit as st

st.title("Welcome to Day 2 of Streamlit !")
st.subheader("Biriyani Maker App")
if st.button("Make Biriyani "):
    st.success("Biriyani is Ready !")

masala=st.checkbox("Add extra spice")
if masala:
    st.write("Extra spice added to your Biriyani !")

biriyani_type=st.radio("Choose your Biriyani type",["Chicken Biriyani","Mutton Biriyani","Veg Biriyani"])

st.write("You have selected : ", biriyani_type)

flavor=st.selectbox("Choose your flavor",["Mild","Medium","Spicy","Extra Spicy"])
st.write("You have selected flavor : ", flavor)

quantity=st.slider("Select quantity (in plates)",0,10,1)
st.write("You have selected ", quantity, " plates of Biriyani") 

st.number_input("Enter number of people to serve",1,20,1)

name=st.text_input("Enter your name")
if name:
    st.write("Hello ", name, "! Your Biriyani order is being prepared.")

dob=st.date_input("Enter your date of birth")
st.write("Your date of birth is : ", dob)

st.subheader("Date calculator")
from datetime import date
today=date.today()
dob=st.date_input("Enter your date of birth for age calculation")
age=today.year - dob.year
st.write("Your age is : ", age, " years")   
