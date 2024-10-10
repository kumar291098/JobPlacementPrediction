import numpy as np
from PIL import Image
import streamlit as st
import pickle

# Load model using pickle
with open('placement.pkl', 'rb') as model_file:
    lg = pickle.load(model_file)

# Web app
img = Image.open('placementImg.jpg')
st.image(img, width=650)
st.title("Placement Prediction")

# Sidebar explanation
st.sidebar.markdown("""
**Input Features:**
- **SSC:** Certificate for completing 10th grade (secondary education).
- **HSC:** Certificate for completing 12th grade (higher secondary education).
- **Degree Percentage:** Percentage obtained in the undergraduate degree.
- **Emp Test Percentage:** Percentage obtained in the employment test.
- **MBA Percent:** Percentage obtained in the MBA program.
- **Gender:** Male or Female.
- **SSC Board (Others):** Whether the SSC board is categorized as Others.
- **HSC Board (Others):** Whether the HSC board is categorized as Others.
- **HSC Subject (Commerce):** Whether the student took Commerce in HSC.
- **HSC Subject (Science):** Whether the student took Science in HSC.
- **Undergraduate Degree (Others):** Whether the undergraduate degree is categorized as Others.
- **Undergraduate Degree (Sci&Tech):** Whether the undergraduate degree is in Science and Technology.
- **Work Experience:** Whether the student has any work experience.
- **Specialisation (Mkt&HR):** Whether the specialisation is in Marketing and Human Resources.
""")

# User input fields
ssc_percentage = st.number_input("Enter SSC Percentage", min_value=0.0, max_value=100.0)
hsc_percentage = st.number_input("Enter HSC Percentage", min_value=0.0, max_value=100.0)
degree_percentage = st.number_input("Enter Degree Percentage", min_value=0.0, max_value=100.0)
emp_test_percentage = st.number_input("Enter Employment Test Percentage", min_value=0.0, max_value=100.0)
mba_percent = st.number_input("Enter MBA Percentage", min_value=0.0, max_value=100.0)

gender = st.selectbox("Select Gender", ("Male", "Female"))
gender_M = 1 if gender == "Male" else 0

ssc_board = st.selectbox("Select SSC Board", ("Others", "State Board", "CBSE", "ICSE"))
ssc_board_Others = 1 if ssc_board == "Others" else 0

hsc_board = st.selectbox("Select HSC Board", ("Others", "State Board", "CBSE", "ICSE"))
hsc_board_Others = 1 if hsc_board == "Others" else 0

hsc_subject = st.selectbox("Select HSC Subject", ("Commerce", "Science"))
hsc_subject_Commerce = 1 if hsc_subject == "Commerce" else 0
hsc_subject_Science = 1 if hsc_subject == "Science" else 0

undergrad_degree = st.selectbox("Select Undergrad Degree", ("Others", "Science & Technology", "Arts"))
undergrad_degree_Others = 1 if undergrad_degree == "Others" else 0
undergrad_degree_Sci_Tech = 1 if undergrad_degree == "Science & Technology" else 0

work_experience = st.selectbox("Work Experience", ("Yes", "No"))
work_experience_Yes = 1 if work_experience == "Yes" else 0

specialisation = st.selectbox("Select Specialisation", ("Mkt & HR", "Finance", "Operations"))
specialisation_Mkt_HR = 1 if specialisation == "Mkt & HR" else 0

# Prepare input data for prediction
input_data = np.array([
    ssc_percentage,
    hsc_percentage,
    degree_percentage,
    emp_test_percentage,
    mba_percent,
    gender_M,
    ssc_board_Others,
    hsc_board_Others,
    hsc_subject_Commerce,
    hsc_subject_Science,
    undergrad_degree_Others,
    undergrad_degree_Sci_Tech,
    work_experience_Yes,
    specialisation_Mkt_HR
]).reshape(1, -1)

# Apply Prediction Button
if st.button("Predict Placement"):
    prediction = lg.predict(input_data)
    if prediction[0] == 1:
        st.write("This student is placed.")
    else:
        st.write("This student is not placed.")
