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
    st.write("""### We need some information to predict the student dropout""")

    marital = (
        1, 2, 3, 4, 5, 6
    )
    scholarship_status = (0, 1)

    marital_status = st.selectbox('Marital Status', marital)
    gdp = st.text_input('GDP')
    age = st.text_input('Age when enroll')
    scholarship = st.selectbox('Are you a scholarship holder?', scholarship_status)
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

show_predict_page()

