import streamlit as st

st.set_page_config(page_title="My Simple Streamlit App", layout="centered")

st.title("My Simple Streamlit App")

st.write("Hello, World! This is a minimal Streamlit app.")

# Example interaction
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")
