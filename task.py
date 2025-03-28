#check if number is even or odd
for i in range(1,16):
    if i % 2 == 0:
        print("the number is even",i)
else:
    print("the number is odd",i)
#looping through numbers 1 to 5
for i in range(1,6): 
    print(i)  
#calculator
number1 = float(input("enter number : "))
number2 = float(input("enter nuber : "))
#ask user for operation
operation = input("choose a desired operator(*, -, +, /,): ")
#perform coressponding operation
if operation == "+":    
    output = number1 + number2
elif operation == "-":
    output = number1 - number2
elif operation == "/":
    output = number1 / number2
elif operation == "*":
    output = number1 * number2
    if number2 != 0: 
        print("valid")
    else:
        output = "error"
    elif operation == "*":
        output = number1 * number2
    else:
      output= "operation chosen is nt valid"
    print ("output:", output)
except valueError:           
    print("invalid input! enter valid number") 
