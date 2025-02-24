import streamlit as st
import pandas as pd

# Title and Introduction
st.markdown("# Introduction\n\n---\n\nThis project analyzes data from a cross-sectional study of 549 participants exploring the relationship between company size, job roles, and well-being in the workplace. Specifically, it examines whether individuals working in larger companies experience higher stress levels and different levels of life satisfaction compared to those in smaller companies. The study also investigates how stress and life satisfaction vary between employees and managers. Additionally, it explores the connection between company size and regular exercise habits, as well as whether adult exercise patterns are linked to childhood exercise habits.")

# Data Source
st.markdown("## Data Source\n\n---\n\n**Study**: Work, Stress, and Life Satisfaction.\n\n**Institution**: Szechenyi Istvan Egyetem (Hungary).\n\n**Published**: 8 August 2024.\n\n**Categories**: Psychology, Adult, Workplace, Job Stress, Life Satisfaction, Exercise Psychology.\n\nDOI: 10.17632/hsgymx6zf8.2")

# Steps to reproduce
st.markdown("## Steps to reproduce:\n\n---\n\nUse the SWL and PSS (Satisfaction with Life - 5 items and Perceived Stress Scale - 14 items) and ask about childhood and current exercise habits, and workplace employee numbers in 4 categories (up to 10, 11-100, 101-1,000, and over 1,000). If needed, you can combine these into large (> 100) and small (< 100) companies. Collect demographic information such as age, gender, education level (basic/elementary, high school, university), perceived health on a 7-point scale, and perceived income on a 7-point scale. Ask for employment status in two categorical terms: employee or manager. Run chi-square and t-tests for group comparisons. Correlations/regression are feasible if the research question warrants it.")

# Upload dataset 
df = pd.read_excel("Cleaned_Work_life.xlsx")

# Display the cleaned dataset
st.write("Cleaned Dataset (rows with nulls removed):", df.head())