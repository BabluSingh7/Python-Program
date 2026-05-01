#Q1
'''
s = input("Enter a String:")
print("Print Corresponding Unicode:")
for u in s:
    print(u,"=",ord(u))

#Q2
s = input("Enter a String:")
print("Print only Vowels:")
for v in s:
    if v in 'aeiouAEIOU':
      print(v)

      
#Q3
s = input("Enter a String:")
print("count Corresponding Spaces:")
count =0
for u in s:
    if u in " ":
     count +=1
print(count)

'''
#Q4
s=input("Enter a number:  ") #s='123234'
u=''
for ch in s:
    if ch not in u:
        u+=ch  
print(u)


#Q5
n=int(input("Enter a number: "))
count=0
for ch in str(n):
    if ch in "0123456789":
        count+=1
print(count)