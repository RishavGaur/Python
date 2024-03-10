''' Write a python script to calculate simple interest, 
 data required should be taken from user. '''

p= eval(input("Enter Principle Amount: "))
r= eval(input("Enter Rate of Interest: "))
t= eval(input("Enter Period of Time(in Years): "))

print("Simple Interest=",(p*r*t)/100)