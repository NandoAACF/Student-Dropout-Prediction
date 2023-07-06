import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('student_dropout_model.pickle', 'rb') as f:
        data = pickle.load(f)
    return data

data = load_model()

def show_predict_page():
    st.title('Student Dropout Prediction')

    marital_status = st.selectbox('Marital Status', ('Single', 'Married', 'Widower', 'Divorced', 'Facto Union', 'Legally Separated'))
    if marital_status == 'Single':
        marital_status = 1
    elif marital_status == 'Married':
        marital_status = 2
    elif marital_status == 'Widower':
        marital_status = 3
    elif marital_status == 'Divorced':
        marital_status = 4
    elif marital_status == 'Facto Union':
        marital_status = 5
    elif marital_status == 'Legally Separated':
        marital_status = 6

    gdp = st.text_input('GDP')

    age = st.select_slider('Age', options=[i for i in range(1, 100)])

    scholarship = st.selectbox('Are you a scholarship holder?', ('No', 'Yes'))
    if scholarship == 'No':
        scholarship = 0
    elif scholarship == 'Yes':
        scholarship = 1

    credit1 = st.text_input('Number of curricular units credited in the 1st semester')
    enrolled1 = st.text_input('Number of curricular units enrolled in the 1st semester')
    eval1 = st.text_input('Number of evaluations to curricular units in the 1st semester')
    noteval1 = st.text_input('Number of curricular units without evalutions in the 1st semester')
    approved1 = st.text_input('Number of curricular units approved in the 1st semester')
    grade1 = st.text_input('Grade average in the 1st semester')
    credit2 = st.text_input('Number of curricular units credited in the 2nd semester')
    enrolled2 = st.text_input('Number of curricular units enrolled in the 2nd semester')
    eval2 = st.text_input('Number of evaluations to curricular units in the 2nd semester')
    noteval2 = st.text_input('Number of curricular units without evalutions in the 2nd semester')
    approved2 = st.text_input('Number of curricular units approved in the 2nd semester')
    grade2 = st.text_input('Grade average in the 2nd semester')

    ok = st.button("Predict")
    if ok: 
        X = np.array([[marital_status, gdp, credit1, age, scholarship, enrolled1, eval1, approved1, grade1, noteval1, credit2, enrolled2, eval2, approved2, grade2, noteval2]])
        pred = data.predict(X)
        if pred == 0:
            st.subheader(f'The student will dropout')
        if pred == 1:
            st.subheader(f'The student will graduate')

