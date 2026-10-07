import maths 
from collections import deque 


marks=[1,2,3,4,5]


# accessing element O(1)
print(marks[0])
print(marks[-1]) # accessing last element 

# Inserting element  O(1)
marks.append(10) # append at last 
#append at specific location
marks.insert(2,55) # 2nd position (index =2 ) pe 55 append krdo all elements will be shifted to right after 2nd

marks.pop () # to remove last element
marks.pop(1) # to remove element at indx 1 
marks.remove(5) # remove this element 

######## Slicing
            #  sequence[start : stop : step]
            #              │      │      │
            #              │      │      └── jump/direction
            #              │      └───────── excluded
            #              └──────────────── included

marks[::-1]  # all tuples in reverse order as direction is -1 move backwards

######## Traversal 

# range(start, stop, step)
#        │      │      │
#        │      │      └── jump
#        │      └───────── excluded
#        └──────────────── included


for i in range (len(marks)):
    print(marks[i])

for mark in marks:
    print(mark)


########### Two pointer 
def two_pointer(numbers,target):
    left=0
    right=len(numbers)-1

    while left < right:
        total+=numbers[left] + numbers[right]

        if total==target : 
            return 1
        elif total>target :
            right=right-1
        else :
            left = left+1


######### Sorting 
numbers=[8,3,5,6,1,3,]
numbers.sort()
a=numbers.sort()
print(a)
print(numbers)


l=[1,3,5,2,7]

a=l
print(a) # 1,3,5,2,7


l.sort()
print(l) # 1,2,3,5,7

b=l
print(b) #1,2,3,5,7


######## Convert no to string and vice-versa 
n=123
s=str(n)
print(s) # '123'

s='123'
n=int(s)
print(n)# 123