'''Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
'''

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''b = []
for x in a: #for each element((x) in the list a
 if x%2 == 0: #even numbers go by 2 with 0 remainder  
  b.append(x) #appending elements to list b
print(b)
'''

b = [x for x in a if x%2 == 0 ]
print(b)