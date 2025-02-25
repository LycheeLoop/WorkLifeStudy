import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, pearsonr, f_oneway, chi2_contingency
from streamlit_lottie import st_lottie
import requests

# Function to load Lottie animation from URL
def load_lottie_url(url:str):
    return url

# Load your Lottie animation from a URL
lottie_url = "https://lottie.host/6f5b51d6-63e7-4fb8-9a09-c81a873648d6/0lOEKzDF98.json"  # Example URL

# Display the animation in Streamlit
st_lottie(load_lottie_url(lottie_url), speed=1, width=600, height=400, key="lottie1")


# ------------ Introduction ----------------#

df = pd.read_excel("Cleaned_Work_life.xlsx")

# Title and Introduction
st.markdown("# Work, Stress and Life Satisfaction Study\n\n---\n\nThis project analyzes data from a cross-sectional study of 549 participants exploring the relationship between company size, job roles, and well-being in the workplace. Specifically, it examines whether individuals working in larger companies experience higher stress levels and different levels of life satisfaction compared to those in smaller companies. The study also investigates how stress and life satisfaction vary between employees and managers. Additionally, it explores the connection between company size and regular exercise habits, as well as whether adult exercise patterns are linked to childhood exercise habits.\n\n---\n\n\n\n---\n\n")



# ------------ Add custom CSS to change sidebar color -------------#
st.markdown("""
    <style>
        /* Change the background color of the sidebar */
        .css-1d391kg { 
            background-color: #e08282; /* Change to any color you'd like */
        }

        /* Change the text color in the sidebar */
        .css-1d391kg h1, .css-1d391kg h2, .css-1d391kg p {
            color: #333; /* Adjust the text color */
        }

        /* Modify the background color of the selectbox */
        .stSelectbox>div>div>input {
            background-color: #e08282; /* Change to your desired color */
        }

        /* Modify the color of the selectbox dropdown */
        .stSelectbox>div>div>div {
            background-color: #e08282; /* Dropdown background color */
        }

        /* Customize the selected option color in the selectbox */
        .stSelectbox>div>div>div>div>div {
            color: #333; /* Adjust text color */
        }
    </style>
""", unsafe_allow_html=True)





# ------------ Create a sidebar for navigation ----------------#
st.sidebar.header("Navigation")
section = st.sidebar.selectbox("Choose Analysis Section", [
    "Introduction",
    "Methods",
    "Company Size & Wellbeing",
    "Income & Wellbeing",
    "Education & Wellbeing",
    "Life Satisfaction & Stress",
    "Employment Type Analysis",
    "Perceived Health & Stress",
    "Exercise Habits & Stress",
    "Current Exercise Habits vs Childhood Sports History",
    "Discussion",
    "Data Source",
    "Steps to Reproduce Study"
])


