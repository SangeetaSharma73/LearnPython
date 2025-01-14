#the elif condition is used to include multiple conditional expressions after the if condition

# if condition1:
#     print('conditon1 is true')
# elif condition2:
#     print('condition2')
# elif condition3:
#     print('condition3')
# else:
#     print('No if elif conditions are true')

num=23
if num>0:
    print('Positive')
elif num==0:
    print('zero')
else:
    print('Negative')

#Find maximum in a list

Riya=24
sapna=50
Geeta=34
if Riya>sapna and Riya>Geeta:
    print('Riya is topper')
elif sapna>Riya and sapna>Geeta:
    print('Sapna is topper')
else:
    print('Geeta is topper')


#Grading problem
marks=90
if marks>=90 and marks<=100:
    print('A grade')
elif marks>=80 and marks<90:
    print('B grade')
elif marks>=70 and marks<=80:
    print('C grade')
elif marks>=60 and marks<70:
    print('D grade')
elif marks<60:
    print('E grade')
else:
    print('Fail')