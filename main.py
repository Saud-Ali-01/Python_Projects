import pandas as ps
import numpy as ny
from functions import *
df = ps.read_csv("student.csv")

subjects = ["Math","Science","English","History"]
# create a object inside the function which is import to use total and average
tools = marks()
df['Total_Marks'] = tools.total(df[subjects])
df['Average'] =tools.Average(df[subjects])
df['Grade'] = df['Average'].apply(Grade)

# Pass/Fail Statistics
# ---------------------------------------------------------
# Rule: A student passes only if they score 40 or above in ALL subjects
# Using numpy.where for conditional assignment
df['Status'] = ny.where((df[subjects] >= 40).all(axis=1), 'Pass', 'Fail')

print("---processed Student Data ---")
print(df[['Name','Total_Marks','Average','Grade','Status']],"\n")

# Calculate overall pass/fail percentage
pass_fail_counts = df['Status'].value_counts(normalize=True) * 100
print("--- Pass/Fail Statistics ---")
print(pass_fail_counts.round(2).astype(str) + '%', "\n")

# ---------------------------------------------------------
# 5. Subject-Wise Performance
# ---------------------------------------------------------
# Using pandas aggregation to get mean, max, and min for each subject
subject_performance = df[subjects].agg(['mean', 'max', 'min']).round(2)

print("--- Subject-Wise Performance ---")
print(subject_performance, "\n")

# ---------------------------------------------------------
# 6. Top Performers
# ---------------------------------------------------------
# Sort by Total Marks in descending order and select the top 3
top_performers = df.sort_values(by='Total_Marks', ascending=False).head(3)

print("--- Top 3 Performers ---")
print(top_performers[['Name', 'Total_Marks', 'Grade']])