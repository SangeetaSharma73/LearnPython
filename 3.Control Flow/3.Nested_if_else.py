#Nested if else

# if condition1:
#     if condition1.1:
#         print('1.1 statement')
#     else:
#         print('if condition false')
# else:
#     print('if not true')


age=23
if age>18:
    if age>=65:
        print('you are eligible but too old')
    else:
        print('You are not too old and eligible to vote')
else:
    print('you are not adult for vote')   