# ------------ Methods ----------------#
if section == "Methods":

    st.markdown("""
    # Methods

    This study utilizes the Satisfaction with Life Scale (SWL) and the Perceived Stress Scale (PSS) to assess life satisfaction and stress levels among participants. The SWL consists of five items (`ls1`through`ls5`), while the PSS includes fourteen items (`pss1`through`pss14`).  

    In addition to these psychological measures, participants provided information on their childhood and current exercise habits, as well as workplace characteristics, including company size categorized into four groups:  

    - **Up to 10 employees**  
    - **11 to 100 employees**  
    - **101 to 1,000 employees**  
    - **Over 1,000 employees**  

    If needed, company size may be further grouped into **small (<100 employees)** and **large (>100 employees)** organizations.  

    ## Collected Variables  

    ### Demographics  
    - **Gender**  
    - **Age**  
    - **Education Level** (`schooling1to3`): Basic/elementary, high school, university  
    - **Perceived Health** (`perceivedhealth1to7`): Rated on a 7-point scale  
    - **Perceived Income** (`income1to7`): Rated on a 7-point scale  

    ### Employment & Workplace  
    - **Employment Status** (`JobPositionEmployeeManager`): Employee or manager  
    - **Company Type** (`GovOrPrivateCo`): Government or private sector  
    - **Company Location** (`HUorEUorNONEuCo`): Hungary, European Union, or outside the EU  
    - **Company Size** (`CompanySize4cat`): Categorized as described above  

    ### Exercise & Sports History  
    - **Childhood Sports Participation** (`Childhood7to16SportsYesNo`)  
    - **Years of Sports History** (`SportsHistoryYears`)  
    - **Current Leisure Activity** (`LeisureCompOrNoSport`)  
    - **Social Support for Sports** (`SportSocSupport1to10ZeroNoSport`): Rated on a 10-point scale  

    ### Psychological Measures  
    - **Satisfaction with Life Scale (SWL)**: `ls1`, `ls2`, `ls3`, `ls4`, `ls5`  
    - **Perceived Stress Scale (PSS)**: `pss1`, `pss2`, `pss3`, `pss4`, `pss5`, `pss6`, `pss7`, `pss8`, `pss9`, `pss10`, `pss11`, `pss12`, `pss13`, `pss14`  

    ### Additional Computed Variables  
    - **Overall Stress Score** (`Stress`)  
    - **Life Satisfaction Score** (`LifeSatisf`)  
    - **Sports Group Classification** (`Sportgr`)  
    - **Company Size Classification** (`CompanySize`)  

    ## Statistical Analysis  

    Chi-square tests and t-tests were conducted to compare groups. Correlation and regression analyses were considered based on the research question.  

    This structured approach ensures a comprehensive analysis of the relationships between workplace factors, exercise habits, demographic characteristics, and psychological well-being.""")
    



    # Display the cleaned dataset
    st.markdown("**Cleaned Dataset Preview**:")

    st.write(df.head())
    st.markdown("\n\n---\n\n")




# ------------------ Company Size Analysis -------------------- #
elif section == "Company Size & Wellbeing":
    # Analyze company size and well-being with t-test 
    st.markdown("# (A) Company Size & Well-Being (Stress & Life Satisfaction)")

    # Separate groups for stress and life satisfaction
    stress_small_companies = df[df['CompanySize'] == 1]['Stress']
    stress_large_companies = df[df['CompanySize'] == 2]['Stress']

    life_satisf_small_companies = df[df['CompanySize'] == 1]['LifeSatisf']
    life_satisf_large_companies = df[df['CompanySize'] == 2]['LifeSatisf']

    # Perform independent t-test for Stress
    t_stat_stress, p_value_stress = ttest_ind(stress_small_companies, stress_large_companies, equal_var=False)
    # Perform independent t-test for Life Satisfaction
    t_stat_life_satisf, p_value_life_satisf = ttest_ind(life_satisf_small_companies, life_satisf_large_companies, equal_var=False)

    # Display results for Stress and Life Satisfaction
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
elif section == "Income & Wellbeing":
    st.markdown("# (B) Income & Wellbeing")

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

