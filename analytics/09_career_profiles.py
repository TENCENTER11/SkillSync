import pandas as pd
import os

os.makedirs("data/analysis", exist_ok=True)

# ---------------------------------------
# Load role-skill profiles
# ---------------------------------------

roles = pd.read_csv(
    "data/analysis/normalized_role_skill_profiles.csv"
)

# Clean role and skill names
roles["job_role"] = (
    roles["job_role"]
    .fillna("")
    .astype(str)
    .str.strip()
)

roles["skill"] = (
    roles["skill"]
    .fillna("")
    .astype(str)
    .str.strip()
)

# ---------------------------------------
# Keep important skills
# ---------------------------------------

roles = roles[
    roles["skill_rank"] <= 10
]

# ---------------------------------------
# Create career profiles
# ---------------------------------------

profiles = (
    roles
    .groupby("job_role")
    .agg(
        top_skills=("skill", lambda x: ", ".join(x)),
        skill_count=("skill", "count"),
        total_skill_mentions=("job_count", "sum")
    )
    .reset_index()
)

# ---------------------------------------
# Calculate role demand
# ---------------------------------------

role_demand = (
    roles.groupby("job_role")["job_count"]
    .sum()
    .reset_index(name="role_skill_demand")
)

profiles = profiles.merge(
    role_demand,
    on="job_role",
    how="left"
)

# ---------------------------------------
# Add trait information
# ---------------------------------------

jds = pd.read_csv(
    "data/analysis/jds_skill_trait_summary.csv"
)

personality = pd.read_csv(
    "data/analysis/personality_trait_summary.csv"
)

# Find strongest JDS trait
strongest_skill_trait = (
    jds.loc[
        jds["average_score"].idxmax(),
        "trait"
    ]
)

# Find strongest personality trait
strongest_personality_trait = (
    personality.loc[
        personality["average_score"].idxmax(),
        "trait"
    ]
)

profiles["strongest_skill_trait"] = strongest_skill_trait
profiles["strongest_personality_trait"] = strongest_personality_trait

# ---------------------------------------
# Sort by demand
# ---------------------------------------

profiles = profiles.sort_values(
    "role_skill_demand",
    ascending=False
)

# ---------------------------------------
# Save
# ---------------------------------------

output_file = (
    "data/analysis/career_profiles.csv"
)

profiles.to_csv(
    output_file,
    index=False
)

# ---------------------------------------
# Display
# ---------------------------------------

print("\n========================================")
print("CAREER PROFILES CREATED")
print("========================================")

print(
    "\nTotal career profiles:",
    len(profiles)
)

print("\nTop career profiles:")

print(
    profiles[
        [
            "job_role",
            "top_skills",
            "skill_count",
            "role_skill_demand"
        ]
    ].head(15).to_string(index=False)
)

print("\nStrongest overall skill trait:")
print(strongest_skill_trait)

print("\nStrongest overall personality trait:")
print(strongest_personality_trait)

print("\nFile created:")
print(output_file)