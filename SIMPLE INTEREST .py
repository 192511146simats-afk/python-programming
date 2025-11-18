p=int(input("enter the principal amount:"))
n=int(input("enter the number of years:"))
sc=input("enter Y for yes or N no:")
gender=input("enter M for male or F for female:")
if sc=='Y':
    SI=p*n*12/100
   
elif sc=='Y' and gender =='F':
    SI=p*n*15/100
  
else :
    SI=p*n*10/100
print(SI)