# ------------------------- Education -------------------------------#
elif section == "Education & Wellbeing":
    st.markdown("## **Education Level & Well-Being (Stress & Life Satisfaction)**")

    # Define education level mapping
    education_labels = {1: "Elementary", 2: "High School", 3: "University"}

    # Map numerical values to labels
    df["Education Level"] = df["schooling1to3"].map(education_labels)

    # Stress Analysis
    st.markdown("### **(A) Stress Levels by Education Level**")

    # Perform ANOVA for Stress
    stress_groups = [df[df["schooling1to3"] == level]["Stress"] for level in [1, 2, 3]]
    f_stat_stress, p_value_stress = f_oneway(*stress_groups)

    st.write(f"**F-statistic:** {f_stat_stress:.3f}")
    st.write(f"**P-value:** {p_value_stress:.5f}")

    if p_value_stress < 0.05:
        st.success("There is a statistically significant difference in stress levels across education levels.")
    else:
        st.info("There is no significant difference in stress levels across education levels.")

    # Boxplot for Stress
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(x=df["Education Level"], y=df["Stress"], ax=ax)
    ax.set_xlabel("Education Level")
    ax.set_ylabel("Stress")
    st.pyplot(fig)

    # Life Satisfaction Analysis
    st.markdown("### **(B) Life Satisfaction by Education Level**")

    # Perform ANOVA for Life Satisfaction
    life_satisfaction_groups = [df[df["schooling1to3"] == level]["LifeSatisf"] for level in [1, 2, 3]]
    f_stat_ls, p_value_ls = f_oneway(*life_satisfaction_groups)

    st.write(f"**F-statistic:** {f_stat_ls:.3f}")
    st.write(f"**P-value:** {p_value_ls:.5f}")

    if p_value_ls < 0.05:
        st.success("There is a statistically significant difference in life satisfaction across education levels.")
    else:
        st.info("There is no significant difference in life satisfaction across education levels.")

    # Boxplot for Life Satisfaction
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(x=df["Education Level"], y=df["LifeSatisf"], ax=ax)
    ax.set_xlabel("Education Level")
    ax.set_ylabel("Life Satisfaction")
    st.pyplot(fig)


    st.markdown("## **Education Level & Perceived Income**")

    # Define education level mapping
    education_labels = {1: "Elementary", 2: "High School", 3: "University"}

    # Map numerical values to labels
    df["Education Level"] = df["schooling1to3"].map(education_labels)

    # ANOVA Test for Income Across Education Levels
    st.markdown("### **Income Levels by Education Level**")

    # Perform ANOVA for Perceived Income
    income_groups = [df[df["schooling1to3"] == level]["income1to7"] for level in [1, 2, 3]]
    f_stat_income, p_value_income = f_oneway(*income_groups)

    st.write(f"**F-statistic:** {f_stat_income:.3f}")
    st.write(f"**P-value:** {p_value_income:.5f}")

    if p_value_income < 0.05:
        st.success("There is a statistically significant difference in perceived income across education levels.")
    else:
        st.info("There is no significant difference in perceived income across education levels.")

    # Boxplot for Income
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(x=df["Education Level"], y=df["income1to7"], ax=ax)
    ax.set_xlabel("Education Level")
    ax.set_ylabel("Perceived Income (1 to 7)")
    st.pyplot(fig)

# ------------------ Life Satisfaction & Stress -------------------- #
elif section == "Life Satisfaction & Stress":

    st.markdown("# Life Satisfaction & Stress")
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
    st.markdown("# (C) Employment Type Analysis - Stress Levels")

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
    st.markdown("# (D) Perceived Health - Stress Levels")



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
    st.markdown("# (E) Exercise Habits - Stress Levels")

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

