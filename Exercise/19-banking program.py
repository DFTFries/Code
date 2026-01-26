# Python banking program

def show_balance(balance):
    submenu = True
    while submenu:
        print("********************")
        print()
        print(f"Your balance is €{balance:.2f}")
        print()
        print("********************")
        print()
        exit = input("Press 0 to go back: ")
        print()
        match exit:
            case "0":
                submenu = False
            case _:
                print("Invalid Input")


def deposit():
    submenu = True
    while submenu:
        print("********************")
        print()
        amount = float(input("Enter an amount to be deposited: "))
        print()
        if amount < 0:
            print("That's not a valid amount.")
            print()
        else:
            print("********************")
            print()
            print(f"Deposited €{amount}")
            print()
            submenu = False
            return amount

def withdraw(balance):
    submenu = True
    while submenu:
        print("********************")
        print()
        amount = float(input("Enter amount to be withdrawn: "))
        print()
        if amount > balance:
            print("********************")
            print()
            print("You have insufficient funds.")
            print("Back to Main Menu")
            print()
            return 0
        elif amount < 0:
            print("********************")
            print()
            print("Amount must be greater than 0")
            print()
        else:
            print("********************")
            print()
            print(f"Withdrawn €{amount}")
            print()
            submenu = False
            return amount

def main():
    balance = 0
    is_running = True


    while is_running:
        print("********************")
        print()
        print("Banking Program")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print()
        print("********************")
        print()
        choice = input("Enter your choice (1-4): ")
        print()

        match choice:
            case "1":
                show_balance(balance)
            case "2":
                balance += deposit()
            case "3":
                balance -= withdraw(balance)
            case "4":
                is_running = False
            case _:
                print()
                print("********************")
                print()
                print("Invalid input!")
                print()

    print("********************")
    print()
    print("Thank you! Have a nice day!")
    print()
    print("********************")

if __name__ == "__main__":
    main()