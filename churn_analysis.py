import pandas as pd 
import numpy as np

df = pd.read_csv("churn.csv")

df= df.drop_duplicates()

print(df.isnull().sum())

df = df[["customerID", "gender", "SeniorCitizen", "Partner", "Dependents", "tenure", "TechSupport", "StreamingTV", "StreamingMovies", "Contract", "PaymentMethod", "MonthlyCharges", "TotalCharges", "Churn"]]

df["Churn"] = df["Churn"].map({"Yes":1, "No":0})

df.groupby("gender")["Churn"].mean()

df.groupby("SeniorCitizen")["Churn"].mean()

df.groupby("Partner")["Churn"].mean()

df.groupby("Dependents")["Churn"].mean()

bins =  [0, 22, 42, 10000]
labels = ["low", "medium", "high"]
df["tenure_group"] = pd.cut(df["tenure"], bins=bins, labels=labels, include_lowest=True)
df.groupby("tenure_group")["Churn"].mean()

df.groupby("TechSupport")["Churn"].mean()

df.groupby("StreamingTV")["Churn"].mean()

df.groupby("StreamingMovies")["Churn"].mean()

df.groupby("Contract")["Churn"].mean()

df.groupby("PaymentMethod")["Churn"].mean()

bins = [0, 40, 80, 150000]
labels = ["low", "medium", "high"]

df["MonthlyCharges_group"] = pd.cut(df["MonthlyCharges"], bins=bins, labels=labels)
df.groupby("MonthlyCharges_group")["Churn"].mean()


df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df["Charges_rate"] = df["TotalCharges"] / df["tenure"].replace(0, np.nan)

bins = [0, 40, 80, 10000000]
labels = ["low", "medium", "high"]

df["Charges_rate"] = pd.cut(df["Charges_rate"], bins=bins, labels=labels, include_lowest=True)

df.groupby("Charges_rate")["Churn"].mean()

df.to_csv("clean_churn.csv", index=False)