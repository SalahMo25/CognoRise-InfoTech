#Calculator
def calculation():
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    print('Choice from this Operation')
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    
    choice = input(f'Enter your choice from this Operation => 1 , 2 , 3 or 4 : ')
    
    if choice == '1':
        result = num1 + num2
        print(f'\n {num1} + {num2} = {result}')
    elif choice == '2':
        result = num1 - num2
        print(f'\n {num1} - {num2} = {result}')
    elif choice == '3':
        result = num1 * num2
        print(f'\n {num1} * {num2} = {result}')
    elif choice == '4':
        if num2 == 0:
            print('Cannot divide by zero.')
        else:
            result = num1 / num2
            print(f'\n {num1} / {num2} = {result}')
    else:
        print('Invalid choice. Please try again.')
        
        
calculation()

   