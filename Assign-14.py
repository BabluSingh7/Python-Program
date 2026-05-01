#Q1
n=int(input("Enter a number"))
match n:
    case n if 1000>n>99:
        print("three digit number")
    case n:
        print("Not three digit number:")

#Q2
n=int(input("Enter a number:"))
match n:
    case n if n>0:
        print("Positive number")
    case n if n<0:
        print("Negative")
    case n if n==0:
        print("Zero")

#Q3
print("Enter a number:\n1.Odd Even :\n2.Positive Non positive:\n3.Simple interst:\n4.find roots of quadratic equestion:")
x=int(input())
match x:
    case x if x==1:
        n=int(input("enter a number:"))
        if n%2==0:
            print("Even number:")
        else:
            print("Odd number")
    case x if x==2:
        n=int(input("enter a number:"))
        if n>0:
            print("Positive:")
        else:
            print("non positive")
    case x if x==3:
        p,r,t=int(input("Enter princple rate and time")),int(input()),int(input())
        si=(p*r*t)/100
        print("SI is = ",si)
    case x if x==4:
        a,b,c=int(input("Enter the value a,b and c")),int(input()),int(input())
        d = b**2-4*a*c
        if d>0:
          print("real & Distinct root")
        elif d<0:
          print('Imagenary roots')
        elif d==0:
          print("Roots are equal")

#Q4
x=eval(input("Enter same data"))
match x:
    case x if type(x)==int:
        print("Monday")
    case x if type(x)==float:
        print("Tuesday")
    case x if type(x)==complex:
        print("Wednesday")
    case x if type(x)==bool:
        print("thursday")

#Q5
x=eval(input("Enter same data"))
match x:
    case x if x in "mysirg":
        print("one")
    case x if x in "education":
        print("Two")
    case x if x in "services":
        print("three")
    case x if type(x)==bool:
        print("thursday")



