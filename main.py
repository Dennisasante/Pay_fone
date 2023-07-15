import sys
def transEntry():
    while True:
        transCode = input("""
        1) Transfer Money
        2) Withdraw Money
        3) Airtime and Bundles
        4) My Wallet

        Select Transaction: """)
        if transCode == "1":
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
        elif transCode == "2":
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
                            PIN = input("Enter your 4-digit pin: ")
                            if len(PIN) == 4 and PIN.isdigit():
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
                            PIN = input("Enter a 4-digit PIN: ")
                            if len(PIN) == 4 and PIN.isdigit():
                                print(amount, "withdrawn from ATM", number)
                                sys.exit()
                            else:
                                print("Invalid PIN. Please try again.")
                        else:
                            print("Invalid ATM Number. Please try again.")
                elif choice == "0":
                    print("Returning to previous menu...")
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif transCode == "3":
            while True:
                print("""
                1) Airtime
                2) Internet Bundles
                3) For Friends and Family
                4) Other Networks
                0) Back""")
                choice = input("Enter your choice: ")
                if choice == "1":
                    print("Airtime and Bundles - Airtime")
                    # Perform the desired action for purchasing airtime
                    # Add your code here
                elif choice == "2":
                    print("Airtime and Bundles - Internet Bundles")
                    # Perform the desired action for purchasing internet bundles
                    # Add your code here
                elif choice == "3":
                    print("Airtime and Bundles - For Friends and Family")
                    # Perform the desired action for sending airtime to friends and family
                    # Add your code here
                elif choice == "4":
                    print("Airtime and Bundles - Other Networks")
                    # Perform the desired action for purchasing airtime for other networks
                    # Add your code here
                elif choice == "0":
                    print("Returning to previous menu...")
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif transCode == "4":
            while True:
                print("""
                1) Check Balance
                2) My Statements
                3) Change Pin
                4) Report Fraud
                0) Back""")
                choice = input("Enter your choice: ")
                if choice == "1":
                    print("My Wallet - Check Balance")
                    # Perform the desired action for checking the balance
                    # Add your code here
                elif choice == "2":
                    print("My Wallet - My Statements")
                    # Perform the desired action for viewing statements
                    # Add your code here
                elif choice == "3":
                    print("My Wallet - Change Pin")
                    # Perform the desired action for changing the PIN
                    # Add your code here
                elif choice == "4":
                    print("My Wallet - Report Fraud")
                    # Perform the desired action for reporting fraud
                    # Add your code here
                elif choice == "0":
                    print("Returning to previous menu...")
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif transCode == "0":
            print("Exiting USSD...")
            break
        else:
            print("Invalid choice. Please try again.")


def confirmUSSD():
    ussd = input("Enter USSD code:")
    if ussd == "*111#":
        transEntry()
    else:
        print("UNKNOWN APPLICATION")
        confirmUSSD()


# calling the function
confirmUSSD()
