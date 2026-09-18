import streamlit as st
import pandas as pd
import joblib

model = joblib.load('student_exam_score_model.pkl')
scaler = joblib.load('student_exam_score_scaler.pkl')

numerical_features = [
    'age',
    'study_hours_per_day',
    'social_media_hours',
    'netflix_hours',
    'attendance_percentage',
    'sleep_hours',
    'exercise_frequency',
    'mental_health_rating'
]

st.title("🎓 Student Exam Score Prediction")


st.subheader("Student Information")

age = st.number_input(
    "Age",
    min_value=10,
    max_value=100,
    value=20
)


study_hours = st.number_input(
    "Study Hours per Day",
    min_value=0.0,
    max_value=24.0,
    value=2.0
)



social_media_hours = st.number_input(
    "Social Media Hours per Day",
    min_value=0.0,
    max_value=24.0,
    value=2.0
)


netflix_hours = st.number_input(
    "Netflix Hours per Day",
    min_value=0.0,
    max_value=24.0,
    value=1.0
)


attendance_percentage = st.number_input(
    "Attendance Percentage",
    min_value=0.0,
    max_value=100.0,
    value=80.0
)


sleep_hours = st.number_input(
    "Sleep Hours per Day",
    min_value=0.0,
    max_value=24.0,
    value=7.0
)


exercise_frequency = st.number_input(
    "Exercise Frequency",
    min_value=0,
    max_value=7,
    value=3
)


mental_health_rating = st.number_input(
    "Mental Health Rating",
    min_value=1,
    max_value=10,
    value=5
)



gender = st.selectbox(
    "Gender",
    ["Female", "Male", "Other"]
)


part_time_job = st.selectbox(
    "Part-Time Job",
    ["No", "Yes"]
)


diet_quality = st.selectbox(
    "Diet Quality",
    ["Average", "Good", "Poor"]
)


parental_education_level = st.selectbox(
    "Parental Education Level",
    ["Bachelor", "High School", "Master", "Unknown"]
)


internet_quality = st.selectbox(
    "Internet Quality",
    ["Average", "Good", "Poor"]
)


extracurricular_participation = st.selectbox(
    "Extracurricular Participation",
    ["No", "Yes"]
)


input_data = pd.DataFrame({
    'age': [age],
    'study_hours_per_day': [study_hours],
    'social_media_hours': [social_media_hours],
    'netflix_hours': [netflix_hours],
    'attendance_percentage': [attendance_percentage],
    'sleep_hours': [sleep_hours],
    'exercise_frequency': [exercise_frequency],
    'mental_health_rating': [mental_health_rating],

    'gender_Male': [1 if gender == 'Male' else 0],
    'gender_Other': [1 if gender == 'Other' else 0],

    'part_time_job_Yes': [1 if part_time_job == 'Yes' else 0],

    'diet_quality_Good': [1 if diet_quality == 'Good' else 0],
    'diet_quality_Poor': [1 if diet_quality == 'Poor' else 0],

    'parental_education_level_High School': [
        1 if parental_education_level == 'High School' else 0
    ],
    'parental_education_level_Master': [
        1 if parental_education_level == 'Master' else 0
    ],
    'parental_education_level_UnKnown': [
        1 if parental_education_level == 'Unknown' else 0
    ],

    'internet_quality_Good': [
        1 if internet_quality == 'Good' else 0
    ],
    'internet_quality_Poor': [
        1 if internet_quality == 'Poor' else 0
    ],

    'extracurricular_participation_Yes': [
        1 if extracurricular_participation == 'Yes' else 0
    ]
})

if st.button("Predict Exam Score"):

    scaled_input = input_data.copy()

    scaled_input[numerical_features] = scaler.transform(
        input_data[numerical_features]
    )

    prediction = model.predict(scaled_input)[0]

    st.success(f"Predicted Exam Score: {prediction:.2f}")