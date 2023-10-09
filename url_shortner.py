import pyperclip
import streamlit as st
import pyshorteners as pyst



shortner = pyst.Shortener()

hide_style ="""
<style>
      #MainMenu {visibility:hidden}
      footer {visibility:hidden}
      header {visibility:hidden}


"""
st.markdown(hide_style,unsafe_allow_html=True)
with open('./design_url.css') as source:
    st.markdown(f"<style>{source.read()}</style>",unsafe_allow_html=True)


st.markdown("<h1 style='text-align:center;'>URL Shortner</h1>",unsafe_allow_html=True)
def copying():
    pyperclip.copy(shortened_url)

form = st.form("Name")
url = form.text_input("URL Here:")
btn = form.form_submit_button("Short")
if btn:
    shortened_url = shortner.tinyurl.short(url)
    st.markdown("<h3>Shortend Url</h3>",unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align:center;'>{shortened_url}</h5>",unsafe_allow_html=True)
    st.button("Copy",on_click=copying)
