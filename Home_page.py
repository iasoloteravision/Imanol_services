import streamlit as st

st.set_page_config(
    page_title="Code Codix products",
    page_icon="👋",
)

st.success("# Welcome to Code Codix services page! ")

col1, col2, col3 = st.columns(3)

text1 = "Build, develop and deploy software products"
text2 = "Software consultory"
text3 = "Business solutions based in software development and startup coaching"

col1.success (text1)
col2.warning (text2)
col3.info (text3)

