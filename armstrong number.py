n=int(input("enter the number:"))
sum=0
original=n
while n>0:
    digit=n%10
    sum=sum+digit**3
    n=n//10
if(sum==original):
    print("it is armstrong number")
else:
    print("it is not a armstrong number")