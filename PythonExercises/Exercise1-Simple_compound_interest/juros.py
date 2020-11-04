print("-"*28)
print("Interest calculation program")
print("-"*28)

def printMessage():
    print(" - Enter (1) to calculate simple interest")
    print(" - Enter (2) to calculate compound interest")
    print(" - Enter (0) to exit the program")

printMessage()
op = int(input(">>> "))

while op != 0:
    if op == 1:
        print("\nSimple interest\n")
        principle = float(input("Enter the initial balance: "))
        interestRate = float(input("Enter the interest rate in months: "))
        time = int(input("Enter the time in months: "))

        interestRate /= 100 
        total = principle*(1+interestRate*time)
        interest = total - principle

        print(f'\nThe total amount is R$ {total:.2f}')
        print(f'The yield is: R$ {interest:.2f}')
        print("\n")
        
        printMessage()
        op = int(input(">>> "))
        
    elif op == 2:
        print("Compound interest\n")
        principle = float(input("Enter the initial balance: "))
        interestRate = float(input("Enter the interest rate in months: "))
        time = int(input("Enter the time in months: "))
        
        interestRate /= 100 
        total = principle*(1+interestRate)**time
        interest = total - principle
        
        print(f'\nThe total amount is R$ {total:.2f}')
        print(f'The yield is: R$ {interest:.2f}')
        print("\n")
        
        printMessage()
        op = int(input(">>> "))
        
    else:
        print("\nInvalid response\n")
        printMessage()
        op = int(input(">>> "))
        
print("\nEND OF PROGRAM")
