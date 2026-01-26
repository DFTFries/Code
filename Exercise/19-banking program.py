# Python banking program

def show_balance(balance):
    print("********************")
    print(f"Your balance is ${balance:.2f}")
    print("********************")


def deposit():
    print("********************")
    amount = float(input("Enter an amount to be deposited: "))
    print("********************")

def withdraw():
    print("********************")
    withdrawal = float(input("Enter the amount you'd like to withdraw: "))
    print("********************")


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


    choice = input("Enter your choice (1-4): ")
    match choice:
        case "1":
            show_balance()
        case "2":
            deposit()
        case "3":
            withdraw()
        case "4":
            is_running = False
        case _:
            print()
            print("********************")
            print()
            print("Invalid input!")
            print()


print("Thank you! Have a nice day!")
