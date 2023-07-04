print("Welcome to ABC Bank\n\nInsert your Card")
password = 1234
balance = 1000
choice = 0
pin = int(input("Enter your four digits pin\n"))

if pin == password:
    while choice != 4:

        print("**** MENU ****")
        print("1 == Balance")
        print("2 == Deposit")
        print("3 == Withdraw")
        print("4 == Cancel")
        choice = int(input("\nEnter your option:\n"))
        if choice == 1:
            print("Balance = ₹", balance)
        elif choice == 2:
            dep = int(input("Enter your deposit: ₹"))
            balance += dep
            print("\nDeposited amount: ₹", dep)
            print("Balance: ₹", balance)

        elif choice == 3:
            wit = int(input("Enter the amount to withdraw: ₹"))
            balance -= wit
            print("\nWithdrawn amount: ₹", wit)
            print("Balance: ₹", balance)

        elif choice == 4:
            print("\nSession Ended!! Good Bye.")
        else:
            print("\nInvalid Entry!!")



else:
    print("Pin Incorrect!! Try again.")

