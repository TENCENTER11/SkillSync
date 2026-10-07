import pandas as pd
import os

os.makedirs("data/analysis", exist_ok=True)

# Load final outputs
skills = pd.read_csv(
    "data/analysis/normalized_skill_demand.csv"
)

roles = pd.read_csv(
    "data/analysis/career_profiles.csv"
)

skill_traits = pd.read_csv(
    "data/analysis/jds_skill_trait_summary.csv"
)

personality = pd.read_csv(
    "data/analysis/personality_trait_summary.csv"
)

success = pd.read_csv(
    "data/analysis/success_classification_summary.csv"
)

# =========================================
# Create summary
# =========================================

lines = []

lines.append("SKILLSYNC ANALYTICS SUMMARY")
lines.append("=" * 60)
lines.append("")

lines.append("DATASET / ANALYSIS")
lines.append("-" * 60)
lines.append("Normalized skills: " + str(len(skills)))
lines.append("Career profiles: " + str(len(roles)))
lines.append("")

# -----------------------------------------
# Top skills
# -----------------------------------------

lines.append("TOP 15 SKILLS")
lines.append("-" * 60)

for i, row in skills.head(15).iterrows():
    lines.append(
        f"{i + 1}. {row['skill']} - "
        f"{row['demand_percentage']}% demand"
    )

lines.append("")

# -----------------------------------------
# Top career profiles
# -----------------------------------------

lines.append("TOP 15 CAREER PROFILES")
lines.append("-" * 60)

for i, row in roles.head(15).iterrows():
    lines.append(
        f"{i + 1}. {row['job_role']} - "
        f"demand score: {row['role_skill_demand']}"
    )

lines.append("")

# -----------------------------------------
# Skill traits
# -----------------------------------------

lines.append("SKILL TRAIT AVERAGES")
lines.append("-" * 60)

for _, row in skill_traits.iterrows():
    lines.append(
        f"{row['trait']}: {row['average_score']}"
    )

strongest_skill = skill_traits.loc[
    skill_traits["average_score"].idxmax(),
    "trait"
]

lines.append("")
lines.append(
    f"Strongest overall skill trait: {strongest_skill}"
)
lines.append("")

# -----------------------------------------
# Personality traits
# -----------------------------------------

lines.append("PERSONALITY TRAIT AVERAGES")
lines.append("-" * 60)

for _, row in personality.iterrows():
    lines.append(
        f"{row['trait']}: {row['average_score']}"
    )

strongest_personality = personality.loc[
    personality["average_score"].idxmax(),
    "trait"
]

lines.append("")
lines.append(
    f"Strongest overall personality trait: "
    f"{strongest_personality}"
)
lines.append("")

# -----------------------------------------
# Success classification
# -----------------------------------------

lines.append("SUCCESS CLASSIFICATION")
lines.append("-" * 60)

for _, row in success.iterrows():
    lines.append(
        f"Class {row['success_classification']}: "
        f"{row['count']}"
    )

lines.append("")

# -----------------------------------------
# Final note
# -----------------------------------------

lines.append("IMPORTANT INTERPRETATION")
lines.append("-" * 60)
lines.append(
    "Career priority scores represent demand/skill-based "
    "analytics from the supplied datasets."
)
lines.append(
    "They should not be interpreted as proof that personality "
    "traits cause career success."
)

# Save summary
output_file = (
    "data/analysis/SKILLSYNC_ANALYTICS_SUMMARY.txt"
)

with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("\n========================================")
print("FINAL ANALYTICS SUMMARY CREATED")
print("========================================")

print("\nFile created:")
print(output_file)