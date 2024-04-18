d={1:4,5:1,4:3}
for key in d:
    print(key,d[key])
   

#using dict.items() 
for key,val in d.items():
    print(key,val)
    
    
#methods of dictionary

print(d.keys())

print(d.values())

print(d.items())


d={}
arr=[1,4,5,6,4,3,4,3]
#dictionary-frequency
for k in range(len(arr)):
    if arr[k] not in d:
        d[arr[k]]=1
    else:
        d[arr[k]]+=1
print(d)