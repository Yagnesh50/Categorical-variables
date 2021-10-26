import streamlit as st

st.title("GUI for Machine Learning Model")

st.subheader("Welcome to the sample GUI")
st.radio("Select the option",[1,2,3])
st.text_input("Enter some value")
st.button("Hit me")
st.text_area("Area for textual entry")
st.file_uploader("Enter the files you want to upload")
st.color_picker("Pick a colour you like")

st.slider("Slide the bar",min_value=0,max_value=10)

st.sidebar.button("Apply")

