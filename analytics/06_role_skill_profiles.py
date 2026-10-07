import pandas as pd
import os

# Create output folder
os.makedirs("data/analysis", exist_ok=True)

# Load role-skill data
df = pd.read_csv("data/analysis/role_skill_demand.csv")

# Remove empty values
df["job_role"] = df["job_role"].fillna("").astype(str).str.strip()
df["skill"] = df["skill"].fillna("").astype(str).str.strip()

df = df[
    (df["job_role"] != "") &
    (df["skill"] != "")
]

# Calculate total skill count for each role
role_totals = (
    df.groupby("job_role")["job_count"]
    .sum()
    .reset_index(name="total_skill_mentions")
)

# Merge totals back
df = df.merge(
    role_totals,
    on="job_role",
    how="left"
)

# Calculate percentage of skill mentions within each role
df["skill_percentage"] = (
    df["job_count"] /
    df["total_skill_mentions"] * 100
).round(2)

# Keep the most important skills for each role
# Minimum 2 occurrences to remove very rare noise
df = df[df["job_count"] >= 2]

# Sort by role and skill importance
df = df.sort_values(
    ["job_role", "skill_percentage"],
    ascending=[True, False]
)

# Add skill rank within each role
df["skill_rank"] = (
    df.groupby("job_role")["skill_percentage"]
    .rank(method="first", ascending=False)
    .astype(int)
)

# Save complete role-skill profile
output_file = "data/analysis/role_skill_profiles.csv"

df.to_csv(
    output_file,
    index=False
)

print("\n========================================")
print("ROLE SKILL PROFILES COMPLETED")
print("========================================")

print("\nTotal role-skill combinations:", len(df))

print("\nExample Data Scientist profile:")

data_scientist = df[
    df["job_role"].str.lower() == "data scientist"
]

print(
    data_scientist[
        ["job_role", "skill", "job_count", "skill_percentage", "skill_rank"]
    ].head(15)
)

print("\nFile created:")
print(output_file)