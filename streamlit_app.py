import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, pearsonr

# Title and Introduction
st.markdown("# Introduction\n\n---\n\nThis project analyzes data from a cross-sectional study of 549 participants exploring the relationship between company size, job roles, and well-being in the workplace. Specifically, it examines whether individuals working in larger companies experience higher stress levels and different levels of life satisfaction compared to those in smaller companies. The study also investigates how stress and life satisfaction vary between employees and managers. Additionally, it explores the connection between company size and regular exercise habits, as well as whether adult exercise patterns are linked to childhood exercise habits.")

# Data Source
st.markdown("## Data Source\n\n---\n\n**Study**: Work, Stress, and Life Satisfaction.\n\n**Institution**: Szechenyi Istvan Egyetem (Hungary).\n\n**Published**: 8 August 2024.\n\n**Categories**: Psychology, Adult, Workplace, Job Stress, Life Satisfaction, Exercise Psychology.\n\nDOI: 10.17632/hsgymx6zf8.2\n\n---\n\n")



# Upload dataset 
df = pd.read_excel("Cleaned_Work_life.xlsx")



st.markdown("#### Each participant provided responses to the following variables:")
st.text(f"Columns: {', '.join(df.columns)}")



# Display the cleaned dataset
st.markdown("**Cleaned Dataset Preview**:")

st.write(df.head())
st.markdown("\n\n---\n\n")


# ------------------ Company Size Analysis -------------------- #

# Analyze company size and well-being with t-test 
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


# ------------------ Income Analysis -------------------- #
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



st.markdown("### Life Satisfaction & Income Analysis")
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





# Steps to reproduce
st.markdown("#### Steps to reproduce:\n\n---\n\nUse the SWL and PSS (Satisfaction with Life - 5 items and Perceived Stress Scale - 14 items) and ask about childhood and current exercise habits, and workplace employee numbers in 4 categories (up to 10, 11-100, 101-1,000, and over 1,000). If needed, you can combine these into large (> 100) and small (< 100) companies. Collect demographic information such as age, gender, education level (basic/elementary, high school, university), perceived health on a 7-point scale, and perceived income on a 7-point scale. Ask for employment status in two categorical terms: employee or manager. Run chi-square and t-tests for group comparisons. Correlations/regression are feasible if the research question warrants it.")