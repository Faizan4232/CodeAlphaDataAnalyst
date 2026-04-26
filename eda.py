# Task 2: Exploratory Data Analysis (EDA)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
# # Personal Information
PROJECT_OWNER = "Faizan Ahmad"
USERNAME = "faizan4232"
DATA_FILE = "Titanic-Dataset.csv"
# Output Folder
OUTPUT_DIR = Path("faizan_eda_outputs")
OUTPUT_DIR.mkdir(exist_ok=True)
# Theme Settings
sns.set_theme(style="whitegrid")

gradient_blue = sns.color_palette("blend:#0D47A1,#42A5F5,#BBDEFB", 8)
# Load Dataset
def load_dataset():
    try:
        df = pd.read_csv(DATA_FILE)
        print(f"\nDataset loaded successfully for {PROJECT_OWNER}")
        return df
    except FileNotFoundError:
        print("Titanic-Dataset.csv file not found.")
        exit()
# Dataset Overview
def dataset_overview(df):
    print("\n========== FIRST 5 ROWS ==========")
    print(df.head())

    print("\n========== SHAPE ==========")
    print(df.shape)

    print("\n========== DATA TYPES ==========")
    print(df.dtypes)

    print("\n========== MISSING VALUES ==========")
    print(df.isnull().sum())

    print("\n========== SUMMARY ==========")
    print(df.describe(include="all"))
# Insights
def quick_insights(df):
    print("\n========== KEY INSIGHTS ==========")

    survival_rate = round(df["Survived"].mean() * 100, 2)
    print(f"Overall Survival Rate: {survival_rate}%")

    female_rate = round(df[df["Sex"] == "female"]["Survived"].mean() * 100, 2)
    male_rate = round(df[df["Sex"] == "male"]["Survived"].mean() * 100, 2)

    print(f"Female Survival Rate: {female_rate}%")
    print(f"Male Survival Rate: {male_rate}%")

    avg_age = round(df["Age"].mean(), 2)
    print(f"Average Age: {avg_age}")
# Charts Section
def generate_charts(df):

    # 1. Survival Count
    plt.figure(figsize=(8,5))
    ax = sns.countplot(data=df, x="Survived", hue="Survived",
                       palette=gradient_blue, legend=False)
    plt.title("Passenger Survival Overview", fontsize=14, weight="bold")
    plt.xticks([0,1], ["Not Survived", "Survived"])
    for p in ax.patches:
        ax.annotate(int(p.get_height()),
                    (p.get_x()+p.get_width()/2, p.get_height()),
                    ha="center", va="bottom", fontsize=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "1_survival_chart.png", dpi=300)
    plt.show()
    plt.close()

    # 2. Gender Distribution
    plt.figure(figsize=(8,5))
    ax = sns.countplot(data=df, x="Sex", hue="Sex",
                       palette=gradient_blue, legend=False)
    plt.title("Passenger Gender Distribution", fontsize=14, weight="bold")
    for p in ax.patches:
        ax.annotate(int(p.get_height()),
                    (p.get_x()+p.get_width()/2, p.get_height()),
                    ha="center", va="bottom", fontsize=10)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "2_gender_chart.png", dpi=300)
    plt.show()
    plt.close()

    # 3. Survival by Gender
    plt.figure(figsize=(8,5))
    sns.countplot(data=df, x="Sex", hue="Survived", palette=gradient_blue)
    plt.title("Survival Based on Gender", fontsize=14, weight="bold")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "3_survival_by_gender.png", dpi=300)
    plt.show()
    plt.close()

    # 4. Age Distribution
    plt.figure(figsize=(9,5))
    sns.histplot(df["Age"].dropna(), bins=25, kde=True,
                 color=gradient_blue[4], edgecolor="black")
    plt.title("Age Distribution", fontsize=14, weight="bold")
    plt.xlabel("Age")
    plt.ylabel("Passengers")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "4_age_distribution.png", dpi=300)
    plt.show()
    plt.close()

    # 5. Fare Distribution
    plt.figure(figsize=(9,5))
    sns.histplot(df["Fare"], bins=30, kde=True,
                 color=gradient_blue[6], edgecolor="black")
    plt.title("Fare Distribution", fontsize=14, weight="bold")
    plt.xlabel("Fare")
    plt.ylabel("Passengers")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "5_fare_distribution.png", dpi=300)
    plt.show()
    plt.close()

    # 6. Correlation Heatmap
    plt.figure(figsize=(9,6))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap="Blues",
                linewidths=0.5, fmt=".2f")
    plt.title("Feature Correlation Heatmap", fontsize=14, weight="bold")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "6_heatmap.png", dpi=300)
    plt.show()
    plt.close()
# Final Report
def final_report():
    print("\n========== TASK COMPLETED ==========")
    print("All premium charts displayed and saved.")
    print(f"Output Folder: {OUTPUT_DIR}")
    print(f"Prepared by {PROJECT_OWNER} ({USERNAME})")

# Main Function
if __name__ == "__main__":
    df = load_dataset()
    dataset_overview(df)
    quick_insights(df)
    generate_charts(df)
    final_report()