balance = 2000

def check_balance():
    print("Your current balance is: PHP " + str(balance))

def withdraw(amount):
    if amount > balance:
        print("Insufficient funds.")
    else:
        balance -= amount
        print("Withdraw successful. Your current balance is: PHP " + str(balance))

def deposit(amount):
    balance += amount
    print("Deposit successful. Your current balance is: PHP " + str(balance))

def main():
    while True:
        print("\nPhilippine ATM Machine:")
        print("[1] Check Balance")
        print("[2] Withdraw")
        print("[3] Deposit")
        print("[4] Quit")
        
        choice = int(input("Enter a number: "))
        
        if choice == 1:
            check_balance()
        elif choice == 2:
            amount = float(input("Enter your withdrawal amount: PHP "))
            withdraw(amount)
        elif choice == 3:
            amount = float(input("Enter your deposit amount: PHP "))
            deposit(amount)
        elif choice == 4:
            print("Thank you for using Philippine ATM Machine.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
