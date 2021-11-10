x = int(input("enter a number"))
y = x
sum = 0
while(y>0):
    rem = y%10
    y = y//10
    sum = sum+rem
if(x==sum):
    print("perfect number")
else:
    print("not a perfect number")
