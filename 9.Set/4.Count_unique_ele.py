#count no of unique elements in the sentence
sent='be the change you wish to see in the world'
print(len(set(sent)))#unique letters

lst=sent.split()
print(len(set(lst)))

#code
sent='be the change you wish to see in the world'
#unique word list
lst=sent.split()
#convert into set
s=set(lst)
print(len(s))