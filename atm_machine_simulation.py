class ATM:
    def __init__(self, initial_balance=0, pin="1234"):
        """
        Initializes the ATM with a starting balance and PIN.
        
        Args:
        initial_balance (float): The initial balance of the account.
        pin (str): The account's PIN code.
        """
        self.balance = initial_balance
        self.pin = pin
        self.transaction_history = []

    def check_balance(self):
        """
        Prints the current account balance and logs the transaction.
        """
        print(f"Your current balance is: ${self.balance:.2f}")
        self.transaction_history.append("Checked balance")

    def deposit(self, amount):
        """
        Deposits a specified amount into the account if the amount is positive.

        Args:
        amount (float): The amount to be deposited.
        """
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} deposited successfully.")
            self.transaction_history.append(f"Deposited ${amount:.2f}")
        else:
            print("Invalid amount. Please enter a positive number.")

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if there are sufficient funds.

        Args:
        amount (float): The amount to be withdrawn.
        """
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"${amount:.2f} withdrawn successfully.")
            self.transaction_history.append(f"Withdrew ${amount:.2f}")
        else:
            print("Invalid transaction. Check the amount or your balance.")

    def change_pin(self, old_pin, new_pin):
        """
        Changes the PIN if the old PIN is correct.

        Args:
        old_pin (str): The current PIN.
        new_pin (str): The new PIN to be set.
        """
        if old_pin == self.pin:
            self.pin = new_pin
            print("PIN changed successfully.")
            self.transaction_history.append("Changed PIN")
        else:
            print("Incorrect PIN.")

    def show_transaction_history(self):
        """
        Prints the list of all transactions.
        """
        if self.transaction_history:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(f" - {transaction}")
        else:
            print("No transactions yet.")

def main():
    """
    The main function that runs the ATM simulation. It presents a menu to the user
    and calls the appropriate ATM class methods based on user input.
    """
    atm = ATM(initial_balance=1000)  # Initialize ATM with $1000 balance
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == '4':
            old_pin = input("Enter current PIN: ")
            new_pin = input("Enter new PIN: ")
            atm.change_pin(old_pin, new_pin)
        elif choice == '5':
            atm.show_transaction_history()
        elif choice == '6':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
