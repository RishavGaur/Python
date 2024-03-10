''' Write a python script to check if a year is leap year or not. '''

year= int(input("Enter an Year: "))

if year%4==0 and year%100!=0:
    print("It's Leap Year")
elif year%400==0 and year%100==0:
    print("It's a Leap Year")
else:
    print("Not a Leap Year")