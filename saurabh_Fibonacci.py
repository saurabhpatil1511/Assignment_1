n = int(input("Enter a number:"))
n1 = 0
n2 = 1
count = 0
if n <= 0:
    print("enter the positive numbers")
elif n == 1:
    print("fibonacci sequence upto", n,":")
    print(n1)
else:
    print("fibonacci sequence :")
    while count < n:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count+=1