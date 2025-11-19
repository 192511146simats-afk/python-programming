for n in range(1000,10000):
    s=str(n)
    half=len(s)//2
    fh=int(s[:half])
    sh=int(s[half:])
    if (fh+sh)**2==n:
        print(n)
    