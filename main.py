from matplotlib import pyplot as plt
import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df=pd.read_csv("student_performance_dataset.csv")

print("Sample Data:\n", df.head())


print("\nDataset Info:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())


X = df[["Study_Hours", "Attendance_Percentage", "Previous_Marks"]]
y = df["Final_Marks"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", round(mse, 2))
print("R² Score:", round(r2, 2))

plt.scatter(y_test, y_pred, color="purple")
plt.title("Actual vs Predicted Final Marks")
plt.xlabel("Actual Marks")
plt.ylabel("Predicted Marks")
plt.plot([0, 100], [0, 100], 'r--')
plt.show()