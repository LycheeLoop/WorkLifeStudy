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



# ------------ Create a sidebar for navigation ----------------#
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

# ------------------ Company Size Analysis -------------------- #
if section == "Company Size & Well-Being":
    # Analyze company size and well-being with t-test 
    st.markdown("### (A) Company Size & Well-Being (Stress & Life Satisfaction)")

    # Separate groups for stress and life satisfaction
    stress_small_companies = df[df['CompanySize'] == 1]['Stress']
    stress_large_companies = df[df['CompanySize'] == 2]['Stress']

    life_satisf_small_companies = df[df['CompanySize'] == 1]['LifeSatisf']
    life_satisf_large_companies = df[df['CompanySize'] == 2]['LifeSatisf']

    # Perform independent t-test for Stress
    t_stat_stress, p_value_stress = ttest_ind(stress_small_companies, stress_large_companies, equal_var=False)
    # Perform independent t-test for Life Satisfaction
    t_stat_life_satisf, p_value_life_satisf = ttest_ind(life_satisf_small_companies, life_satisf_large_companies, equal_var=False)

    # Display results for Stress and Life Satisfaction in Streamlit
    st.header("T-Test Results")

    # Stress results
    st.write("### Stress")
    st.write(f"**T-statistic (Stress):** {t_stat_stress:.3f}")
    st.write(f"**P-value (Stress):** {p_value_stress:.5f}")
    if p_value_stress < 0.05:
        st.success("There is a statistically significant difference between small and large companies in stress.")
    else:
        st.info("There is no significant difference in stress between small and large companies.")

    # Life Satisfaction results
    st.write("### Life Satisfaction")
    st.write(f"**T-statistic (Life Satisfaction):** {t_stat_life_satisf:.3f}")
    st.write(f"**P-value (Life Satisfaction):** {p_value_life_satisf:.5f}")
    if p_value_life_satisf < 0.05:
        st.success("There is a statistically significant difference between small and large companies in life satisfaction.")
    else:
        st.info("There is no significant difference in life satisfaction between small and large companies.")

    # Visualization: Boxplot for Stress
    st.header("Boxplot Comparison (Stress)")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(x=df["CompanySize"], y=df["Stress"], ax=ax)
    ax.set_xticklabels(["Small Companies", "Large Companies"])
    ax.set_xlabel("Company Size")
    ax.set_ylabel("Stress Level")
    st.pyplot(fig)

    # Visualization: Boxplot for Life Satisfaction
    st.header("Boxplot Comparison (Life Satisfaction)")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(x=df["CompanySize"], y=df["LifeSatisf"], ax=ax)
    ax.set_xticklabels(["Small Companies", "Large Companies"])
    ax.set_xlabel("Company Size")
    ax.set_ylabel("Life Satisfaction")
    st.pyplot(fig)

    # Visualization: Histogram for Stress
    st.header("Histogram of Stress Distribution")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(stress_small_companies, color="blue", label="Small Companies", kde=True, alpha=0.6)
    sns.histplot(stress_large_companies, color="red", label="Large Companies", kde=True, alpha=0.6)
    ax.set_xlabel("Stress Level")
    ax.legend()
    st.pyplot(fig)

    # Visualization: Histogram for Life Satisfaction
    st.header("Histogram of Life Satisfaction Distribution")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(life_satisf_small_companies, color="blue", label="Small Companies", kde=True, alpha=0.6)
    sns.histplot(life_satisf_large_companies, color="red", label="Large Companies", kde=True, alpha=0.6)
    ax.set_xlabel("Life Satisfaction Level")
    ax.legend()
    st.pyplot(fig)


