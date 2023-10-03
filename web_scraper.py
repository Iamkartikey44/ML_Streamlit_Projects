import streamlit as st 
import requests
import webbrowser
from bs4 import BeautifulSoup

st.set_page_config(page_title="Web Scraper",page_icon=":globe_with_meridians:")


st.markdown("<h1 style='text-align:center;'>Web Scraper </h1>",unsafe_allow_html=True)

with st.form('Search'):
    keyword = st.text_input("Enter your Image Name")
    search = st.form_submit_button("Search")
placeholder = st.empty()
if keyword:
    page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
    soup = BeautifulSoup(page.content,'lxml')
    rows = soup.find_all("div",class_="ripi6")
    col1,col2 = placeholder.columns(2)
    for idx,row in enumerate(rows):
        figure = row.find_all('figure')
        for i in range(2):
            img = figure[i].find("img",class_="tB6UZ a5VGX")
            list = img["srcset"].split("?")
            anchors = figure[i].find('a',class_='rEAWd')
            if (i==0):
                col1.image(list[0])
                btn = col1.button("Download",key=str(idx)+str(i))

                if btn:
                    webbrowser.open_new_tab("https://unsplash.com"+anchors["href"])
            
            else:
                col2.image(list[0])
                btn = col2.button("Download",key = str(idx)+str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com"+anchors["href"])    
