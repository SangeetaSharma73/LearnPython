#Break,continue and pass
#These statements are used to alter the flow of a program
#break- Breaks the flow of program once this condition is hit
#COntinue- it skips that particular iteration
#Pass-to avoid syntax error
# def fun():
#     pass 
for i in range(1,10):
    # it will give indented error if we didn't write anything 
    pass
#Continue
for i in range(1,5):
    if i==3:
        continue
    print(i)
#break
for i in range(1,5):
    if i==2:
        break
    print(i)