# ------------------ Income Analysis -------------------- #
elif section == "Stress & Income":
    st.markdown("### (B) Stress & Income Analysis")

    # Compute correlation
    corr_coeff, p_value = pearsonr(df["Stress"], df["income1to7"])

    # Display correlation results
    st.header("Correlation Between Stress and Income")
    st.write(f"**Pearson's Correlation Coefficient:** {corr_coeff:.3f}")
    st.write(f"**P-value:** {p_value:.5f}")

    # Interpretation
    if p_value < 0.05:
        st.success("There is a statistically significant correlation between stress and income.")
    else:
        st.info("There is no significant correlation between stress and income.")

    # Scatterplot Visualization
    st.header("Scatterplot: Stress vs. Income")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.regplot(x=df["income1to7"], y=df["Stress"], ax=ax, scatter_kws={'alpha':0.6}, line_kws={'color':'red'})
    ax.set_xlabel("Income Level (1 = Low, 7 = High)")
    ax.set_ylabel("Stress Level")
    ax.set_title("Relationship Between Stress and Income")
    st.pyplot(fig)

    # Life satisfaction vs income

    # Compute correlation
    corr_coeff, p_value = pearsonr(df["LifeSatisf"], df["income1to7"])

    # Display correlation results
    st.header("Correlation Between Life Satisfaction and Income")
    st.write(f"**Pearson's Correlation Coefficient:** {corr_coeff:.3f}")
    st.write(f"**P-value:** {p_value:.5f}")

    # Interpretation
    if p_value < 0.05:
        st.success("There is a statistically significant correlation between life satisfaction and income.")
    else:
        st.info("There is no significant correlation between life satisfaction and income.")

    # Scatterplot Visualization
    st.header("Scatterplot: Life Satisfaction vs. Income")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.regplot(x=df["income1to7"], y=df["LifeSatisf"], ax=ax, scatter_kws={'alpha':0.6}, line_kws={'color':'red'})
    ax.set_xlabel("Income Level (1 = Low, 7 = High)")
    ax.set_ylabel("Life Satisfaction Level")
    ax.set_title("Relationship Between Life Satisfaction and Income")
    st.pyplot(fig)


# ------------------ Life Satisfaction & Stress -------------------- #
elif section == "Life Satisfaction & Stress":

    st.markdown("### Life Satisfaction & Stress")
    # Compute correlation
    corr_coeff, p_value = pearsonr(df["Stress"], df["LifeSatisf"])

    # Display correlation results
    st.header("Correlation Between Stress and Life Satisfaction")
    st.write(f"**Pearson's Correlation Coefficient:** {corr_coeff:.3f}")
    st.write(f"**P-value:** {p_value:.5f}")

    # Interpretation
    if p_value < 0.05:
        st.success("There is a statistically significant correlation between stress and life satisfaction.")
    else:
        st.info("There is no significant correlation between stress and life satisfaction.")

    # Scatterplot Visualization
    st.header("Scatterplot: Stress vs. Life Satisfaction")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.regplot(x=df["Stress"], y=df["LifeSatisf"], ax=ax, scatter_kws={'alpha':0.6}, line_kws={'color':'red'})
    ax.set_xlabel("Stress Level")
    ax.set_ylabel("Life Satisfaction Level")
    ax.set_title("Relationship Between Stress and Life Satisfaction")
    st.pyplot(fig)

# ------------------ Employment Type Analysis -------------------- #
elif section == "Employment Type Analysis":
    # Employment type vs Stress
    st.markdown("### (C) Employment Type Analysis - Stress Levels")

    # Split into two groups
    employees = df[df["JobPositionEmployeeManager"] == 1]["Stress"]
    managers = df[df["JobPositionEmployeeManager"] == 2]["Stress"]

    # Perform t-test
    t_stat, p_value = ttest_ind(employees, managers, equal_var=False)

    # Display t-test results
    st.header("Stress Levels Between Employees and Managers")
    st.write(f"**T-test Statistic:** {t_stat:.3f}")
    st.write(f"**P-value:** {p_value:.5f}")

    # Interpretation
    if p_value < 0.05:
        st.success("There is a statistically significant difference in stress levels between employees and managers.")
    else:
        st.info("There is no significant difference in stress levels between employees and managers.")

    # Boxplot Visualization
    st.header("Boxplot: Stress Levels of Employees vs. Managers")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(x=df["JobPositionEmployeeManager"], y=df["Stress"], ax=ax, palette=["blue", "orange"])
    ax.set_xticklabels(["Employee", "Manager"])
    ax.set_xlabel("Job Position")
    ax.set_ylabel("Stress Level")
    ax.set_title("Comparison of Stress Levels Between Employees and Managers")
    st.pyplot(fig)

    # Employment type vs Life Satisfaction

    st.markdown("### Employment Type Analysis - Life Satisfaction")

    # Split into two groups
    employees_ls = df[df["JobPositionEmployeeManager"] == 1]["LifeSatisf"]
    managers_ls = df[df["JobPositionEmployeeManager"] == 2]["LifeSatisf"]

    # Perform t-test
    t_stat_ls, p_value_ls = ttest_ind(employees_ls, managers_ls, equal_var=False)

    # Display t-test results
    st.header("Life Satisfaction Between Employees and Managers")
    st.write(f"**T-test Statistic:** {t_stat_ls:.3f}")
    st.write(f"**P-value:** {p_value_ls:.5f}")

    # Interpretation
    if p_value_ls < 0.05:
        st.success("There is a statistically significant difference in life satisfaction between employees and managers.")
    else:
        st.info("There is no significant difference in life satisfaction between employees and managers.")

    # Boxplot Visualization
    st.header("Boxplot: Life Satisfaction of Employees vs. Managers")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(x=df["JobPositionEmployeeManager"], y=df["LifeSatisf"], ax=ax, palette=["blue", "orange"])
    ax.set_xticklabels(["Employee", "Manager"])
    ax.set_xlabel("Job Position")
    ax.set_ylabel("Life Satisfaction Score")
    ax.set_title("Comparison of Life Satisfaction Between Employees and Managers")
    st.pyplot(fig)



