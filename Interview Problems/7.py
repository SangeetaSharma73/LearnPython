import pandas as pd
import matplotlib.pyplot as plt

# Read data from the CSV file
data = pd.read_csv(r"C:\Users\user\OneDrive\Desktop\StudentTable.csv")

# Count how many times each subject appears in the 'Favourite Subject' column
subject_count = data['Favourite Subject'].value_counts()

# Plot the bar chart
plt.bar(subject_count.index, subject_count.values, color='pink')
plt.title("Favourite Subjects")
plt.xlabel("Subjects")
plt.ylabel("Number of Students")
plt.show()