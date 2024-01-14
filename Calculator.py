#Fuctions
def add(x,y):
    return x + y
def subtraction(x,y):
    return x - y
def multiplication(x,y):
    return x * y
def divide(x,y):
    if y == 0:
        print("Error! Cannot be Divide by zero")
    else: return x / y

#Selections
print("Select Operation")
print("1 For Addition 2 For Subraction 3 For Multiplication 4 For Divide")

#Calculation Loop
while True:
    try:
        choice = input("Enter choice(1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        else:
            print("Invalid. Select number between 1 and 4.")
            break
        
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtraction(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiplication(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        else:
            print("Error")
            break

        next = input("continue calculation? (y/n): ")
        if next == 'n':
            print("Exiting the calculator")
            break

        else: next == 'y'
        print("Continue the calculator")
       
    except ValueError as e:
        print(e)
        break