# ------------------ Perceived Health vs. Stress levels -------------------- #
elif section == "Perceived Health & Stress":
    # Perceived Health vs Stress
    st.markdown("### (D) Perceived Health - Stress Levels")



    # Calculate Pearson correlation
    correlation, p_value = pearsonr(df["Stress"], df["perceivedhealth1to7"])

    # Display correlation result
    st.header("Relationship Between Stress and Perceived Health")
    st.write(f"**Pearson Correlation Coefficient:** {correlation:.3f}")
    st.write(f"**P-value:** {p_value:.5f}")

    # Interpretation
    if p_value < 0.05:
        st.success("There is a statistically significant relationship between stress levels and perceived health.")
    else:
        st.info("There is no significant correlation between stress levels and perceived health.")

    # Scatterplot Visualization
    st.header("Scatterplot: Stress vs. Perceived Health")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.scatterplot(x=df["perceivedhealth1to7"], y=df["Stress"], ax=ax, alpha=0.6, color="purple")
    ax.set_xlabel("Perceived Health (1 = Least Healthy, 7 = Most Healthy)")
    ax.set_ylabel("Stress Score")
    ax.set_title("Scatterplot of Stress vs. Perceived Health")
    st.pyplot(fig)

    # Boxplot Visualization
    st.header("Boxplot: Stress Across Perceived Health Levels")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(x=df["perceivedhealth1to7"], y=df["Stress"], ax=ax, palette="coolwarm")
    ax.set_xlabel("Perceived Health (1 = Least Healthy, 7 = Most Healthy)")
    ax.set_ylabel("Stress Score")
    ax.set_title("Comparison of Stress Across Different Perceived Health Levels")
    st.pyplot(fig)



    # Perceived Health Vs. Life Satisfaction

    # Calculate Pearson correlation
    correlation_health_ls, p_value_health_ls = pearsonr(df["LifeSatisf"], df["perceivedhealth1to7"])

    # Display correlation result
    st.header("Relationship Between Life Satisfaction and Perceived Health")
    st.write(f"**Pearson Correlation Coefficient:** {correlation_health_ls:.3f}")
    st.write(f"**P-value:** {p_value_health_ls:.5f}")

    # Interpretation
    if p_value_health_ls < 0.05:
        st.success("There is a statistically significant relationship between life satisfaction and perceived health.")
    else:
        st.info("There is no significant correlation between life satisfaction and perceived health.")

    # Scatterplot Visualization
    st.header("Scatterplot: Life Satisfaction vs. Perceived Health")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.scatterplot(x=df["perceivedhealth1to7"], y=df["LifeSatisf"], ax=ax, alpha=0.6, color="teal")
    ax.set_xlabel("Perceived Health (1 = Least Healthy, 7 = Most Healthy)")
    ax.set_ylabel("Life Satisfaction Score")
    ax.set_title("Scatterplot of Life Satisfaction vs. Perceived Health")
    st.pyplot(fig)

    # Boxplot Visualization
    st.header("Boxplot: Life Satisfaction Across Perceived Health Levels")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(x=df["perceivedhealth1to7"], y=df["LifeSatisf"], ax=ax, palette="viridis")
    ax.set_xlabel("Perceived Health (1 = Least Healthy, 7 = Most Healthy)")
    ax.set_ylabel("Life Satisfaction Score")
    ax.set_title("Comparison of Life Satisfaction Across Different Perceived Health Levels")
    st.pyplot(fig)

