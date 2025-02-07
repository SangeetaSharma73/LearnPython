# Input:
# arr1 = [1, 2, 3, 4, 5,12,9,20]
# arr2 = [3, 4, 5, 6, 7,]
arr1 = [1, 2, 3, 4, 5,8,9,7]
arr2 = [3, 4, 5, 6, 7]

# Output:
# [3, 4, 5]

ansArr =[]
for i in range(len(arr1)):
    if arr1[i] in arr2:
        ansArr.append(arr1[i])
print(ansArr)

