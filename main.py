import sys


def trans_entry():
    while True:
        trans_code = input("""
        1) Transfer Money
        2) Withdraw Money
        3) Airtime and Bundles
        4) My Wallet

        Select Transaction: """)
        if trans_code == "1":
            while True:
                print("""
                1) Momo User
                2) Other Networks
                3) Bank Account
                0) Back""")
                choice = input("Enter your choice: ")
                if choice == "1":
                    while True:
                        number = input("Enter the number ")
                        if len(number) == 10 and number.isdigit():
                            amount = input("Amount: ")
                            print(amount, "sent to user", number)
                            sys.exit()
                        else:
                            print("Invalid Mobile Number. Please try again")
                            break
                elif choice == "2":
                    while True:
                        number = input("Enter the number ")
                        if len(number) == 10 and number.isdigit():
                            amount = input("Amount: ")
                            print(amount, "sent to user", number)
                            sys.exit()
                        else:
                            print("Invalid Mobile Number. Please try again")
                            break
                elif choice == "3":
                    number = input("Account Number: ")
                    if len(number) == 15 and number.isdigit():
                        amount = input("Amount: ")
                        print(amount, "sent to Bank Account", number)
                        sys.exit()
                    else:
                        print("Invalid Bank Account Number. Please try again")
                        break
                elif choice == "0":
                    print("Returning to previous menu...")
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif trans_code == "2":
            while True:
                print("""
                1) From Agent
                2) From ATM
                0) Back""")
                choice = input("Enter your choice: ")
                if choice == "1":
                    while True:
                        number = input("Enter the Agent Number: ")
                        if len(number) == 6 and number.isdigit():
                            amount = input("Amount: ")
                            pin = input("Enter your 4-digit pin: ")
                            if len(pin) == 4 and pin.isdigit():
                                print(amount, "withdrawn from Agent Number:", number)
                                sys.exit()
                        else:
                            print("Invalid Agent Number. Please try again")
                            break
                elif choice == "2":
                    while True:
                        number = input("Enter the ATM Number: ")
                        if len(number) == 10 and number.isdigit():
                            amount = input("Amount: ")
                            pin = input("Enter a 4-digit pin: ")
                            if len(pin) == 4 and pin.isdigit():
                                print(amount, "withdrawn from ATM", number)
                                sys.exit()
                            else:
                                print("Invalid pin. Please try again.")
                        else:
                            print("Invalid ATM Number. Please try again.")
                elif choice == "0":
                    print("Returning to previous menu...")
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif trans_code == "3":
            while True:
                print("""
                1) Airtime
                2) Internet Bundles
                3) For Friends and Family
                4) Other Networks
                0) Back""")
                choice = input("Enter your choice: ")
                if choice == "1":
                    while True:
                        my_choice = input("1. Buy Airtime\n2. Check Balance\n")
                        if my_choice == "1":
                            amount = input("Amount: ")
                            print(amount, "has been purchased to your account")
                        elif my_choice == "2":
                            print("Your account balance is AMOUNT")
                            sys.exit()
                        else:
                            print("Invalid choice. Please try again.")
                            break
                elif choice == "2":
                    while True:
                        my_choice = input("1. Buy Internet Bundle\n2. Check Data Balance\n")
                        if my_choice == "1":
                            amount = input("Amount: ")
                            print(amount, " MB has been purchased to your account")
                        elif my_choice == "2":
                            print("Your account balance is AMOUNT")
                            sys.exit()
                        else:
                            print("Invalid choice. Please try again.")
                            break
                elif choice == "3":
                    while True:
                        number = input("Enter the number ")
                        if len(number) == 10 and number.isdigit():
                            amount = input("Amount: ")
                            print(amount, "sent to user.\n", number, "Family is everything :)")
                            sys.exit()
                        else:
                            print("Invalid Mobile Number. Please try again")
                            break
                elif choice == "4":
                    while True:
                        number = input("Enter the number ")
                        if len(number) == 10 and number.isdigit():
                            amount = input("Amount: ")
                            print(amount, "sent to user", number)
                            sys.exit()
                        else:
                            print("Invalid Mobile Number. Please try again")
                            break
                elif choice == "0":
                    print("Returning to previous menu...")
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif trans_code == "4":
            while True:
                print("""
                1) Check Balance
                2) My Statements
                3) Change Pin
                4) Report Fraud
                0) Back""")
                choice = input("Enter your choice: ")
                if choice == "1":
                    while True:
                        pin = input("Enter your 4-digit pin: ")
                        if len(pin) == 4 and pin.isdigit():
                            print("Your account balance is __GHC")
                            sys.exit()
                        else:
                            print("Invalid pin. Please try again")
                            break
                elif choice == "2":
                    input("Your email :")
                    print("Your wallet statement will be sent to your email")
                elif choice == "3":
                    while True:
                        current_code = input("Enter your current 4-digit code: ")
                        if len(current_code) == 4 and current_code.isdigit():
                            new_code = input("Enter your new 4-digit code: ")
                            if len(new_code) == 4 and new_code.isdigit():
                                print("Code changed successfully!")
                                sys.exit()
                            else:
                                print("Invalid new code. Please enter a 4-digit code.")
                        else:
                            print("Invalid current code. Please enter a 4-digit code.")
                elif choice == "4":
                    input("Kindly state your complain: ")
                    print("We will look into it and get right back to you")
                elif choice == "0":
                    print("Returning to previous menu...")
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif trans_code == "0":
            print("Exiting USSD...")
            break
        else:
            print("Invalid choice. Please try again.")


def confirm_ussd():
    ussd = input("Enter USSD code:")
    if ussd == "*111#":
        trans_entry()
    else:
        print("UNKNOWN APPLICATION")
        confirm_ussd()


# calling the function
confirm_ussd()
