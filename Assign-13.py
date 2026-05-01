#Q1
n=int(input("Enter three digit number"))
if n>99 and n<1000:
    print("three digit numbers")
else:
    print("Not three digit numbers")

#Q2
num = int(input("Enter a number:"))
if num > 0:
    print("Positive number")
elif num<0:
    print("Negative Number")
else:
    print("Zero")

#Q3
a,b,c=int(input("Enter the value a,b and c")),int(input()),int(input())
d = b**2-4*a*c
if d>0:
    print("real & Distinct root")
elif d<0:
    print('Imagenary roots')
elif d==0:
    print("Roots are equal")

#Q4
year = int(input("Enter a year"))
print("Leap Year" if year%400==0 or (year%100!=0 and year%4==0) else "Non Leap Year")

"""
if year%100==0:
    if year%400==0:
        print("Leap year")
    else:
        print("Non Leap Year")
else:
    if year%4==0:
        print("Leap year")
    else:
        print("Non Leap Year")
"""

#Q5
print("Enter three numbers")
a,b,c=int(input()),int(input()),int(input())

print(a if a>c else c if a>b else b if b>c else c)
            
"""
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if b>c:
        print(b)
    else:
        print(c)
"""


