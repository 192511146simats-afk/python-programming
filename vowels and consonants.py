

Vowel and consonant

s=input("enter the string:")
vcount=0
ccount=0
vowel="AaEeIiOoUu"
v=[]
c=[]
for ch in s:
    if ch in vowel:
        vcount+=1
        v.append(ch)
    elif(ch.isalpha() and ch not in vowel):
        ccount+=1
        c.append(ch)
print ("total number of vowel and consonant are:")
print(vcount,v)
print(ccount,c)