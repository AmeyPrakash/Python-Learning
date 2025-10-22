pin = "1234"
balance = 6000.0
enetered_pin = input("Enter Your PIN: ")
if enetered_pin == pin:
    while True:
        print("\nATM MENU")
        print("\n1.Check Balance")
        print("\n2.Withdraw Money")
        print("\n3.Deposit Money")
        print("\n4.Exit")

        choice = input("Choosr an option (1-4):")
        
        if choice == "1":
            print(f"Your current balance is: ${balance:.2f}")


        elif choice == "2":


            amount = float(input("Enter amount to Withdraw: $"))
            if amount > balance:
                print("Insufficient balance!")
            elif amount > 0:
                balance -= amount
                print(f"Please collect your cash new balance is: ${balance:.2f}")
            else:
                print("Invalid amount!")

        elif choice == "3":


            amount = float(input("Enter amount to Deposit: $"))
            if 0 < amount:
                balance += amount
                print(f"Amount deposited successfully! New balance is : ${balance:.2f}")
            else:
                print("Invalid amount!")


        elif choice == "4":

            print("Thank you for using the ATM. Goodbye!")
            break       
        else:
            print("Invalid choice! Please slect a valid option.")
else:
        print("Incorrect PIN. Access denied.")
