num=int(input("enter the number:"))
s=str(num)
if len(s)%2!=0:
    print("it is not a tech number")
else:
    half=len(s)//2
    fh=int(s[ :half])
    sh=int(s[half: ])
    if (fh+sh)**2==num:
        print("it is a tech number")
    else:
        print("it is not a tech number")