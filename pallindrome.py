s=input("enter the string:")
s=s.lower()
rev=s[::-1]
if s==rev:
    print("it is a palindrome")
else :
    print("it is not a palindrome")