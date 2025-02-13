fuel = int(input())
distance = int(input())

required= fuel*distance
if required>50:
    print('Enough')
else:
    print('Go On')