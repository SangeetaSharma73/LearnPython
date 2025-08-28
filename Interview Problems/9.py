import pandas as pd
import matplotlib.pyplot as plt
# Read data from the CSV file
data = pd.read_csv(r"C:\Users\user\OneDrive\Desktop\StudentTable.csv")

# Filter data by class
class_7A = data[data['Class'] == '7A']
class_7B = data[data['Class'] == '7B']
# Count the favourite subjects for each class
fav_subject_7A = class_7A['Favourite Subject'].value_counts()
fav_subject_7B = class_7B['Favourite Subject'].value_counts()
# Create two bar charts side by side
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Bar chart for Class 7A
axes[0].bar(fav_subject_7A.index, fav_subject_7A.values, color='brown')
axes[0].set_title('Class 7A: Favourite Subjects')
axes[0].set_xlabel('Subject')
axes[0].set_ylabel('Number of Students')
# Bar chart for Class 7B
axes[1].bar(fav_subject_7B.index, fav_subject_7B.values, color='green')
axes[1].set_title('Class 7B: Favourite Subjects')
axes[1].set_xlabel('Subject')
axes[1].set_ylabel('Number of Students')

# Display the charts
plt.tight_layout()
plt.show()