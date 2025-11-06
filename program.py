# Air Quality Data Cleaning & Analysis
# Python Mini Project

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# 1. Load Dataset
# -------------------------------
# Replace 'air_quality_data.csv' with your dataset file
df = pd.read_csv('air_quality_data.csv')

# Display first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# -------------------------------
# 2. Data Cleaning
# -------------------------------
# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Fill missing numerical values with mean
numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].mean())

# Check for duplicates
print("\nNumber of duplicate rows:", df.duplicated().sum())

# Drop duplicates if any
df = df.drop_duplicates()

# -------------------------------
# 3. Descriptive Statistics
# -------------------------------
print("\nDescriptive Statistics:")
print(df.describe())

# -------------------------------
# 4. Correlation Analysis
# -------------------------------
correlation = df.corr()
print("\nCorrelation Matrix:")
print(correlation)

# -------------------------------
# 5. Data Visualization
# -------------------------------
# Set seaborn style
sns.set(style="whitegrid")

# 5.1 Line Plot: PM2.5 & PM10 over Time
plt.figure(figsize=(10,5))
plt.plot(df['PM2.5'], label='PM2.5', color='red')
plt.plot(df['PM10'], label='PM10', color='blue')
plt.title('PM2.5 and PM10 Trends')
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend()
plt.savefig('PM_plot.png')
plt.close()

# 5.2 Histogram: NO2 Distribution
plt.figure(figsize=(6,4))
sns.histplot(df['NO2'], bins=20, kde=True, color='green')
plt.title('NO2 Distribution')
plt.xlabel('NO2 Concentration')
plt.ylabel('Frequency')
plt.savefig('NO2_hist.png')
plt.close()

# 5.3 Boxplot: SO2 & CO
plt.figure(figsize=(6,4))
sns.boxplot(data=df[['SO2', 'CO']])
plt.title('SO2 and CO Boxplot')
plt.savefig('SO2_CO_boxplot.png')
plt.close()

# 5.4 Heatmap: Correlation
plt.figure(figsize=(8,6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.savefig('Correlation_heatmap.png')
plt.close()

print("\nAll plots saved as PNG files in the current folder.")
