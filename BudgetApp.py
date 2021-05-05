class Budget:
    """A simple model of a budget."""
    def __init__(self, category):
        """Initialize attribute of the budget."""
        self.category = category
        self.amount = 1

    def deposit(self):
        """Deposit funds to each category."""
        print("\nPlease deposit money for food, clothing and entertainment.\n")

        deposit_amount = int(input("Enter amount you want to deposit: \n"))

        if deposit_amount >= self.amount:
           self.amount = deposit_amount
           return self.amount
        
        else:
            print("You have entered an invalid amount.")
            

    def withdraw(self):
        """Withdraw funds from each category."""
        print("\n")
        withdraw_amount = int(input("Enter amount you want to withdraw: \n"))

        if withdraw_amount <= self.amount:
           self.amount = withdraw_amount
           return self.amount
        
        else:
            print("You have entered an invalid amount.")

    def balance_for_deposit(self):
        """Check account balance when deposit is made."""
        self.amount += 1
        return self.amount

my_budget = Budget("Food")
print("You have deposited " + str(my_budget.deposit()) + " for food")
print("You have withdrawn " + str(my_budget.withdraw()) + " for food")
print("Your balance after deposit is " + str(my_budget.balance_for_deposit()) + " for food")
