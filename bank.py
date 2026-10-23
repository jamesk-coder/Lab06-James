# Part 1 - a menu-driven text interface (TUI) for a simple "piggy bank".
#
# This is a terminal program: it shows a menu, reads a choice, does something, and
# loops until the user quits. The menu loop is written for you - fill in the three
# TODO branches. Keep the exact wording shown (the tests look for it).

def main():
    balance = 0.0
    while True:
        print("1) Deposit")
        print("2) Withdraw")
        print("3) Balance")
        print("4) Quit")
        choice = input("Choice: ").strip()

        if choice == "1":
            # I had accidentaly done all of my work on the template branch instaid of copying it
            DepAmmount:float = float(input("Amount:"))
            balance += DepAmmount
            print(f"New balance: {balance:.2f}")
            pass
        elif choice == "2":
            WitAmmount:float = float(input("Amount:"))
            if WitAmmount <= balance:
                balance -= WitAmmount
                print(f"New balance: {balance:.2f}")
            else:
                print("Insufficient funds")
            pass
        elif choice == "3":
            print(f"Current balance: {balance:.2f}")
            pass
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
