import pandas as pd

analytics = pd.read_csv("raw_data/hackathon/Analytics Jobs.csv")
data_science = pd.read_csv("raw_data/hackathon/DataScience Jobs.csv")
jds = pd.read_excel("raw_data/hackathon/JDS Skill Traits.xlsx")
sds = pd.read_excel("raw_data/hackathon/SDS Personality Traits.xlsx")

datasets = {
    "Analytics Jobs": analytics,
    "Data Science Jobs": data_science,
    "JDS Skill Traits": jds,
    "SDS Personality Traits": sds
}

for name, df in datasets.items():

    print("\n" + "=" * 50)
    print(name)
    print("=" * 50)

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nDuplicate rows:")
    print(df.duplicated().sum())

    print("\nData types:")
    print(df.dtypes)