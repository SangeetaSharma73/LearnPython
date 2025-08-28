import pandas as pd

file_path = r"C:\Users\user\OneDrive\Desktop\Book1.csv"

data = pd.read_csv(file_path)
# print(data)
# print(data.to_string())
# print(data.isnull())
# print(data.dropna())
new_data =  data[(data['Age']>10)  (data['Age']<15)]
print(data)