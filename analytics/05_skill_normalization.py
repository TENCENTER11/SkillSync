import pandas as pd
import re
import os

# Create output folder
os.makedirs("data/analysis", exist_ok=True)

# Load skill demand data
df = pd.read_csv("data/analysis/skill_demand.csv")

# Clean skill text
df["skill"] = (
    df["skill"]
    .astype(str)
    .str.lower()
    .str.strip()
)

# Remove obvious junk
junk_values = [
    "",
    "...",
    "..",
    ".",
    "nan",
    "na",
    "n/a",
    "-"
]

df = df[~df["skill"].isin(junk_values)]

# Remove unwanted special characters
df["skill"] = df["skill"].apply(
    lambda x: re.sub(r"\s+", " ", x)
)

df["skill"] = df["skill"].apply(
    lambda x: re.sub(r"^[^a-z0-9]+|[^a-z0-9+#.]+$", "", x)
)

# Combine common variations
skill_mapping = {
    "python programming": "python",
    "python programming language": "python",
    "py": "python",

    "sql server": "sql",
    "mysql": "sql",
    "ms sql": "sql",

    "machine-learning": "machine learning",
    "machinelearning": "machine learning",
    "ml": "machine learning",

    "artificial intelligence": "artificial intelligence",
    "ai": "artificial intelligence",

    "data analytics": "data analytics",
    "data analysis": "data analysis",

    "power bi": "power bi",
    "powerbi": "power bi",

    "ms excel": "excel",
    "microsoft excel": "excel",

    "javascript": "javascript",
    "java script": "javascript",

    "c plus plus": "c++",
    "cpp": "c++"
}

df["skill"] = df["skill"].replace(skill_mapping)

# Combine duplicate normalized skills
normalized = (
    df.groupby("skill", as_index=False)["job_count"]
    .sum()
)

# Sort by demand
normalized = normalized.sort_values(
    "job_count",
    ascending=False
)

# Recalculate demand percentage
total_jobs = 15841

normalized["demand_percentage"] = (
    normalized["job_count"] / total_jobs * 100
).round(2)

# Save
output_file = "data/analysis/normalized_skill_demand.csv"

normalized.to_csv(
    output_file,
    index=False
)

print("\n========================================")
print("SKILL NORMALIZATION COMPLETED")
print("========================================")

print("\nSkills before normalization:", len(df))
print("Skills after normalization:", len(normalized))

print("\nTop 30 normalized skills:")
print(normalized.head(30))

print("\nFile created:")
print(output_file)