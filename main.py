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
                3) Favorite
                4) Bank Account
                0) Back""")
                choice = input("Enter your choice: ")
                if choice == "1":
                    print("Transfer Money - Momo User")
                    # Perform the desired action for Momo User transfer
                    # Add your code here
                elif choice == "2":
                    print("Transfer Money - Other Networks")
                    # Perform the desired action for Other Networks transfer
                    # Add your code here
                elif choice == "3":
                    print("Transfer Money - Favorite")
                    # Perform the desired action for Favorite transfer
                    # Add your code here
                elif choice == "4":
                    print("Transfer Money - Bank Account")
                    # Perform the desired action for Bank Account transfer
                    # Add your code here
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
                    print("Withdraw Money - From Agent")
                    # Perform the desired action for withdrawal from an agent
                    # Add your code here
                elif choice == "2":
                    print("Withdraw Money - From ATM")
                    # Perform the desired action for withdrawal from an ATM
                    # Add your code here
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
