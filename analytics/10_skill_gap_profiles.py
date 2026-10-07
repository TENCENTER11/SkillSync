import pandas as pd
import os

os.makedirs("data/analysis", exist_ok=True)

# Load career profiles
df = pd.read_csv(
    "data/analysis/career_profiles.csv"
)

# Keep only useful columns
gap_profiles = df[
    [
        "job_role",
        "top_skills",
        "skill_count",
        "role_skill_demand"
    ]
].copy()

# Convert top skills into a clean list
gap_profiles["required_skills"] = (
    gap_profiles["top_skills"]
    .fillna("")
    .astype(str)
)

# Calculate a simple priority score
# Higher role demand + more required skills = higher priority
gap_profiles["priority_score"] = (
    gap_profiles["role_skill_demand"] *
    gap_profiles["skill_count"]
)

# Normalize priority score to 0–100
max_score = gap_profiles["priority_score"].max()

if max_score > 0:
    gap_profiles["priority_score"] = (
        gap_profiles["priority_score"] /
        max_score * 100
    ).round(2)

# Sort by priority
gap_profiles = gap_profiles.sort_values(
    "priority_score",
    ascending=False
)

# Save matching-ready career profiles
output_file = (
    "data/analysis/skill_gap_profiles.csv"
)

gap_profiles.to_csv(
    output_file,
    index=False
)

print("\n========================================")
print("SKILL GAP PROFILES CREATED")
print("========================================")

print(
    "\nTotal career profiles:",
    len(gap_profiles)
)

print("\nTop career profiles by priority:")

print(
    gap_profiles[
        [
            "job_role",
            "required_skills",
            "skill_count",
            "role_skill_demand",
            "priority_score"
        ]
    ].head(15).to_string(index=False)
)

print("\nFile created:")
print(output_file)