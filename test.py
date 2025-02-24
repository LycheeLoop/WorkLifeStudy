import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, pearsonr, f_oneway, chi2_contingency

# Title and Introduction
st.markdown("# Work, Stress and Life Satisfaction Study\n\n---\n\nThis project analyzes data from a cross-sectional study of 549 participants exploring the relationship between company size, job roles, and well-being in the workplace. Specifically, it examines whether individuals working in larger companies experience higher stress levels and different levels of life satisfaction compared to those in smaller companies. The study also investigates how stress and life satisfaction vary between employees and managers. Additionally, it explores the connection between company size and regular exercise habits, as well as whether adult exercise patterns are linked to childhood exercise habits.")

# Data Source
st.markdown("### Data Source\n\n---\n\n**Study**: Work, Stress, and Life Satisfaction.\n\n**Institution**: Szechenyi Istvan Egyetem (Hungary).\n\n**Published**: 8 August 2024.\n\n**Categories**: Psychology, Adult, Workplace, Job Stress, Life Satisfaction, Exercise Psychology.\n\nDOI: 10.17632/hsgymx6zf8.2\n\n---\n\n")

# Upload dataset 
df = pd.read_excel("Cleaned_Work_life.xlsx")

st.markdown("#### Each participant provided responses to the following variables:")
st.text(f"Columns: {', '.join(df.columns)}")

# Display the cleaned dataset
st.markdown("**Cleaned Dataset Preview**:")
st.write(df.head())
st.markdown("\n\n---\n\n")

# Create a sidebar for navigation
st.sidebar.header("Navigation")
section = st.sidebar.selectbox("Choose Analysis Section", [
    "Company Size & Well-Being",
    "Stress & Income",
    "Life Satisfaction & Stress",
    "Employment Type Analysis",
    "Perceived Health & Stress",
    "Exercise Habits & Stress",
    "Exercise Habits & Life Satisfaction",
    "Current Exercise Habits vs Childhood Sports History"
])

# ------------------ Company Size & Well-Being Analysis -------------------- #
if section == "Company Size & Well-Being":
    st.markdown("### (A) Company Size & Well-Being (Stress & Life Satisfaction)")
    # Sidebar for user selection
    st.sidebar.header("T-Test & Visualization")
    selected_variable = st.sidebar.radio("Select Variable for T-Test", ["Stress", "LifeSatisf"])

    # Separate groups
    small_companies = df[df['CompanySize'] == 1][selected_variable]
    large_companies = df[df['CompanySize'] == 2][selected_variable]

    # Perform independent t-test
    t_stat, p_value = ttest_ind(small_companies, large_companies, equal_var=False)

    # Display results in Streamlit
    st.header("T-Test Results")
    st.write(f"**Variable:** {selected_variable}")
    st.write(f"**T-statistic:** {t_stat:.3f}")
    st.write(f"**P-value:** {p_value:.5f}")

    # Interpretation
    if p_value < 0.05:
        st.success("There is a statistically significant difference between small and large companies.")
    else:
        st.info("There is no significant difference between small and large companies.")

    # Visualization: Boxplot
    st.header("Boxplot Comparison")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(x=df["CompanySize"], y=df[selected_variable], ax=ax)
    ax.set_xticklabels(["Small Companies", "Large Companies"])
    ax.set_xlabel("Company Size")
    ax.set_ylabel(selected_variable)
    st.pyplot(fig)

    # Visualization: Histogram
    st.header("Histogram of Distribution")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(small_companies, color="blue", label="Small Companies", kde=True, alpha=0.6)
    sns.histplot(large_companies, color="red", label="Large Companies", kde=True, alpha=0.6)
    ax.set_xlabel(selected_variable)
    ax.legend()
    st.pyplot(fig)

# ------------------ Stress & Income Analysis -------------------- #
elif section == "Stress & Income":
    st.markdown("### (B) Stress & Income Analysis")
    corr_coeff, p_value = pearsonr(df["Stress"], df["income1to7"])
    st.header("Correlation Between Stress and Income")
    st.write(f"**Pearson's Correlation Coefficient:** {corr_coeff:.3f}")
    st.write(f"**P-value:** {p_value:.5f}")
    if p_value < 0.05:
        st.success("There is a statistically significant correlation between stress and income.")
    else:
        st.info("There is no significant correlation between stress and income.")
    st.header("Scatterplot: Stress vs. Income")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.regplot(x=df["income1to7"], y=df["Stress"], ax=ax, scatter_kws={'alpha':0.6}, line_kws={'color':'red'})
    ax.set_xlabel("Income Level (1 = Low, 7 = High)")
    ax.set_ylabel("Stress Level")
    ax.set_title("Relationship Between Stress and Income")
    st.pyplot(fig)

