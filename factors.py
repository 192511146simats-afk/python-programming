x=int(input("enter the number to find factors:"))
y=[]
for i in range(1,x):
    if(x%i==0):
        y.append(i)
print(y)
print(x ," has ",len(y) ,"factors")
n=int(input("enter the N value:"))
if n>len(y):
    print("invalid")
else:
    for k in range(0,n):
        print(y[k])