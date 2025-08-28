students = [ 
    {"No": 1, "Name": "Aarav", "Age": 12, "Class": "7A", "Favourite Subject": "Maths"}, 
    {"No": 2, "Name": "Ananya", "Age": 13, "Class": "7B", "Favourite Subject": "Science"}, 
    {"No": 3, "Name": "Rohan", "Age": 12, "Class": "7A", "Favourite Subject": "English"}, 
    {"No": 4, "Name": "Priya", "Age": 13, "Class": "7B", "Favourite Subject": "History"}, 
    {"No": 5, "Name": "Vivaan", "Age": 12, "Class": "7A", "Favourite Subject": "Art"}, 
    {"No": 6, "Name": "Ishita", "Age": 13, "Class": "7B", "Favourite Subject": "Geography"}, 
    {"No": 7, "Name": "Karan", "Age": 12, "Class": "7A", "Favourite Subject": "Maths"}, 
    {"No": 8, "Name": "Meera", "Age": 13, "Class": "7B", "Favourite Subject": "Science"}, 
    {"No": 9, "Name": "Dev", "Age": 12, "Class": "7A", "Favourite Subject": "English"}, 
    {"No": 10, "Name": "Sneha", "Age": 13, "Class": "7B", "Favourite Subject": "History"}, 
    {"No": 11, "Name": "Aditya", "Age": 12, "Class": "7A", "Favourite Subject": "Art"}, 
    {"No": 12, "Name": "Riya", "Age": 13, "Class": "7B", "Favourite Subject": "Geography"}, 
    {"No": 13, "Name": "Siddharth", "Age": 12, "Class": "7A", "Favourite Subject": "Maths"}, 
    {"No": 14, "Name": "Nandini", "Age": 13, "Class": "7B", "Favourite Subject": "Science"}, 
    {"No": 15, "Name": "Yash", "Age": 12, "Class": "7A", "Favourite Subject": "English"}
] 

print("First Student detail: ", students[0])

for student_data in students:
    if student_data["Class"]=="7A":
        print(f"No: {student_data['No']}, Name: {student_data['Name']}, Age: {student_data['Age']}, Class: {student_data['Class']}, Favourite Subject: {student_data['Favourite Subject']}")