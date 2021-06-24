#calculate factorial of a number (First enter a input, then calculate factorial of a number and print it.)

number = int(input("Please enter a number: "))
factorial = 1

while number<0:
   print("Please enter a positive number or zero: ")
   number = int(input("Please enter a number: "))
   
if number == 0:
   factorial = 1
   
elif number>0:
   for i in range(number,0,-1): #range(1,10,3)
      factorial *= i # factorial = factorial * i
      
print(f"{number}! = {factorial}")