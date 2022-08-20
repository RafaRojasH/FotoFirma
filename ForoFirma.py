import streamlit as st
import urllib
import base64
import fitz

def read_pdf_with_fitz(file):
 	with fitz.open(file) as doc:
 		text = ""
 		for page in doc:
 			text += page.getText()
 		return text 

uploaded_file = st.file_uploader("Choose a file", type=['pdf'], accept_multiple_files=True)

if uploaded_file is not None:
    st.subheader('llll')
    read_pdf_with_fitz(uploaded_file)
