import streamlit as st
from predict_page import show_predict_page
from insight_page import show_insight_page

page = st.sidebar.selectbox("Predict Or Insight", ("Predict", "Insight"))

if page == 'Predict':
    show_predict_page()
else:
    show_insight_page()
