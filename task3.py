'''#Smart Attendance System
def Smart_Attendance_System(student):
    for name,time in student:
        if time <= 9.05 :
            print("Present:",name)      
student=[("adhi",9.00),("deva",9.02),("kalai",9.10),("sham",9.08)]
Smart_Attendance_System(student)'''

#E-commerce Discount Engine
def Ecommerce_Discount_Engine():
        if total>5000:
            discount = 0.20
        elif total>2000:
            discount = 0.10
        else:
            discount = 0   
        price=total*discount
        Final=total-price
        print("Total Amount:",total)
        print("discounts",price)
        print("Final Amount:",Final)

total=int(input("Enter the price:"))
Ecommerce_Discount_Engine()
