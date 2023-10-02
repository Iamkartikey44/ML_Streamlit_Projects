import streamlit as st
import re

st.markdown("<h1 style='text-align:center;'>Density Checker</h1>",unsafe_allow_html=True)
st.markdown("----",unsafe_allow_html=True)
hide_style ="""
<style>
      #MainMenu {visibility:hidden}
      footer {visibility:hidden}
      header {visibility:hidden}


"""
st.markdown(hide_style,unsafe_allow_html=True)

text = st.text_area("Paragraph")
col1,col2,col3 = st.columns(3)
words_dict = {}
btn = st.button('Submit')
if btn:
    col1.markdown(f"<h2 style='text-align:center;'>{'Keywords'}</h2>",unsafe_allow_html=True)
    col2.markdown(f"<h2 style='text-align:center;'>{'Occurances'}</h2>",unsafe_allow_html=True)
    col3.markdown(f"<h2 style='text-align:center;'>{'Percentages'}</h2>",unsafe_allow_html=True)

    text_clean = (re.sub("[,/\.?|&*;:]",'',text)).lower()
    words = text_clean.split(" ")
    t_word = len(words)
    for w in words:
        if w in words_dict:
            words_dict[w] = words_dict[w]+1
        else:
            words_dict[w] =1 
    keys = list(words_dict.keys())
    values = list(words_dict.values())
    for i in range(len(keys)):
        col1.markdown(f"<h5 style='text-align:center;'>{keys[i]}</h5>",unsafe_allow_html=True)
        col2.markdown(f"<h5 style='text-align:center;'>{values[i]}</h5>",unsafe_allow_html=True)
        col3.markdown(f"<h5 style='text-align:center;'>{(values[i]/t_word)*100}</h5>",unsafe_allow_html=True)



