import pandas as pd
import re
import os
from collections import Counter

# Create output folder
os.makedirs("data/analysis", exist_ok=True)

# Load cleaned Analytics Jobs dataset
df = pd.read_csv("data/cleaned/analytics_jobs_cleaned.csv")

print("Dataset loaded:", df.shape)

# ---------------------------------------
# 1. Job role analysis
# ---------------------------------------

role_counts = (
    df["job_desig"]
    .str.strip()
    .replace("", pd.NA)
    .dropna()
    .value_counts()
)

role_counts_df = role_counts.reset_index()
role_counts_df.columns = ["job_role", "job_count"]

role_counts_df.to_csv(
    "data/analysis/job_role_demand.csv",
    index=False
)

print("\nTop 20 Job Roles:")
print(role_counts_df.head(20))


# ---------------------------------------
# 2. Skill extraction
# ---------------------------------------

all_skills = []

for value in df["key_skills"].dropna():

    text = str(value).lower()

    # Split skills using common separators
    skills = re.split(r"[,;|/]+", text)

    for skill in skills:

        skill = skill.strip()

        if skill and len(skill) > 1:
            all_skills.append(skill)


# Count skills
skill_counts = Counter(all_skills)

skill_demand_df = pd.DataFrame(
    skill_counts.items(),
    columns=["skill", "job_count"]
)

skill_demand_df = skill_demand_df.sort_values(
    "job_count",
    ascending=False
)

# Total jobs
total_jobs = len(df)

# Skill demand percentage
skill_demand_df["demand_percentage"] = (
    skill_demand_df["job_count"] / total_jobs * 100
).round(2)

skill_demand_df.to_csv(
    "data/analysis/skill_demand.csv",
    index=False
)

print("\nTop 30 Skills:")
print(skill_demand_df.head(30))


# ---------------------------------------
# 3. Job role + skill relationship
# ---------------------------------------

role_skill_data = []

for _, row in df.iterrows():

    role = str(row["job_desig"]).strip()

    if not role:
        continue

    skills = re.split(
        r"[,;|/]+",
        str(row["key_skills"]).lower()
    )

    for skill in skills:

        skill = skill.strip()

        if skill and len(skill) > 1:

            role_skill_data.append({
                "job_role": role,
                "skill": skill
            })


role_skill_df = pd.DataFrame(role_skill_data)

# Count how frequently each skill occurs for each role
role_skill_counts = (
    role_skill_df
    .groupby(["job_role", "skill"])
    .size()
    .reset_index(name="job_count")
)

role_skill_counts = role_skill_counts.sort_values(
    ["job_role", "job_count"],
    ascending=[True, False]
)

role_skill_counts.to_csv(
    "data/analysis/role_skill_demand.csv",
    index=False
)


# ---------------------------------------
# 4. Summary
# ---------------------------------------

print("\n========================================")
print("SKILL ANALYSIS COMPLETED")
print("========================================")

print("\nTotal jobs:", total_jobs)

print("Unique job roles:", len(role_counts_df))

print("Unique extracted skills:", len(skill_demand_df))

print("\nFiles created:")

print("1. data/analysis/job_role_demand.csv")
print("2. data/analysis/skill_demand.csv")
print("3. data/analysis/role_skill_demand.csv")