# Import the Bank class from the bank_management module
from bank_management import Bank

def main():
    """Main function to run the bank management system CLI."""
    # Create an instance of the Bank class
    my_bank = Bank("Global Trust Bank")
    print(f"Welcome to {my_bank.name}!")

    # Start an infinite loop to display the menu until the user exits
    while True:
        # Display the main menu options to the user
        print("\nPlease choose an option:")
        print("1. Create a new account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Check balance")
        print("5. View account details")
        print("6. List all accounts")
        print("7. Close an account")
        print("8. Exit")

        # Get the user's choice from the input
        choice = input("Enter your choice (1-8): ")

        # Option 1: Create a new account
        if choice == '1':
            name = input("Enter account holder's name: ")
            account_type = input("Enter account type (e.g., Savings, Checking): ")
            # Use a try-except block to handle non-numeric input for the deposit
            try:
                initial_deposit = float(input("Enter initial deposit amount: $"))
                my_bank.create_account(name, account_type, initial_deposit)
            except ValueError:
                print("\nInvalid amount. Please enter a number.")

        # Option 2: Deposit money into an existing account
        elif choice == '2':
            # Use a try-except block to handle non-numeric input
            try:
                acc_num = int(input("Enter account number: "))
                amount = float(input("Enter amount to deposit: $"))
                # Find the account first
                account = my_bank.find_account(acc_num)
                if account:
                    # If account is found, call the deposit method
                    account.deposit(amount)
                else:
                    print("\nAccount not found.")
            except ValueError:
                print("\nInvalid input. Please enter numbers for account number and amount.")

        # Option 3: Withdraw money from an existing account
        elif choice == '3':
            # Use a try-except block to handle non-numeric input
            try:
                acc_num = int(input("Enter account number: "))
                amount = float(input("Enter amount to withdraw: $"))
                # Find the account first
                account = my_bank.find_account(acc_num)
                if account:
                    # If account is found, call the withdraw method
                    account.withdraw(amount)
                else:
                    print("\nAccount not found.")
            except ValueError:
                print("\nInvalid input. Please enter numbers for account number and amount.")

        # Option 4: Check the balance of an account
        elif choice == '4':
            try:
                acc_num = int(input("Enter account number: "))
                account = my_bank.find_account(acc_num)
                if account:
                    # Print the balance formatted to two decimal places
                    print(f"\nCurrent Balance: ${account.get_balance():.2f}")
                else:
                    print("\nAccount not found.")
            except ValueError:
                print("\nInvalid account number. Please enter a number.")

        # Option 5: View all details of a specific account
        elif choice == '5':
            try:
                acc_num = int(input("Enter account number: "))
                account = my_bank.find_account(acc_num)
                if account:
                    # The __str__ method of the Account class is called automatically
                    print(account)
                else:
                    print("\nAccount not found.")
            except ValueError:
                print("\nInvalid account number. Please enter a number.")

        # Option 6: List all accounts in the bank
        elif choice == '6':
            my_bank.list_all_accounts()

        # Option 7: Close an account
        elif choice == '7':
            try:
                acc_num = int(input("Enter account number to close: "))
                my_bank.close_account(acc_num)
            except ValueError:
                print("\nInvalid account number. Please enter a number.")

        # Option 8: Exit the program
        elif choice == '8':
            print("\nThank you for using the Bank Management System. Goodbye!")
            break # Exit the while loop

        # Handle invalid menu choices
        else:
            print("\nInvalid choice. Please select an option from 1 to 8.")

# This ensures the main() function is called only when the script is executed directly
if __name__ == "__main__":
    main()

