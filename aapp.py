import streamlit as st
import pandas as pd

df = pd.read_csv("salary_data.csv")

st.title("💰 Salary Prediction App")

job_title = st.selectbox("Job Title", df["Job Title"].unique())
location = st.selectbox("Location", df["Location"].unique())
skills = st.selectbox("Skills", df["Skills"].unique())
experience = st.slider("Years of Experience", 0, 20, 2)

st.write("### Input Summary")
st.write(f"**Job:** {job_title} | **Experience:** {experience} years | **Location:** {location} | **Skills:** {skills}")

if st.button("Predict Salary"):
    # Base salary suggestion
    base_salary = 500000

    # Add 80k for each year of experience
    salary = base_salary + (experience * 80000)

    # Format nicely with commas
    salary_formatted = f"₹{salary:,.0f}"

    st.success(f"Estimated Salary: {salary_formatted}")
