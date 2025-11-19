n=int(input("enter the number of elements in the array:"))
arr=[]
print("enter the elements")
for i in range(n):
    arr.append(int(input()))
max = secmax = -10**9
for x in arr:
    if x > max:
        secmax= max
        max=x
    elif x > secmax and x!=max:
        secmax=x
print("largest=",max," secondlargest=",secmax)