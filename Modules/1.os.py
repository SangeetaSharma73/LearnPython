'''
1. os
Purpose: Interact with the operating system.
Key Features:
Manipulate directories and files (create, delete, rename).
Access environment variables.
Execute system commands.
'''

import os
# os.mkdir('new_folder')  # Create a new directory
print(os.getcwd())      # Get the current working directory


'''
2. sys
Purpose: Access system-specific parameters and functions.
Key Features:
Command-line arguments.
Exit Python script.
Access Python path and other interpreter-related settings.
'''

import sys
print(sys.argv)  # Command-line arguments as a list
# sys.exit()       # Exit the script


'''
3. math
Purpose: Perform mathematical operations.
Key Features:
Trigonometric functions.
Logarithmic functions.
Constants like π (pi) and e (Euler's number).
'''

import math
print(math.sqrt(16))      # Square root
print(math.pi)            # Value of pi


'''
4. random
Purpose: Generate random numbers.
Key Features:
Generate random integers, floats, and choices from a sequence.
Shuffle lists.
Random sampling without replacement.
'''

import random
print(random.randint(1, 10))    # Random integer between 1 and 10
my_list = [1, 2, 3, 4]
random.shuffle(my_list)        # Shuffle the list


'''
5. datetime
Purpose: Work with dates and times.
Key Features:
Create, manipulate, and format dates and times.
Perform date arithmetic (add/subtract time intervals).
Retrieve the current date/time.
'''

import datetime
now = datetime.datetime.now()
print(now)  # Current date and time
delta = datetime.timedelta(days=5)
print(now + delta)  # Add 5 days to the current date


'''
6. json
Purpose: Parse and manipulate JSON data.
Key Features:
Convert Python objects to JSON format.
Parse JSON strings into Python dictionaries and lists.
'''
import json
data = {'name': 'Alice', 'age': 25}
json_string = json.dumps(data)  # Convert dictionary to JSON string
print(json_string)
parsed_data = json.loads(json_string)  # Parse JSON string back to Python dict
print(parsed_data)

'''
7. re
Purpose: Perform regular expression matching.
Key Features:
Match, search, and replace text using regular expressions.
Split strings based on patterns.
Validate inputs (emails, phone numbers, etc.).
'''

import re
pattern = r'\d+'  # Matches any sequence of digits
result = re.findall(pattern, 'My phone number is 12345')
print(result)  # ['12345']


'''
8. collections
Purpose: Specialized container datatypes.
Key Features:
Counter: Count elements in a collection.
deque: Fast appending and popping from both ends of a list.
namedtuple: Tuple with named fields.
'''

from collections import Counter
my_list = ['a', 'b', 'a', 'c', 'b', 'a']
count = Counter(my_list)
print(count)  # Output: Counter({'a': 3, 'b': 2, 'c': 1})



'''
10. pandas
Purpose: Data manipulation and analysis.
Key Features:
Data structures like DataFrame and Series for handling tabular and time-series data.
Import/export data from CSV, Excel, SQL, etc.
Operations like grouping, merging, and reshaping data.

'''

import pandas as pd
df = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})
print(df)


'''
11. numpy
Purpose: Perform numerical and scientific computations.
Key Features:
Support for large multi-dimensional arrays and matrices.
Mathematical operations over arrays (vectorization).
Linear algebra, Fourier transforms, and random number generation.
'''
import numpy as np
array = np.array([1, 2, 3, 4])
print(type(array))
print(array * 2)  # Element-wise multiplication

'''
12. flask
Purpose: Micro web framework for building web applications.
Key Features:
Simple routing and request handling.
Support for templates (HTML rendering).
Extensible with plugins for authentication, sessions, etc.

'''

'''from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run()
'''



'''
13. requests
Purpose: Send HTTP requests.
Key Features:
Simplifies making HTTP requests to web servers.
Support for GET, POST, PUT, DELETE requests.
Handle JSON responses, file uploads, and authentication.
'''
import requests
response = requests.get('https://api.github.com')
print(response.json())  # Parse the JSON response


'''
15. multiprocessing
Purpose: Parallelize tasks and execute code using multiple processes.
Key Features:
Spawn processes to run code concurrently.
Share data between processes.
Useful for CPU-bound tasks.
'''

import multiprocessing

def worker(num):
    print(f'Worker: {num}')

if __name__ == '__main__':
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()
