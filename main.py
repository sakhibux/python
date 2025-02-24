
import streamlit as st

# ایپ کا ٹائٹل
st.title("Simple Streamlit App")

# یوزر سے ان پٹ لینا
name = st.text_input("Enter your Name:")
message = st.text_area("Enter your Father Name:")

# جب یوزر بٹن دبائے
if st.button("Submit"):
    st.write(f"### Hello, {name}!")
    st.write(f"Your Father Name: {message}")

# اضافی فیچر: یوزر کی پسندیدہ رنگ کا انتخاب
color = st.color_picker("Pick a color", "#00f900")
st.write(f"You selected: {color}")
