import streamlit as st
from prediction_helper import make_prediction

# App Title
st.header('Predict Your Health Insurance Premium')

# Define options for categorical fields
choices = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment': ['Salaried', 'Self-Employed', 'Freelancer', ''],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical Background': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Plan Type': ['Bronze', 'Silver', 'Gold']
}

# Layout: Four rows, three columns each
section1 = st.columns(3)
section2 = st.columns(3)
section3 = st.columns(3)
section4 = st.columns(3)

# Collect user inputs in the layout grid
with section1[0]:
    user_age = st.number_input('Enter Age', min_value=18, max_value=100, step=1)
with section1[1]:
    dependants = st.number_input('Dependants Count', min_value=0, max_value=20, step=1)
with section1[2]:
    annual_income = st.number_input('Annual Income (Lakhs)', min_value=0, max_value=200, step=1)

with section2[0]:
    genetic_factor = st.number_input('Genetic Risk Score', min_value=0, max_value=5, step=1)
with section2[1]:
    plan_choice = st.selectbox('Choose Plan', choices['Plan Type'])
with section2[2]:
    job_status = st.selectbox('Employment Type', choices['Employment'])

with section3[0]:
    user_gender = st.selectbox('Select Gender', choices['Gender'])
with section3[1]:
    marital = st.selectbox('Marital Status', choices['Marital Status'])
with section3[2]:
    bmi_group = st.selectbox('BMI Group', choices['BMI Category'])

with section4[0]:
    smoke_habit = st.selectbox('Smoking Habit', choices['Smoking Status'])
with section4[1]:
    geo_region = st.selectbox('Geographical Region', choices['Region'])
with section4[2]:
    med_history = st.selectbox('Medical Background', choices['Medical Background'])

# Compile all inputs for prediction
user_inputs = {
    'Age': user_age,
    'Number of Dependants': dependants,
    'Income in Lakhs': annual_income,
    'Genetical Risk': genetic_factor,
    'Insurance Plan': plan_choice,
    'Employment Status': job_status,
    'Gender': user_gender,
    'Marital Status': marital,
    'BMI Category': bmi_group,
    'Smoking Status': smoke_habit,
    'Region': geo_region,
    'Medical History': med_history
}

# Prediction trigger
if st.button('Estimate Premium'):
    estimated_cost = make_prediction(user_inputs)
    st.success(f'Estimated Health Insurance Premium: {estimated_cost}')
