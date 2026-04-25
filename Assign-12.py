#Q1
n=int(input("Enter a number:"))
if n>0:
    print("positive")
else:
    print("non positive")

#Q2
n=int(input("Enter a number:"))
if n%5==0:
    print("Divisble by 5")
else:
    print("not divisble by 5")

#Q3
n = int(input("Enter a number"))
if n%2==0:
    print("Even number",n)
else:
    print("Odd number",n)

#Q4
a,b=int(input("Enter two number:")),int(input())
if a>b:
    print("A is grater")
elif a<b:
    print("B is grater")
else:
    print("A and B both are same")

#Q5
w1,w2=input("Enter two word"),input()
if(w1<w2):
    print(w1,w2)
else:
    print(w2,w1)

