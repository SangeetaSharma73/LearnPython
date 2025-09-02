## 📁 Step-by-Step Breakdown

### Step 1: Import Required Libraries

```py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
```

pandas: For data manipulation and analysis.

matplotlib.pyplot: For creating static visualizations (bar charts, etc.).

seaborn: Enhances matplotlib visuals with cleaner styles and additional features.

os: For interacting with the file system (used here to create directories).

### Step 2: Create Folder to Save Plots

```py
os.makedirs("plots", exist_ok=True)
```

- Creates a new folder named plots if it doesn't already exist.
- Ensures that charts/images generated during analysis are saved in an organized location.

### Step 3: Set the File Path

```py
file_path = r"C:\Users\user\OneDrive\Documents\street_energy_data.xls.xlsx"
```

- Specifies the absolute path to your Excel file containing street energy data.
- Update this to your local file path as needed.
- The r prefix means this is a raw string, so backslashes are treated literally.

### Step 4: Load the Excel File

```py
try:
df = pd.read_excel(file_path, engine='xlrd') # for .xls
except:
df = pd.read_excel(file_path, engine='openpyxl') # fallback for .xlsx
```

Tries to read the Excel file using the xlrd engine (used for .xls files).

If that fails (e.g., it's an .xlsx file), it uses openpyxl instead.

The result is a DataFrame called df containing the dataset.

### Step 5: Set Style for Plots

```py
sns.set(style="whitegrid")
```

Applies a white grid background to all seaborn/matplotlib plots for better readability.

#### ✅ TASK 1: Average Energy Consumption per Street

```py
avg_energy_per_street = df.groupby("Street ID")["Energy Consumption (kWh)"].mean().sort_values(ascending=False)
```

- groupby("Street ID"): Groups the data based on each unique street.

- ["Energy Consumption (kWh)"].mean(): Calculates the average energy usage for each street.

- sort_values(ascending=False): Sorts the results from highest to lowest average consumption.

```py
print("Average Energy Consumption per Street:\n", avg_energy_per_street)
```

- Prints the sorted list of average energy usage per street to the console.

### 📊 Plot Average Energy Consumption

```
plt.figure(figsize=(10, 6))
avg_energy_per_street.plot(kind="bar", color="skyblue")
plt.title("Average Energy Consumption per Street")
plt.ylabel("Energy Consumption (kWh)")
plt.xlabel("Street ID")
plt.tight_layout()
plt.savefig("plots/avg_energy_per_street.png")
plt.show()
```

- Creates a bar chart of the average energy usage per street.

- Labels axes and title.

- Saves the chart as a PNG in the plots directory.

- Displays the chart on screen using plt.show().

### ✅ TASK 2: Find Brightest and Darkest Streets

```py
avg_light = df.groupby("Street ID")["Light Intensity (Lux)"].mean()
```

- Groups the dataset by Street ID and calculates the average light intensity in Lux for each.

```py
brightest_street = avg_light.idxmax()
darkest_street = avg_light.idxmin()
```

- idxmax(): Finds the street ID with the highest average brightness.

- idxmin(): Finds the street ID with the lowest average brightness.

```py
print(f"Brightest Street: {brightest_street}")
print(f"Darkest Street: {darkest_street}")
```

- Displays the brightest and darkest streets in the dataset.

### ✅ TASK 3: Simulate Energy Saving with 20% Dimming

```py
df["Optimized Energy (kWh)"] = df["Energy Consumption (kWh)"] \* 0.8
```

- Creates a new column where each energy consumption value is reduced by 20%, simulating dimming lights.

original_total = df["Energy Consumption (kWh)"].sum()
optimized_total = df["Optimized Energy (kWh)"].sum()

Calculates total energy consumed before and after optimization.

print(f"\nOriginal Total Energy: {original_total:.2f} kWh")
print(f"Optimized Total Energy (with 20% dimming): {optimized_total:.2f} kWh")

Prints both totals for comparison, showing how much energy would be saved with the proposed optimization.

📁 Output Files

plots/avg_energy_per_street.png: Bar chart visualizing average energy consumption across streets.

📌 Notes

Ensure the Excel file path is valid on your system.

Required Python libraries:

pandas

matplotlib

seaborn

openpyxl and/or xlrd

You can install missing libraries using:

pip install pandas matplotlib seaborn openpyxl xlrd

✅ Summary

This script helps city planners or energy analysts:

Understand which streets use the most energy.

Identify underlit or overlit areas.

Simulate and evaluate the benefits of dimming streetlights.
