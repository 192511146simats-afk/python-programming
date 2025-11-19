numbers=list(map(int,input("enter the numbers seperated by spaces:").split()))
numbers.sort
#find mean
mean=sum(numbers)/len(numbers)
#median
n=len(numbers)
if(n%2==0):
    median=(numbers[(n//2)-1]+numbers[n//2])/2
else:
    median= numbers[n//2]
#find mode
mode=max(numbers, key=numbers.count)
#display result
print("mean=",mean)
print("median=",median)
print("mode=",mode)