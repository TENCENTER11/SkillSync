import pandas as pd
import os

# Create output folder
os.makedirs("data/cleaned", exist_ok=True)

# Load raw datasets
analytics = pd.read_csv("raw_data/hackathon/Analytics Jobs.csv")
data_science = pd.read_csv("raw_data/hackathon/DataScience Jobs.csv")
jds = pd.read_excel("raw_data/hackathon/JDS Skill Traits.xlsx")
sds = pd.read_excel("raw_data/hackathon/SDS Personality Traits.xlsx")

# -----------------------------
# Analytics Jobs
# -----------------------------

analytics.columns = analytics.columns.str.strip()

# Clean text columns
text_columns = [
    "experience",
    "job_description",
    "job_desig",
    "job_type",
    "key_skills",
    "location"
]

for col in text_columns:
    analytics[col] = analytics[col].fillna("").astype(str).str.strip()

# Clean salary
analytics["salary"] = (
    analytics["salary"]
    .fillna("")
    .astype(str)
    .str.replace(",", "", regex=False)
)

# -----------------------------
# Data Science Jobs
# -----------------------------

data_science.columns = data_science.columns.str.strip()

# Clean text columns
for col in ["company_name", "job_title"]:
    data_science[col] = (
        data_science[col]
        .fillna("")
        .astype(str)
        .str.strip()
    )

# Convert salary columns to numeric
salary_columns = [
    "avg_salary",
    "min_salary",
    "max_salary"
]

for col in salary_columns:
    data_science[col] = (
        data_science[col]
        .astype(str)
        .str.replace(",", "", regex=False)
        .str.replace("₹", "", regex=False)
        .str.strip()
    )

    data_science[col] = pd.to_numeric(
        data_science[col],
        errors="coerce"
    )

# -----------------------------
# JDS Skill Traits
# -----------------------------

jds.columns = jds.columns.str.strip()

# -----------------------------
# SDS Personality Traits
# -----------------------------

sds.columns = sds.columns.str.strip()

# -----------------------------
# Save cleaned datasets
# -----------------------------

analytics.to_csv(
    "data/cleaned/analytics_jobs_cleaned.csv",
    index=False
)

data_science.to_csv(
    "data/cleaned/data_science_jobs_cleaned.csv",
    index=False
)

jds.to_csv(
    "data/cleaned/jds_skill_traits_cleaned.csv",
    index=False
)

sds.to_csv(
    "data/cleaned/sds_personality_traits_cleaned.csv",
    index=False
)

print("\nCleaning completed successfully!")

print("\nFiles created:")
print("1. data/cleaned/analytics_jobs_cleaned.csv")
print("2. data/cleaned/data_science_jobs_cleaned.csv")
print("3. data/cleaned/jds_skill_traits_cleaned.csv")
print("4. data/cleaned/sds_personality_traits_cleaned.csv")