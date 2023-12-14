import math
Name=input("Enter your name: ")
family=input("Enter your family: ")
score1=float(input("Enter score1: "))
score2=float(input("Enter score2: "))
score3=float(input("Enter score3: "))
avg=(score1+score2+score3)/3
print(avg)
if avg<=12:
   print("failed")
elif 12<=avg>=17:
 print("good")
elif avg>17: 
 print("perfect")
print("you are with",avg,"average")