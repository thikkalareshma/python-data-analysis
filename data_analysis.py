import pandas as pd

data = {
    "Employee": ["John", "Sara", "Mike", "David"],
    "Department": ["IT", "HR", "IT", "Finance"],
    "Salary": [50000, 45000, 60000, 70000]
}

df = pd.DataFrame(data)

print("Dataset")
print(df)

avg_salary = df.groupby("Department")["Salary"].mean()

print("\nAverage Salary By Department")
print(avg_salary)
