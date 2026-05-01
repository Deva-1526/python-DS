#2nd sum
def students(S):
    total=0
    top_marks = 0
    top_name=" "
    print("Passed students:")
    for name,marks in S:
        if marks>=50:
            print(name)
    
        total= total+marks
        if marks > top_marks:
            top_marks = marks
            top_name= name
    avg = total/len(S)
    print("Average:",avg)
    print("Topper:",top_name)
    
S=[("A",85),("B",40),("C",72),("D",30)]
students(S)

#5th sum
def rotated_sorted_array(arr):
    f=arr[0]
    for i in range(len(arr)):
        f=arr[3:]+arr[:3]
    return f
l=[4,5,6,1,2,3]
print(rotated_sorted_array(l))

#3rd sum
def Ecommerce(cart,prices):
    total=0
    for i in cart:
        total += cart[i] * prices[i]
    print("Total amount:",total)
    if total>100:
        discount = total*0.10
        total = total-discount
        print("discounts:",discount)
    print("Final Amount:",total)
cart = {"apple":2,"banana":3,"milk":1}
prices = {"apple":50,"banana":20,"milk":60}
Ecommerce(cart,prices)

#4th sum
def password_checker(password):
    if len(password) < 8:
            print("weak")
            return
    upper=0
    lower=0
    digit=0
    special=0
    for i in password:
        if i >='A' and  i <='Z':
            upper =1
        elif i >='a' and  i <='z':
            lower = 1
        elif i>= '0' and i<= '9':
            digit = 1
        else:
            special = 1

    if upper ==1 and  lower == 1 and digit == 1 and special == 1:
        print("Strong")
    else:
        print("Weak")
a=input("Enter the password:")
password_checker(a)
























    