# ------------------ Exercise Habits vs. Stress levels -------------------- #
elif section == "Exercise Habits & Stress":
    # Exercise Habits vs Stress
    st.markdown("### (E) Exercise Habits - Stress Levels")

    # Boxplot/Violin plot
    st.header("Stress Across Exercise Habits")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(x=df["LeisureCompOrNoSport"], y=df["Stress"], ax=ax, palette="muted")
    ax.set_xlabel("Exercise Habits (1=Leisure, 2=Competitive, 3=No Sport)")
    ax.set_ylabel("Stress Level")
    ax.set_title("Comparison of Stress Across Exercise Habits")
    st.pyplot(fig)

    # ANOVA to test for significant difference
    leisure = df[df["LeisureCompOrNoSport"] == 1]["Stress"]
    competitive = df[df["LeisureCompOrNoSport"] == 2]["Stress"]
    no_sport = df[df["LeisureCompOrNoSport"] == 3]["Stress"]

    f_statistic, p_value = f_oneway(leisure, competitive, no_sport)

    # Display result
    st.write(f"**F-statistic:** {f_statistic:.3f}")
    st.write(f"**P-value:** {p_value:.5f}")

    # Interpretation of ANOVA results
    if p_value < 0.05:
        st.success("There is a significant difference in stress levels based on exercise habits.")
    else:
        st.info("There is no significant difference in stress levels based on exercise habits.")


    # exercise Habits vs. Life Satisfaction

    # Boxplot/Violin plot to compare life satisfaction across exercise habits
    st.header("Life Satisfaction Across Exercise Habits")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(x=df["LeisureCompOrNoSport"], y=df["LifeSatisf"], ax=ax, palette="muted")
    ax.set_xlabel("Exercise Habits (1=Leisure, 2=Competitive, 3=No Sport)")
    ax.set_ylabel("Life Satisfaction Score")
    ax.set_title("Comparison of Life Satisfaction Across Exercise Habits")
    st.pyplot(fig)

    # ANOVA to test for significant difference in life satisfaction
    leisure = df[df["LeisureCompOrNoSport"] == 1]["LifeSatisf"]
    competitive = df[df["LeisureCompOrNoSport"] == 2]["LifeSatisf"]
    no_sport = df[df["LeisureCompOrNoSport"] == 3]["LifeSatisf"]

    f_statistic, p_value = f_oneway(leisure, competitive, no_sport)

    # Display result
    st.write(f"**F-statistic:** {f_statistic:.3f}")
    st.write(f"**P-value:** {p_value:.5f}")

    # Interpretation of ANOVA results
    if p_value < 0.05:
        st.success("There is a significant difference in life satisfaction based on exercise habits.")
    else:
        st.info("There is no significant difference in life satisfaction based on exercise habits.")

# ------------------ Childhood Sports vs Current Exercise -------------------- #
elif section == "Current Exercise Habits vs Childhood Sports History":
    # Bar plot to compare current exercise habits based on childhood sports history
    st.header("Current Exercise Habits vs Childhood Sports History")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(data=df, x="LeisureCompOrNoSport", hue="Childhood7to16SportsYesNo", ax=ax, palette="muted")
    ax.set_xlabel("Current Exercise Habits (1=Leisure, 2=Competitive, 3=No Sport)")
    ax.set_ylabel("Count")
    ax.set_title("Comparison of Current Exercise Habits by Childhood Sports History")
    st.pyplot(fig)

    # Chi-Square Test to see if childhood sports history and current exercise habits are related
    contingency_table = pd.crosstab(df['Childhood7to16SportsYesNo'], df['LeisureCompOrNoSport'])

    # Perform the Chi-Square test
    chi2_stat, p_value, dof, expected = chi2_contingency(contingency_table)

    # Display result
    st.write(f"**Chi-Square Statistic:** {chi2_stat:.3f}")
    st.write(f"**P-value:** {p_value:.5f}")

    # Interpretation of results
    if p_value < 0.05:
        st.success("There is a significant association between childhood sports history and current exercise habits.")
    else:
        st.info("There is no significant association between childhood sports history and current exercise habits.")








# ------------------ Steps to Reproduce Study -------------------- #

# Steps to reproduce
st.markdown("#### Steps to reproduce:\n\n---\n\nUse the SWL and PSS (Satisfaction with Life - 5 items and Perceived Stress Scale - 14 items) and ask about childhood and current exercise habits, and workplace employee numbers in 4 categories (up to 10, 11-100, 101-1,000, and over 1,000). If needed, you can combine these into large (> 100) and small (< 100) companies. Collect demographic information such as age, gender, education level (basic/elementary, high school, university), perceived health on a 7-point scale, and perceived income on a 7-point scale. Ask for employment status in two categorical terms: employee or manager. Run chi-square and t-tests for group comparisons. Correlations/regression are feasible if the research question warrants it.")