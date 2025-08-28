import pandas as pd
import matplotlib.pyplot as plt

# Read data from the CSV file
data = pd.read_csv(r"C:\Users\user\OneDrive\Desktop\StudentTable.csv")
ages = [12, 13, 12, 13, 12, 13, 12, 13, 12, 13, 12, 13, 12, 13, 12]
#ages = data['Age']

age_count = {}
for age in ages:
    age_count[age] = age_count.get(age, 0) + 1
plt.plot(list(age_count.keys()), list(age_count.values()), marker='*',color='blue')


plt.title("Age Distribution of Students")
plt.xlabel("Age")
plt.ylabel("Number of Students")
plt.grid(True)
plt.show()