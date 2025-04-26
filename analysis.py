import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\saich\Downloads\archive\smart_city_citizen_activity.csv")

print("=== Dataset Information ===")
print(df.info())
print("\n")

print("=== First 5 Rows of the Dataset ===")   
print(df.head())
print("\n") 

print("=== Descriptive Statistics for Numerical Columns ===")
print(df.describe())
print("\n")

print("=== Missing Values in Each Column ===")
print(df.isnull().sum())
print("\n")

print("=== Gender Distribution ===")
gender_counts = df['Gender'].value_counts()
print(gender_counts)
print("\n")

plt.figure(figsize=(6, 6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90,
        colors=sns.color_palette("pastel"))
plt.title("Gender Distribution")
plt.axis('equal')
plt.show()

print("=== Transport Mode Distribution ===")
transport_counts = df['Mode_of_Transport'].value_counts()
print(transport_counts)
print("\n")

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Mode_of_Transport', order=transport_counts.index)
plt.title("Distribution of Transport Modes")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Mode_of_Transport', y='Carbon_Footprint_kgCO2')
plt.title("Carbon Footprint by Mode of Transport")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Age', bins=20, kde=True, color='skyblue')
plt.title("Age Distribution of Citizens")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Steps_Walked', bins=30, kde=True, color='green')
plt.title("Distribution of Steps Walked by Citizens")
plt.xlabel("Steps Walked")
plt.ylabel("Frequency")
plt.show()

df['Age_Group'] = pd.cut(df['Age'], bins=[0, 18, 30, 45, 60, 100], 
                         labels=['<18', '18-30', '31-45', '46-60', '60+'])

age_group_footprint = df.groupby('Age_Group', observed=True)['Carbon_Footprint_kgCO2'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(data=age_group_footprint, x='Age_Group', y='Carbon_Footprint_kgCO2')
plt.title("Average Carbon Footprint by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Average Carbon Footprint (kgCO2)")
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Mode_of_Transport', hue='Gender')
plt.title("Mode of Transport by Gender")
plt.xlabel("Mode of Transport")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.legend(title="Gender")
plt.show()

plt.figure(figsize=(12, 8))
numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
correlation_matrix = df[numeric_columns].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title("Correlation Heatmap Between Numerical Features")
plt.show()

print("=== Carbon Footprint Summary ===")
print(f"Average: {df['Carbon_Footprint_kgCO2'].mean():.2f} kgCO2")
print(f"Minimum: {df['Carbon_Footprint_kgCO2'].min():.2f} kgCO2")
print(f"Maximum: {df['Carbon_Footprint_kgCO2'].max():.2f} kgCO2")
print("\n")

ev_users = df[df['Mode_of_Transport'] == 'EV']
non_ev_users = df[df['Mode_of_Transport'] != 'EV']

print("=== Comparison: EV vs Non-EV Users ===")
print(f"Average Carbon Footprint (EV Users): {ev_users['Carbon_Footprint_kgCO2'].mean():.2f} kgCO2")
print(f"Average Carbon Footprint (Non-EV Users): {non_ev_users['Carbon_Footprint_kgCO2'].mean():.2f} kgCO2")
print("\n")

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Steps_Walked', y='Carbon_Footprint_kgCO2', hue='Mode_of_Transport')
plt.title("Relationship Between Steps Walked and Carbon Footprint")
plt.xlabel("Steps Walked")
plt.ylabel("Carbon Footprint (kgCO2)")
plt.show()

df.to_csv("cleaned_citizen_activity.csv", index=False)
print("✅ Data analysis completed. Cleaned data saved to 'cleaned_citizen_activity.csv'")