# ------------------- Discussion ------------------#
elif section == "Discussion":
    st.markdown("""
    # **Summary and Discussion of Findings**  

    This study explored various factors influencing stress and life satisfaction, including company size, income, employment type, perceived health, and exercise habits. The analysis yielded several key insights regarding workplace environments, financial well-being, and lifestyle factors.  

    ## **Workplace Environment and Well-Being**  
    - There was **no significant difference** in **stress levels** or **life satisfaction** between employees in **small and large companies**. This suggests that company size alone may not be a determining factor in workplace stress or overall satisfaction. Other factors, such as workplace culture and work-life balance, might have a greater impact.  
    - However, a **significant difference** was found between **employees and managers**:  
    - **Managers reported higher stress levels** than employees, likely due to increased responsibilities.  
    - **Managers also reported higher life satisfaction**, which may be linked to job autonomy, financial benefits, or career fulfillment.  

    ## **Financial Factors and Well-Being**  
    - **Income was significantly correlated** with both stress and life satisfaction:  
    - Higher **income** was associated with **lower stress levels** (*r = -0.182, p < 0.001*).  
    - Higher **income** was associated with **greater life satisfaction** (*r = 0.209, p < 0.001*).  
    - While income plays a role, the relatively low correlation values suggest that other factors, such as job satisfaction and personal values, contribute to stress and life satisfaction as well.  

    ## **Interplay Between Stress and Life Satisfaction**  
    - A **strong negative correlation** was observed between **stress and life satisfaction** (*r = -0.474, p < 0.001*), indicating that individuals experiencing higher stress levels tend to report lower life satisfaction.  
    - This result highlights the importance of **stress management** in improving overall well-being.  

    ## **Health and Lifestyle Factors**  
    - **Perceived Health**:  
    - Individuals who reported **better perceived health** had **lower stress levels** (*r = -0.167, p < 0.001*) and **higher life satisfaction** (*r = 0.224, p < 0.001*).  
    - This reinforces the well-documented relationship between physical and mental/emotional well-being.  
    - **Exercise Habits**:  
    - There were **significant differences** in both **stress levels** (*F = 7.648, p < 0.001*) and **life satisfaction** (*F = 11.926, p < 0.001*) based on **exercise habits**.  
    - This suggests that **regular physical activity** is associated with **lower stress and greater life satisfaction**.  
    - **Childhood Sports Participation**:  
    - A **significant association** was found between **childhood sports participation and current exercise habits** (*χ² = 26.329, p < 0.001*).  
    - This indicates that early exposure to physical activity may influence **long-term health behaviors**.  

    ## **Conclusion**  
    These findings emphasize the **multifaceted nature of well-being**, highlighting the complex interactions between **workplace dynamics, financial stability, health, and lifestyle habits**.  

    - While **income and job role** influence **stress and satisfaction**, **personal health perceptions and exercise habits** also play a crucial role.  
    - The results suggest that **organizations and individuals** may benefit from **policies and behaviors that promote financial security and physical well-being** to enhance overall quality of life.  
    """)






# ------------------ Source -------------------- #
elif section == "Data Source":
    # Data Source
    st.markdown("### Data Source\n\n---\n\n**Study**: Work, Stress, and Life Satisfaction.\n\n**Institution**: Szechenyi Istvan Egyetem (Hungary).\n\n**Published**: 8 August 2024.\n\n**Categories**: Psychology, Adult, Workplace, Job Stress, Life Satisfaction, Exercise Psychology.\n\nDOI: 10.17632/hsgymx6zf8.2\n\n---\n\n")





# ------------------ Steps to Reproduce Study -------------------- #
elif section == "Steps to Reproduce Study":
    # Steps to reproduce
    st.markdown("""
# **Steps to Reproduce the Study**  

To replicate this study, follow these steps for data collection and analysis:  

## **1. Survey Design**  
Use standardized psychological scales:  
- **Satisfaction with Life Scale (SWL)** – 5 items  
- **Perceived Stress Scale (PSS)** – 14 items  

Additionally, collect information on:  
- **Exercise Habits**: Ask about both **childhood** and **current** exercise habits.  
- **Workplace Environment**: Categorize **company size** into:  
  - Up to **10** employees  
  - **11-100** employees  
  - **101-1,000** employees  
  - Over **1,000** employees  
  - (Optional) Combine into **small** (< 100 employees) and **large** (> 100 employees) categories.  

## **2. Demographic Information**  
Gather data on:  
- **Age**  
- **Gender**  
- **Education Level** (Basic/Elementary, High School, University)  
- **Perceived Health** (7-point scale)  
- **Perceived Income** (7-point scale)  
- **Employment Status**: Categorize as either **employee** or **manager**.  

## **3. Data Analysis**  
- Use **chi-square tests** to assess relationships between categorical variables.  
- Perform **independent t-tests** to compare group differences (e.g., stress levels between employees and managers).  
- Conduct **correlation analysis** (Pearson’s r) to examine relationships between continuous variables (e.g., stress and income, life satisfaction and perceived health).  
- **Regression analysis** can be performed if further predictive insights are needed based on the research question.  

These steps will ensure a structured and reproducible approach to studying workplace well-being, financial factors, and health-related behaviors.  
""")