# Step 1: Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Step 2: Create Folder to Save Plots
os.makedirs("plots", exist_ok=True)

# Step 3: Set the File Path (Update this to your actual file path)
file_path = r"C:\Users\user\OneDrive\Documents\street_energy_data.xls.xlsx"  # or use .xlsx if needed

# Step 4: Load the Excel File
try:
    df = pd.read_excel(file_path, engine='xlrd')  # for .xls
except:
    df = pd.read_excel(file_path, engine='openpyxl')  # fallback for .xlsx

# Step 5: Set Style for Plots
sns.set(style="whitegrid")

# ✅ TASK 1: Average Energy Consumption per Street
# 1.groupby("Street ID"): Groups the data by each street. 
# 2. ["Energy Consumption (kWh)"].mean(): Calculates the average energy usage for each group. 
# 3.sort_values(ascending=False): Sorts the result from highest to lowest. 

avg_energy_per_street = df.groupby("Street ID")["Energy Consumption (kWh)"].mean().sort_values(ascending=False)
print("Average Energy Consumption per Street:\n", avg_energy_per_street)

# Plot Average Energy Consumption
plt.figure(figsize=(10, 6))
avg_energy_per_street.plot(kind="bar", color="blue")
plt.title("Average Energy Consumption per Street")
plt.ylabel("Energy Consumption (kWh)")
plt.xlabel("Street ID")
plt.tight_layout()
plt.savefig("plots/avg_energy_per_street.png")
plt.show()

# ✅ TASK 2: Find Brightest and Darkest Streets
avg_light = df.groupby("Street ID")["Light Intensity (Lux)"].mean()
brightest_street = avg_light.idxmax()
darkest_street = avg_light.idxmin()
print(f"Brightest Street: {brightest_street}")
print(f"Darkest Street: {darkest_street}")

# ✅ TASK 3: Simulate Energy Saving with 20% Dimming
df["Optimized Energy (kWh)"] = df["Energy Consumption (kWh)"] * 0.8
original_total = df["Energy Consumption (kWh)"].sum()
optimized_total = df["Optimized Energy (kWh)"].sum()
print(f"\nOriginal Total Energy: {original_total:.2f} kWh")
print(f"Optimized Total Energy (with 20% dimming): {optimized_total:.2f} kWh")
