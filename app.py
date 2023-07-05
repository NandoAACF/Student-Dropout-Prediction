import streamlit as st
from predict_page import show_predict_page
from insight_page import show_insight_page
from model_information_page import show_model_information_page

page = st.sidebar.selectbox("Predict Or Insight", ("Predict", "Insight", "Model Information"))

if page == 'Predict':
    show_predict_page()
elif page == 'Insight':
    show_insight_page()
elif page == 'Model Information':
    show_model_information_page()