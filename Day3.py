import streamlit as st
st.title("Welcome to Day 3 of Streamlit!")

col1, col2 = st.columns(2)
with col1:
    st.header('this is Column 1')
    st.image('https://static.vecteezy.com/system/resources/thumbnails/049/855/347/small/nature-background-high-resolution-wallpaper-for-a-serene-and-stunning-view-photo.jpg', width=200)
    vote1=st.button('Vote for Column 1')

with col2:
    st.header('this is Column 2')
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSVwGt_qWyifgkbhxRUco7Ay1lD7XotxINlgp5KzPhmf4wB6WJpTvuHOIn8Mlkh0oNpHNw&usqp=CAU', width=200)
    vote2=st.button('Vote for Column 2')

if vote1:
    st.success("You voted for Column 1!")
elif vote2:
    st.success("You voted for Column 2!")

name=st.sidebar.text_input("Enter your name")
pic=st.sidebar.selectbox("Choose your profile picture",['🐶','🐱','🦊','🐵','🐻‍❄️'])
if name and pic:
  st.write("Welcome {name} and {pic} is set as your profile picture".format(name=name,pic=pic))

st.markdown("---")
with st.expander("See explanation"):
    st.write("""
        This is an example of using Streamlit to create a simple voting app with two columns.
        You can vote for your favorite column by clicking the respective button.
        Additionally, you can enter your name and select a profile picture from the sidebar.
    """)

st.markdown("---")