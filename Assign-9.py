#Q1

p=int(input("Enter the principal amount: "))
r=int(input("Enter the rate of interest: "))
t=int(input("Enter the time period: "))
si = (p*r*t)/100
print("the simple interest is :",si)

#Q2
rectangle_length = int(input("Enter the length of the rectangle: "))
rectangle_breadth = int(input("Enter the breadth of the rectangle: "))
area_rectangle = rectangle_length * rectangle_breadth
print("The area of the rectangle is:", area_rectangle)


#Q3
num1,num2,num3 = map(int, input("Enter three numbers: ").split())
avg = (num1 + num2 + num3) / 3
print("The average of the three numbers is:", avg)

#Q4
l,w,h= int(input("Enter the  length width height cube: ")),int(input()),int(input())
volume = l * w * h
print("The length of the side of the cube is:",volume)

#Q5
x,y=int(input("Enter two numbers: ")),int(input())
print("power of the first number to the second number is:=",x**y)