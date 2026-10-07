import pandas as pd

# Load datasets
analytics = pd.read_csv("raw_data/hackathon/Analytics Jobs.csv")
data_science = pd.read_csv("raw_data/hackathon/DataScience Jobs.csv")
jds = pd.read_excel("raw_data/hackathon/JDS Skill Traits.xlsx")
sds = pd.read_excel("raw_data/hackathon/SDS Personality Traits.xlsx")

print("\n===== ANALYTICS JOBS =====")
print("Shape:", analytics.shape)
print("Columns:", analytics.columns.tolist())

print("\n===== DATA SCIENCE JOBS =====")
print("Shape:", data_science.shape)
print("Columns:", data_science.columns.tolist())

print("\n===== JDS SKILL TRAITS =====")
print("Shape:", jds.shape)
print("Columns:", jds.columns.tolist())

print("\n===== SDS PERSONALITY TRAITS =====")
print("Shape:", sds.shape)
print("Columns:", sds.columns.tolist())