import pandas as pd
import os

# Create output folder
os.makedirs("data/analysis", exist_ok=True)

# Load cleaned trait datasets
jds = pd.read_csv(
    "data/cleaned/jds_skill_traits_cleaned.csv"
)

sds = pd.read_csv(
    "data/cleaned/sds_personality_traits_cleaned.csv"
)

# =========================================
# JDS SKILL TRAITS
# =========================================

jds.columns = jds.columns.str.strip()

# Rename columns for easier use
jds = jds.rename(columns={
    "big_data_skills": "big_data",
    "maths-stats_skills": "maths_statistics",
    "coding_skills": "coding",
    "ai_and_ml_skills": "ai_ml",
    "dashboard_and_storytelling_skills": "dashboard_storytelling",
    "salary_hike_high_or_low": "salary_hike"
})

# Calculate average skill scores
skill_trait_summary = pd.DataFrame({
    "trait": [
        "big_data",
        "maths_statistics",
        "coding",
        "ai_ml",
        "dashboard_storytelling"
    ],
    "average_score": [
        jds["big_data"].mean(),
        jds["maths_statistics"].mean(),
        jds["coding"].mean(),
        jds["ai_ml"].mean(),
        jds["dashboard_storytelling"].mean()
    ]
})

skill_trait_summary["average_score"] = (
    skill_trait_summary["average_score"].round(2)
)

skill_trait_summary.to_csv(
    "data/analysis/jds_skill_trait_summary.csv",
    index=False
)

# =========================================
# SDS PERSONALITY TRAITS
# =========================================

sds.columns = sds.columns.str.strip()

sds = sds.rename(columns={
    "neuroticism": "neuroticism",
    "extraversion": "extraversion",
    "openness_to_experience": "openness",
    "agreeableness": "agreeableness",
    "conscientiousness": "conscientiousness",
    "success_ classification_ high_low":
        "success_classification"
})

# Calculate average personality scores
personality_summary = pd.DataFrame({
    "trait": [
        "neuroticism",
        "extraversion",
        "openness",
        "agreeableness",
        "conscientiousness"
    ],
    "average_score": [
        sds["neuroticism"].mean(),
        sds["extraversion"].mean(),
        sds["openness"].mean(),
        sds["agreeableness"].mean(),
        sds["conscientiousness"].mean()
    ]
})

personality_summary["average_score"] = (
    personality_summary["average_score"].round(2)
)

personality_summary.to_csv(
    "data/analysis/personality_trait_summary.csv",
    index=False
)

# =========================================
# SUCCESS CLASSIFICATION
# =========================================

success_counts = (
    sds["success_classification"]
    .value_counts()
    .reset_index()
)

success_counts.columns = [
    "success_classification",
    "count"
]

success_counts.to_csv(
    "data/analysis/success_classification_summary.csv",
    index=False
)

# =========================================
# DISPLAY RESULTS
# =========================================

print("\n========================================")
print("CAREER TRAIT ANALYSIS COMPLETED")
print("========================================")

print("\nJDS Skill Trait Averages:")
print(skill_trait_summary)

print("\nPersonality Trait Averages:")
print(personality_summary)

print("\nSuccess Classification:")
print(success_counts)

print("\nFiles created:")
print("1. data/analysis/jds_skill_trait_summary.csv")
print("2. data/analysis/personality_trait_summary.csv")
print("3. data/analysis/success_classification_summary.csv")