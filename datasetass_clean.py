import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import (
    LabelEncoder, PowerTransformer, StandardScaler,
    MinMaxScaler, MaxAbsScaler, RobustScaler
)
from scipy.stats import boxcox

# Load Dataset
df = pd.read_excel("kaggle.xlsx")

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Missing Values
if 'customer_phone' in df.columns:
    df['customer_phone'] = df['customer_phone'].fillna(df['customer_phone'].median())

if 'customer_id' in df.columns:
    df['customer_id'] = df['customer_id'].fillna(df['customer_id'].mode()[0])

# Remove Duplicates
df.drop_duplicates(inplace=True)

# Label Encoding
if 'customer_name' in df.columns:
    le = LabelEncoder()
    df['customer_name_encoded'] = le.fit_transform(df['customer_name'])

print(df.head())

# Sample Transformation Data
data = {
    "Student_Name": ["Arun","Bala","Charan","Divya","Eswar","Farah","Gokul","Hari","Ishi","John"],
    "Study_Hours": [1,2,2,3,3,4,5,6,8,10],
    "Attendance": [50,60,65,70,75,80,85,90,95,98],
    "Marks": [30,40,50,55,60,65,70,75,85,95],
    "Pocket_Money": [50,80,100,120,150,180,200,250,300,350],
    "Daily_Screen_Time": [1,2,2,3,4,4,5,6,7,8]
}

df2 = pd.DataFrame(data)

df2["Pocket_Log"] = np.log(df2["Pocket_Money"])
df2["Study_Sqrt"] = np.sqrt(df2["Study_Hours"])
df2["Study_Cuberoot"] = np.cbrt(df2["Study_Hours"])
df2["Pocket_BoxCox"], _ = boxcox(df2["Pocket_Money"])

pt = PowerTransformer(method="yeo-johnson")
df2["Screen_YJ"] = pt.fit_transform(df2[["Daily_Screen_Time"]])

df2["Marks_Z"] = StandardScaler().fit_transform(df2[["Marks"]])
df2["Marks_MinMax"] = MinMaxScaler().fit_transform(df2[["Marks"]])
df2["Screen_MaxAbs"] = MaxAbsScaler().fit_transform(df2[["Daily_Screen_Time"]])
df2["Screen_Robust"] = RobustScaler().fit_transform(df2[["Daily_Screen_Time"]])

print(df2.head())

movies = ["MI2", "Fast&Furious", "Avengers", "Ironman", "Speed", "LifeofPi", "Redcliff"]
percentage = [61, 85, 91, 60, 55, 40, 63]

plt.figure(figsize=(8, 5))
plt.bar(movies, percentage)
plt.title("Movie Popularity")
plt.show()
