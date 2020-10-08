while True:
    print("instructions:")
    print("     type 'add' and press enter to add two numbers")
    print("     type 'subtract' and press enter to subtract two numbers")
    print("     type 'multiply' and press enter to multiply two numbers")
    print("     type 'divide' and press enter to devide two numbers")
    print("     type 'quit' and press enter to end the program")
    print("                                                 ")
    user_input = input(": ")

    if user_input == "quit":
        break
    
    elif user_input == "add":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter a number: "))
        result = str(num1 + num2)
        print("the answer is " +  result)
    
    elif user_input == "subtract":
        num1 = float(input("enter a number: "))
        num2 = float(input("enter a number: "))
        result = str(num1-num2)
        print("the answer is " +  result)
        
    elif user_input == "multiply":
        num1 = float(input("enter a number: "))
        num2 = float(input("enter a number: "))
        result = str(num1*num2)
        print("the answer is " +  result)
        
    elif user_input == "divide":
        num1 = float(input("enter a number: "))
        num2 = float(input("enter a number: "))
        result = str(num1/num2)
        print("the answer is " +  result)
    
    else:
         print("unknown input, make sure to enter only numbers")
         
