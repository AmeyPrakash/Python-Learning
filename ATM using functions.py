def check_pin(correct_pin):
    enetered_pin = input("Enter Your PIN:")
    if enetered_pin == correct_pin:
        return True
    else:
        print("Incorrect PIN. Access denied.")
        return False

def show_menu():
    print("\nATM MENU")
    print("1. Check Balance")
    print("2. Deposited Money")
    print("3. Withdraw Money")
    print("4. Exit")

def check_balance(balance):
    print(f"Your current balance is: ${balance:.2f}")

def deposit_money(balance):
    try:
        amount = float(input("Enter the ammount to Deposit: $"))
        if amount > 0:
            balance += amount
            print(f"{amount:.2f}deposited successfully! New balance is: ${balance:.2f}")

        else:
            print("Inavalid amount!")
    except ValueError:
        print("Invalid Input! Please enter a numeric value.")
    return balance
    

def withdraw_money(balance):
    try:
        amount = float(input("Enter amount to be withdrawn: $"))
        if amount <= 0:
            print(" Invalid amount!")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            
            print(f"{amount:.2f}Withdrawn successfully! Please collect your cash. New balance is: ${balance}")
    except ValueError:
        print("Invalid Input! Please enter a numeric value.")
    return balance 

def atm_system():
    pin = "1234"
    balance = 7000.0

    if not check_pin(pin):
        return
    
    while True:
        show_menu()
        choice = input("CHoose an otpion (1-4):")
        if choice == "3":
            balance = withdraw_money(balance)
        elif choice == "2":
            balance = deposit_money(balance)
        elif choice == "1":
            check_balance(balance)
        elif choice == "4":
            print("Thank you for using the ATM. GoodBye!")
            break
        else:
            print("Invalid choice! Please select a valid option.\n")

atm_system()            

                                   