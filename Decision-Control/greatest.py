''' Write a python script to find greatest among three numbers '''

num1= eval(input("Enter first Number: "))
num2= eval(input("Enter second Number: "))
num3= eval(input("Enter third Number: "))

if num1>num2 and num1>num3:
    print("%d is greatest"%num1)
elif num2>num1 and num2>num3:
    print("%d is greatest"%num2)
else:
    print("%d is greatest"%num3)