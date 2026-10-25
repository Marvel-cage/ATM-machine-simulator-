import time
import sys

correct_pin = {
    "2024": "Adikwu John Stephen",
    "1234": "Arora Cookie Lyon",
    "1001": "Michael Kelvin Gabriel",
    "0000": "George Washington Mark",
    "0123": "Will Nelson Mandella"
}
my_account_balance = 1000
my_account_number = 1684023598

while True:
    welcome_message = "WELCOME TO JOHN ADIKWU ATM SIMULATOR"
    for letter in welcome_message:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(.1)

    print()
    print()
    print("1. Insert your card")
    print("2. Exit")
    print()
    choice = input("Enter number corresponding to your choice: ")

    if choice == '1':
        max_attempts = 3
        attempts = 0

        while attempts < max_attempts:
            pin = (input("Enter your PIN: "))
            attempts += 1
            if pin.isdigit():
                if len(pin) == 4:
                    if pin in correct_pin:
                        print("PIN accepted! Access granted.")
                        print()
                        accountholder = correct_pin[pin]
                        print(f"Welcome back {accountholder}")
                        print()

                        while True:
                            print("1. Check Balance")
                            print("2. Deposit")
                            print("3. Withdraw")
                            print("4. Transfer")
                            print("5. Change PIN")
                            print("6. Exit")
                            transaction = input("Select transaction type: ")
                            print()

                            if transaction == '1':
                                print("Please wait...")
                                time.sleep(4)
                                print(f"Your current balance is: ${my_account_balance}")
                                print()

                            elif transaction == '2':
                                while True:
                                    print("Select deposit type:")
                                    print("1. Cash")
                                    print("2. Cheque")
                                    deposit_type = input("Enter the number corresponding to deposit type: ").lower()
                                    if deposit_type == '1':
                                        deposit_amount = float(input("Enter amount to deposit: "))
                                        my_account_balance += deposit_amount
                                        print("Please wait...")
                                        time.sleep(4)
                                        print(f"You have successfully deposited ${deposit_amount}. Your new balance is: ${my_account_balance}")
                                        print()
                                        break
                                    elif deposit_type == '2':
                                        while True:
                                            cheque_number = input("Enter cheque number: ")
                                            if len(cheque_number) == 6 and cheque_number.isdigit():
                                                cheque_amount = float(input("Enter amount of the cheque: "))
                                                my_account_balance += cheque_amount
                                                print()
                                                print("Please wait...")
                                                time.sleep(4)
                                                print(f"Cheque of ${cheque_amount}, cheque no: {cheque_number}, deposited successfully.\n"
                                                      f"Your new balance is: ${my_account_balance}")
                                                print()
                                                break
                                            else:
                                                print("Invalid cheque number. Please try again.")
                                                print()
                                        break
                                    else:
                                        print("Invalid deposit type option.")
                                        print()

                            elif transaction == '3':
                                while True:
                                    print("Select the account type")
                                    print("1. Savings")
                                    print("2. Current")
                                    account_type = input("Enter the number corresponding to the type of account: ")
                                    if account_type == '1':
                                        break
                                    elif account_type == '2':
                                        break
                                    else:
                                        print("Invalid option. Please try again.")
                                        print()

                                withdraw_amount = float(input("Enter amount to withdraw: "))
                                if 0 < withdraw_amount < 20000:
                                    if withdraw_amount <= my_account_balance:
                                        my_account_balance -= withdraw_amount
                                        print("Please wait...")
                                        time.sleep(4)
                                        print(f"You have successfully withdrawn ${withdraw_amount}. Your new balance is: ${my_account_balance}")
                                        print()
                                    else:
                                        print("Insufficient funds.")
                                        print()
                                else:
                                    print(f"You cannot withdraw more than $20000 at once")

                            elif transaction == '4':
                                while True:
                                    print("Select the account type to transfer to:")
                                    print("1. Savings")
                                    print("2. Current")
                                    account_type = input("Enter the number corresponding to the type of account: ")
                                    if account_type == '1':
                                        break
                                    elif account_type == '2':
                                        break
                                    else:
                                        print("Invalid option. Please try again.")
                                        print()

                                beneficiaries = {
                                    "1234567890": "John Smith Doe",
                                    "1357924680": "John Reece Stone",
                                    "1020406080": "John Adikwu Stephen",
                                    "0102030405": "John Augustin Caleb"
                                }
                                while True:
                                    print()
                                    print("Select the bank to transfer to:")
                                    print("1. First Bank")
                                    print("2. Access Bank")
                                    print("3. Wema Bank")
                                    print("4. GT Bank")
                                    print("5. Others")
                                    print()
                                    bank_choice = input("Enter the number corresponding to the bank: ")

                                    if bank_choice == '1':
                                        bank_name = "First Bank"
                                        break
                                    elif bank_choice == '2':
                                        bank_name = "Access Bank"
                                        break
                                    elif bank_choice == '3':
                                        bank_name = "GT Bank"
                                        break
                                    elif bank_choice == '4':
                                        bank_name = "Heritage Bank"
                                        break
                                    elif bank_choice == '5':
                                        print()
                                        print("Please wait...")
                                        time.sleep(2)
                                        print()
                                        print("6. Diamond Bank")
                                        print("7. Kuda Bank")
                                        print("8. Heritage Bank")
                                        print("9. Fidelity Bank")
                                        print()
                                        bank_choice = input("Enter the number corresponding to the bank: ")

                                        if bank_choice == '6':
                                            bank_name = "Diamond Bank"
                                            break
                                        elif bank_choice == '7':
                                            bank_name = "Kuda Bank"
                                            break
                                        elif bank_choice == '8':
                                            bank_name = "Heritage Bank"
                                            break
                                        elif bank_choice == '9':
                                            bank_name = "Fidelity Bank"
                                            break
                                        else:
                                            print("Invalid bank selection. Please try again!")
                                            print()
                                            continue
                                    else:
                                        print("Invalid bank selection. Please try again!")
                                        print()

                                while True:
                                    account_number = input("Enter the beneficiary's account number: ")
                                    if len(account_number) == 10 and account_number.isdigit():
                                        if account_number in beneficiaries:
                                            beneficiary_name = beneficiaries[account_number]
                                            time.sleep(4)
                                            confirm = input(f"{beneficiary_name}\nDo you want to proceed? (yes/no): ")
                                            if confirm.lower() != "yes":
                                                print("Transfer canceled.")
                                                print()
                                                break
                                        else:

                                            print("Beneficiary name not found. Please check the account number again.")
                                            print()
                                            continue

                                        transfer_amount = float(input("Enter amount to transfer: "))
                                        if transfer_amount <= my_account_balance:
                                            my_account_balance -= transfer_amount
                                            print()
                                            print("Please wait...")
                                            print()
                                            time.sleep(4)
                                            print(f"You have successfully transferred ${transfer_amount} to {beneficiary_name}.\n"
                                                  f"Bank: {bank_name}\n"
                                                  f"Your new balance is: ${my_account_balance}")
                                            print()
                                            break
                                        else:
                                            print("Insufficient funds.")
                                            print()
                                            continue_transfer = input("Would you like to try again(yes/no): ")
                                            if continue_transfer.lower() == "yes":
                                                print()
                                            elif continue_transfer.lower() == "no":
                                                break
                                            else:
                                                print("invalid input")
                                    else:
                                        print("Invalid account number! Please check and enter a 10-digit account number.")
                                        print()

                            elif transaction == '5':
                                while True:
                                    new_pin = (input("Enter your new 4-digit PIN: "))
                                    if len(new_pin) == 4 and new_pin.isdigit():
                                        confirm_pin = (input("Confirm your new PIN: "))
                                        if new_pin == confirm_pin:
                                            if pin in correct_pin:
                                                correct_pin[confirm_pin] = correct_pin[pin]
                                                del correct_pin[pin]
                                                print("PIN successfully changed.")
                                                print()
                                                break
                                        else:
                                            print("PINs do not match. Please tr1y again.")
                                            print()
                                    else:
                                        print("Invalid PIN. PIN must be 4 digits. Please try again.")
                                        print()

                            elif transaction == '6':
                                print("Thank you for using the ATM. Goodbye!")
                                print()
                                break
                            else:
                                print("Invalid option. Please try again.")

                            another_transaction = input("Do you want to perform another transaction? (yes/no): ")
                            print()
                            if another_transaction.lower() == 'no':
                                print("Thank you for using the ATM. Please remove your card. Goodbye!")
                                time.sleep(3)
                                print()
                                break
                            elif another_transaction.lower() not in ("yes", "no"):
                                print("Type either yes or no")
                        break
                else:
                    print("Error, pin can only be 4 digits")
                    print()
            else:
                print("Error, pin can only be in digits")
                print()
            if attempts < max_attempts:
                print("Incorrect PIN. Please try again.")
                print()
            else:
                print("Incorrect PIN entered three times. Your card has been restricted.")
                print()

    elif choice == '2':
        print("Goodbye!")
        print()
        break
    else:
        print("Invalid option. Please try again.")
        print()