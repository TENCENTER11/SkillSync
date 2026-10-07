import pandas as pd
import re
import os

# Create output folder
os.makedirs("data/analysis", exist_ok=True)

# Load role-skill data
df = pd.read_csv("data/analysis/role_skill_profiles.csv")

# ---------------------------------------
# 1. Basic role cleaning
# ---------------------------------------

df["job_role"] = (
    df["job_role"]
    .fillna("")
    .astype(str)
    .str.strip()
    .str.lower()
)

# Remove extra spaces
df["job_role"] = df["job_role"].apply(
    lambda x: re.sub(r"\s+", " ", x)
)

# Remove leading/trailing special characters
df["job_role"] = df["job_role"].apply(
    lambda x: re.sub(r"^[^a-z0-9]+|[^a-z0-9]+$", "", x)
)

# ---------------------------------------
# 2. Common role variations
# ---------------------------------------

role_mapping = {

    "data scientist": "data scientist",
    "data scientist ": "data scientist",

    "data analyst": "data analyst",
    "data analytics": "data analyst",

    "business analyst": "business analyst",
    "business analysis": "business analyst",

    "software developer": "software developer",
    "software development": "software developer",

    "software engineer": "software engineer",

    "data engineer": "data engineer",

    "machine learning engineer": "machine learning engineer",
    "machine learning": "machine learning engineer",

    "ai engineer": "ai engineer",
    "artificial intelligence engineer": "ai engineer",

    "web developer": "web developer",
    "web development": "web developer",

    "frontend developer": "frontend developer",
    "front end developer": "frontend developer",

    "backend developer": "backend developer",
    "back end developer": "backend developer",

    "full stack developer": "full stack developer",
    "fullstack developer": "full stack developer",

    "project manager": "project manager",
    "project management": "project manager",

    "product manager": "product manager",

    "digital marketing manager": "digital marketing manager",
    "digital marketing": "digital marketing",

    "seo executive": "seo executive",
    "seo analyst": "seo analyst"
}

df["job_role"] = df["job_role"].replace(role_mapping)

# ---------------------------------------
# 3. Remove obvious junk roles
# ---------------------------------------

junk_roles = [
    "",
    "nan",
    "na",
    "n/a",
    "...",
    "associate",
    "executive",
    "manager",
    "analyst"
]

df = df[~df["job_role"].isin(junk_roles)]

# ---------------------------------------
# 4. Combine duplicate normalized roles
# ---------------------------------------

group_columns = [
    "job_role",
    "skill"
]

df = (
    df.groupby(group_columns, as_index=False)
    .agg({
        "job_count": "sum"
    })
)

# ---------------------------------------
# 5. Recalculate skill percentages
# ---------------------------------------

role_totals = (
    df.groupby("job_role")["job_count"]
    .sum()
    .reset_index(name="total_skill_mentions")
)

df = df.merge(
    role_totals,
    on="job_role",
    how="left"
)

df["skill_percentage"] = (
    df["job_count"] /
    df["total_skill_mentions"] * 100
).round(2)

# ---------------------------------------
# 6. Rank skills within each role
# ---------------------------------------

df = df.sort_values(
    ["job_role", "skill_percentage"],
    ascending=[True, False]
)

df["skill_rank"] = (
    df.groupby("job_role")["skill_percentage"]
    .rank(method="first", ascending=False)
    .astype(int)
)

# ---------------------------------------
# 7. Save normalized role profiles
# ---------------------------------------

output_file = "data/analysis/normalized_role_skill_profiles.csv"

df.to_csv(
    output_file,
    index=False
)

# ---------------------------------------
# 8. Display results
# ---------------------------------------

print("\n========================================")
print("ROLE NORMALIZATION COMPLETED")
print("========================================")

print("\nUnique roles after normalization:", df["job_role"].nunique())

print("\nTop normalized roles:")

print(
    df.groupby("job_role")["job_count"]
    .sum()
    .sort_values(ascending=False)
    .head(20)
)

print("\nData Scientist profile:")

print(
    df[df["job_role"] == "data scientist"][
        ["job_role", "skill", "job_count", "skill_percentage", "skill_rank"]
    ].head(15)
)

print("\nFile created:")
print(output_file)