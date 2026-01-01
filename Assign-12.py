#Q-1 
n = int(input("Enter a number:"))
if n>0:
    print("Positive")
else :
    print("Non Positive")  

#Q-2
n = int(input("Enter a number"))
if n%5==0:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")

#Q-3
a=int(input("Enter a number"))
if a%2==0:
    print("Even",a)
else:
    print("Odd",a)
    
#Q4
a=int(input("Enter first number"))
b=int(input("Enter second number"))
print(a if a>b else b)

#Q5
w1=input("Enter first word")
w2=input("Enter second word")
if(w1<w2):
    print(w1,w2)
else:
    print(w2,w1)  