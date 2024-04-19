#Intersection- when we want to find the common thing between two ar more than two things

python_students={"Siya",'Nrupul',"yogesh","Ritika"}
java_students={'Neha','Kirti','priya','Nrupul','yogesh'}
print(python_students.intersection(java_students))
print(java_students.intersection(python_students))


#union - when we want to find the item come either in 1st set or 2nd set or in both 
python_students={"Siya",'Nrupul',"yogesh","Ritika"}
java_students={'Neha','Kirti','priya','Nrupul','yogesh'}
print(python_students.union(java_students))

#difference- when we have to find out the set of students who have enrolled in python not in java course or vice-versa, then we can use the difference method
python_studentspython_students={"Siya",'Nrupul',"yogesh","Ritika"}
java_students={'Neha','Kirti','priya','Nrupul','yogesh'}
print(python_students.difference(java_students))
print(java_students.difference(python_students))