# ------------------ Life Satisfaction & Stress -------------------- #
elif section == "Life Satisfaction & Stress":
    st.markdown("### Life Satisfaction & Stress")
    corr_coeff, p_value = pearsonr(df["Stress"], df["LifeSatisf"])
    st.header("Correlation Between Stress and Life Satisfaction")
    st.write(f"**Pearson's Correlation Coefficient:** {corr_coeff:.3f}")
    st.write(f"**P-value:** {p_value:.5f}")
    if p_value < 0.05:
        st.success("There is a statistically significant correlation between stress and life satisfaction.")
    else:
        st.info("There is no significant correlation between stress and life satisfaction.")
    st.header("Scatterplot: Stress vs. Life Satisfaction")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.regplot(x=df["Stress"], y=df["LifeSatisf"], ax=ax, scatter_kws={'alpha':0.6}, line_kws={'color':'red'})
    ax.set_xlabel("Stress Level")
    ax.set_ylabel("Life Satisfaction Level")
    ax.set_title("Relationship Between Stress and Life Satisfaction")
    st.pyplot(fig)

# ------------------ Employment Type Analysis -------------------- #
elif section == "Employment Type Analysis":
    st.markdown("### (C) Employment Type Analysis - Stress Levels")
    employees = df[df["JobPositionEmployeeManager"] == 1]["Stress"]
    managers = df[df["JobPositionEmployeeManager"] == 2]["Stress"]
    t_stat, p_value = ttest_ind(employees, managers, equal_var=False)
    st.header("Stress Levels Between Employees and Managers")
    st.write(f"**T-test Statistic:** {t_stat:.3f}")
    st.write(f"**P-value:** {p_value:.5f}")
    if p_value < 0.05:
        st.success("There is a statistically significant difference in stress levels between employees and managers.")
    else:
        st.info("There is no significant difference in stress levels between employees and managers.")
    st.header("Boxplot: Stress Levels of Employees vs. Managers")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(x=df["JobPositionEmployeeManager"], y=df["Stress"], ax=ax, palette=["blue", "orange"])
    ax.set_xticklabels(["Employee", "Manager"])
    ax.set_xlabel("Job Position")
    ax.set_ylabel("Stress Level")
    ax.set_title("Comparison of Stress Levels Between Employees and Managers")
    st.pyplot(fig)

# ------------------ Perceived Health vs. Stress levels -------------------- #
elif section == "Perceived Health & Stress":
    st.markdown("### (D) Perceived Health - Stress Levels")
    correlation, p_value = pearsonr(df["Stress"], df["perceivedhealth1to7"])
    st.header("Relationship Between Stress and Perceived Health")
    st.write(f"**Pearson Correlation Coefficient:** {correlation:.3f}")
    st.write(f"**P-value:** {p_value:.5f}")
    if p_value < 0.05:
        st.success("There is a statistically significant relationship between stress levels and perceived health.")
    else:
        st.info("There is no significant correlation between stress levels and perceived health.")
    st.header("Scatterplot: Stress vs. Perceived Health")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.scatterplot(x=df["perceivedhealth1to7"], y=df["Stress"], ax=ax, alpha=0.6, color="purple")
    ax.set_xlabel("Perceived Health (1 = Least Healthy, 7 = Most Healthy)")
    ax.set_ylabel("Stress Score")
    ax.set_title("Scatterplot of Stress vs. Perceived Health")
    st.pyplot(fig)

# ------------------ Exercise Habits vs. Stress levels -------------------- #
elif section == "Exercise Habits & Stress":
    st.markdown("### (E) Exercise Habits - Stress Levels")
    st.header("Stress Across Exercise Habits")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(x=df["LeisureCompOrNoSport"], y=df["Stress"], ax=ax, palette="muted")
    ax.set_xlabel("Exercise Habits (1=Leisure, 2=Regular)")
    ax.set_ylabel("Stress")
    ax.set_title("Stress Levels in Different Exercise Habit Groups")
    st.pyplot(fig)

# ------------------ Exercise Habits & Life Satisfaction -------------------- #
elif section == "Exercise Habits & Life Satisfaction":
    st.markdown("### (F) Exercise Habits - Life Satisfaction")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(x=df["LeisureCompOrNoSport"], y=df["LifeSatisf"], ax=ax, palette="muted")
    ax.set_xlabel("Exercise Habits (1=Leisure, 2=Regular)")
    ax.set_ylabel("Life Satisfaction")
    ax.set_title("Life Satisfaction Across Exercise Habit Groups")
    st.pyplot(fig)

# ------------------ Childhood Sports vs Current Exercise -------------------- #
elif section == "Current Exercise Habits vs Childhood Sports History":
    st.markdown("### (G) Childhood Sports vs. Current Exercise Habits")
    contingency_table = pd.crosstab(df["LeisureCompOrNoSport"], df["ExerciseChildhood"])
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    st.header("Chi-Square Test: Childhood Exercise vs. Current Habits")
    st.write(f"**Chi-Square Statistic:** {chi2:.3f}")
    st.write(f"**P-value:** {p:.5f}")
    if p < 0.05:
        st.success("There is a statistically significant relationship between childhood exercise and current exercise habits.")
    else:
        st.info("There is no significant relationship between childhood exercise and current exercise habits.")

    # Visualization
    st.header("Heatmap of Childhood Sports vs. Current Exercise Habits")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.heatmap(contingency_table, annot=True, cmap="coolwarm", fmt="d", ax=ax)
    st.pyplot(fig)

