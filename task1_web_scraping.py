# Task 1 : Web Scraping
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import requests
from io import StringIO
import warnings
warnings.filterwarnings("ignore")
PROJECT_OWNER = "Faizan Ahmad"
USERNAME = "faizan4232"

# Public Titanic CSV URL (GitHub Raw File)
URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

# Output Folder
OUTPUT_DIR = Path("faizan_task1_outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

# Theme
sns.set_theme(style="whitegrid")
gradient_blue = sns.color_palette("blend:#0D47A1,#42A5F5,#BBDEFB", 8)
# Scrape Dataset from Web
def scrape_dataset():
    try:
        print(f"\nConnecting to website for {PROJECT_OWNER}...")
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(URL, headers=headers, timeout=15)
        response.raise_for_status()
        df = pd.read_csv(StringIO(response.text))
        print("Dataset collected successfully from web.")
        print(f"Total Rows: {df.shape[0]}")
        print(f"Total Columns: {df.shape[1]}")
        return df
    except Exception as e:
        print("Error while collecting dataset:", e)
        exit()

def dataset_overview(df):
    print("\n========== FIRST 5 ROWS ==========")
    print(df.head())
    print("\n========== SHAPE ==========")
    print(df.shape)
    print("\n========== DATA TYPES ==========")
    print(df.dtypes)
    print("\n========== MISSING VALUES ==========")
    print(df.isnull().sum())
# Quick Insights
def quick_insights(df):
    print("\n========== KEY INSIGHTS ==========")
    survival_rate = round(df["Survived"].mean() * 100, 2)
    female_rate = round(df[df["Sex"] == "female"]["Survived"].mean() * 100, 2)
    male_rate = round(df[df["Sex"] == "male"]["Survived"].mean() * 100, 2)
    avg_fare = round(df["Fare"].mean(), 2)
    print(f"Overall Survival Rate : {survival_rate}%")
    print(f"Female Survival Rate  : {female_rate}%")
    print(f"Male Survival Rate    : {male_rate}%")
    print(f"Average Fare Paid     : {avg_fare}")
def save_dataset(df):
    file_path = OUTPUT_DIR / "titanic_scraped_data.csv"
    df.to_csv(file_path, index=False)
    print(f"\nDataset saved at: {file_path}")
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
                    ha="center", va="bottom")
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
                    ha="center", va="bottom")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "2_gender_chart.png", dpi=300)
    plt.show()
    plt.close()
    # 3. Fare Distribution
    plt.figure(figsize=(9,5))
    sns.histplot(df["Fare"], bins=30, kde=True,
                 color=gradient_blue[5], edgecolor="black")
    plt.title("Fare Distribution", fontsize=14, weight="bold")
    plt.xlabel("Fare")
    plt.ylabel("Passengers")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "3_fare_distribution.png", dpi=300)
    plt.show()
    plt.close()
def final_report():
    print("\n========== TASK COMPLETED ==========")
    print("Web scraping completed successfully.")
    print(f"Output Folder: {OUTPUT_DIR}")
    print(f"Prepared by {PROJECT_OWNER} ({USERNAME})")
if __name__ == "__main__":
    df = scrape_dataset()
    dataset_overview(df)
    quick_insights(df)
    save_dataset(df)
    generate_charts(df)
    final_report()
