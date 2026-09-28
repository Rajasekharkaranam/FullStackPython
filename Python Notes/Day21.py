#123ATM Project Code
balance = 10000
correct_pin = 1234

pin = int(input("Enter your PIN: "))

if pin == correct_pin:
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Available Balance:", balance)

        elif choice == 2:
            amount = float(input("Enter withdrawal amount: "))

            if amount <= balance:
                balance -= amount
                print("Please collect your cash.")
                print("Remaining Balance:", balance)
            else:
                print("Insufficient balance.")

        elif choice == 3:
            amount = float(input("Enter deposit amount: "))
            balance += amount
            print("Amount deposited successfully.")
            print("Updated Balance:", balance)

        elif choice == 4:
            print("Thank you for using the ATM!")
            break

        else:
            print("Invalid choice.")

else:
    print("Incorrect PIN.")