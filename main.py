import sys
from datetime import datetime


def trans_entry(menu_stack):
    while True:
        print("""
        1) Transfer Money
        2) Withdraw Money
        3) Airtime and Bundles
        4) My Wallet
        5) Cancel

        Select Transaction: """)
        trans_code = input("Enter your choice: ")
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
                        number = input("Enter the number: ")
                        if len(number) == 10 and number.isdigit():
                            amount = input("Amount: ")
                            print("You have successfully transferred GHC", amount, "to", number, "on", datetime.now())
                            sys.exit()
                        else:
                            print("Invalid Mobile Number. Please try again")
                elif choice == "2":
                    while True:
                        number = input("Enter the number: ")
                        if len(number) == 10 and number.isdigit():
                            amount = input("Amount: ")
                            print("Confirmed. GHC", amount, "sent to", number, "on", datetime.now())
                            sys.exit()
                        else:
                            print("Invalid Mobile Number. Please try again")
                elif choice == "3":
                    while True:
                        number = input("Account Number: ")
                        if len(number) == 15 and number.isdigit():
                            amount = input("Amount: ")
                            print("Your payment of GHS", amount, ".00 to BANK_PUSH has been completed at",
                                  datetime.now(), "- Reference:", number)
                            sys.exit()
                        else:
                            print("Invalid Bank Account Number. Please try again")
                elif choice == "0":
                    if len(menu_stack) > 1:
                        print("Returning to previous menu...")
                        menu_stack.pop()
                        break
                    else:
                        print("You are at the top-level menu. Cannot go back further.")
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
                                print(amount, "withdrawn from Agent Number:", number, "on", datetime.now())
                                sys.exit()
                            else:
                                print("Invalid pin. Please try again.")
                        else:
                            print("Invalid Agent Number. Please try again.")
                elif choice == "2":
                    while True:
                        number = input("Enter the ATM Number: ")
                        if len(number) == 10 and number.isdigit():
                            amount = input("Amount: ")
                            pin = input("Enter a 4-digit pin: ")
                            if len(pin) == 4 and pin.isdigit():
                                print("Confirmed. GHC", amount, "withdrawn from ATM", number, "on", datetime.now())
                                sys.exit()
                            else:
                                print("Invalid pin. Please try again.")
                        else:
                            print("Invalid ATM Number. Please try again.")
                elif choice == "0":
                    print("Returning to previous menu...")
                    menu_stack.pop()
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
                        my_choice = input("1. Buy Airtime\n2. Check Balance\n Enter your choice : ")
                        if my_choice == "1":
                            amount = input("Amount: ")
                            print("Congratulations,GHC", amount, "has been purchased to your account as airtime")
                            sys.exit()
                        elif my_choice == "2":
                            print("Your account balance is GHC_____.00")
                            sys.exit()
                        else:
                            print("Invalid choice. Please try again.")
                elif choice == "2":
                    while True:
                        my_choice = input("1. Buy Internet Bundle\n2. Check Data Balance\n Enter your choice : ")
                        if my_choice == "1":
                            amount = input("Amount: ")
                            print(amount, "MB has been purchased to your account")
                            sys.exit()
                        elif my_choice == "2":
                            print("Your account balance is ______.MB")
                            sys.exit()
                        else:
                            print("Invalid choice. Please try again.")
                elif choice == "3":
                    while True:
                        number = input("Enter the number: ")
                        if len(number) == 10 and number.isdigit():
                            amount = input("Amount: ")
                            print("GHC", amount, ".00 airtime sent to user", number, "on", datetime.now(),
                                  ".Family is everything :)")
                            sys.exit()
                        else:
                            print("Invalid Mobile Number. Please try again")
                elif choice == "4":
                    while True:
                        number = input("Enter the number: ")
                        if len(number) == 10 and number.isdigit():
                            amount = input("Amount: ")
                            print("GHC", amount, ".00 airtime sent to user", number, "on", datetime.now())
                            sys.exit()
                        else:
                            print("Invalid Mobile Number. Please try again")
                elif choice == "0":
                    print("Returning to previous menu...")
                    menu_stack.pop()
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
                elif choice == "2":
                    input("Your email: ")
                    print("Your wallet statement will be sent to your email")
                    sys.exit()
                elif choice == "3":
                    while True:
                        current_code = input("Enter your current 4-digit code: ")
                        if len(current_code) == 4 and current_code.isdigit():
                            new_code = input("Enter your new 4-digit code: ")
                            if len(new_code) == 4 and new_code.isdigit():
                                print("Code changed successfully on", datetime.now())
                                sys.exit()
                            else:
                                print("Invalid new code. Please enter a 4-digit code.")
                        else:
                            print("Invalid current code. Please enter a 4-digit code.")
                elif choice == "4":
                    input("Kindly state your complaint: ")
                    print("You have successfully lodged a complaint at", datetime.now(),
                          ". We will look into it and get right back to you")
                    sys.exit()
                elif choice == "0":
                    print("Returning to previous menu...")
                    menu_stack.pop()
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif trans_code == "5":
            print("Exiting USSD...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")


def confirm_ussd():
    ussd = input("Enter USSD code:")
    if ussd == "*111#":
        menu_stack = [0]
        while True:
            trans_entry(menu_stack)
    else:
        print("UNKNOWN APPLICATION")
        confirm_ussd()

confirm_ussd()