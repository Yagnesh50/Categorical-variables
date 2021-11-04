import streamlit as st

st.title("House price prediction website")

st.subheader("Welcome to the sample GUI")
st.sidebar.radio("Selects the number you want",[1,2,3,4,5,6,7,8])
st.text_input("Enter some value")
st.button("Hit me")


st.selectbox("Select the option wanted",("Ford","Ferrari","Rolls Royce","BMW"))

st.color_picker("Pick a colour")
st.checkbox("Check this out")

st.slider("Slide the bar",min_value=0,max_value=10)



