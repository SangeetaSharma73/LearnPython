import os

def find_project(root_dir, keyword):
    for root, dirs, files in os.walk(root_dir):
        for name in dirs + files:
            if keyword.lower() in name.lower():
                print(os.path.join(root, name))

find_project("C:\\", "temperature")  # Replace with your keyword