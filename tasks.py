'''#1st
def  remove_duplicates(arr):
    a=[]
    for i in arr:
        if i not in a:
             a.append(i)
    return a
       
l=[4,4,4,4]
print(remove_duplicates(l))'''

'''#2nd
def left_rotate_by_one(arr):
    f=arr[0]
    for i in range (len(arr)-1):
        f=arr[1:]+arr[:1]
    return f
l=[1,2,3,4]
print(left_rotate_by_one(l))'''

'''#3rd
def left_rotate(arr, k):
    f=arr[0]
    for i in range(len(arr)):
        f=arr[2:]+arr[:2]
    return f
l=[1,2,3,4,5]
k=2
print(left_rotate(l,k))

#4th
def is_sorted(arr):
   for i in range(len(arr)-1):
       if i in arr:
           arr[i]>arr[i+1]
           return False
   return True
l=[2,3,1]
print(is_sorted(l))

#5
s=input("Enter the string:")
count=0
for i in s:
    if i in "aeiou":
        count+=1
print(count)

#6th
def count_even_odd(arr):
    even=0
    odd=0
    for i in range(len(arr)):
        if i%2==0:
            even+=1
        else:
            odd+=1
    return(even,odd)
l=[1,2,3,4,5,6]
print(count_even_odd(l))

#7
def unique_elements(arr1,arr2):
    a=[]
    for i in arr1:
        if i not in arr2:
            a.append(i)
    for i in arr2:
        if i not in arr1:
            a.append(i)
    return a
a=[1,2,3]
b=[3,4,5]
print(unique_elements(a,b))

#8
def intersection(arr1,arr2):
    a=[]
    for i in arr1:
        if i  in arr2 and i not in a:
            a.append(i)
    return a
a=[4,9,5]
b=[9,4,9,8,4]
print(intersection(a,b))'''

#10
def find_min_max(arr):
    a=arr[0]
    b=arr[0]
    for i in range(len(arr)):
        if arr[i]<a:
            a=arr[i]
        if arr[i]>b:
            b=arr[i]
    return a,b
l=[3,5,1,8,2]
print(find_min_max(l))

    






















        
 
        
       















        
