import pandas as pd
import datetime

class PersonalFinanceManager:
    def __init__(self):
        self.transactions = pd.DataFrame(columns=['Date', 'Type', 'Amount'])
        self.saving_goals = {}

    def add_income(self, date, amount):
        new_transaction = pd.DataFrame({'Date': [date], 'Type': ['Income'], 'Amount': [amount]})
        self.transactions = pd.concat([self.transactions, new_transaction])

    def add_expense(self, date, amount):
        new_transaction = pd.DataFrame({'Date': [date], 'Type': ['Expense'], 'Amount': [amount]})
        self.transactions = pd.concat([self.transactions, new_transaction])

    def set_saving_goal(self, goal_name, target_amount, deadline):
        self.saving_goals[goal_name] = {'target_amount': target_amount, 'deadline': deadline, 'progress': 0}

    def update_saving_goal_progress(self, goal_name, amount):
        if goal_name in self.saving_goals:
            self.saving_goals[goal_name]['progress'] += amount
            if self.saving_goals[goal_name]['progress'] >= self.saving_goals[goal_name]['target_amount']:
                print(f"Congratulations! You have reached your saving goal for {goal_name}!")

    def check_alerts(self):
        today = datetime.date.today()
        for goal_name, goal in self.saving_goals.items():
            deadline = goal['deadline']
            if deadline <= today:
                if goal['progress'] < goal['target_amount']:
                    print(f"Alert! You have not reached your saving goal for {goal_name} and the deadline has passed.")
            else:
                days_left = (deadline - today).days
                if days_left <= 7:
                    if goal['progress'] < goal['target_amount']:
                        print(f"Alert! You have only {days_left} days left to reach your saving goal for {goal_name}.")

    def generate_report(self):
        income = self.transactions[self.transactions['Type'] == 'Income']['Amount'].sum()
        expenses = self.transactions[self.transactions['Type'] == 'Expense']['Amount'].sum()
        balance = income - expenses
        print(f'Income: {income}')
        print(f'Expenses: {expenses}')
        print(f'Balance: {balance}')
        print("Saving Goals:")
        for goal_name, goal in self.saving_goals.items():
            print(f"{goal_name}: {goal['progress']}/{goal['target_amount']}")

def main():
    finance_manager = PersonalFinanceManager()
    import datetime

# Define a dictionary to store transactions
transactions = []

# Define a dictionary to store saving goals
saving_goals = {}

while True:
    print("\n1. Add transactions")
    print("2. Add Expense")
    print("3. Set Saving Goal")
    print("4. Update Saving Goal Progress")
    print("5. Generate Report")
    print("6. Check Alerts")
    print("7. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        date = input("Enter date: ")
        amount = float(input("Enter amount: "))
        transactions.append({"date": date, "type": "Income", "amount": amount})
        print("Income added successfully!")

    elif choice == "2":
        date = input("Enter date: ")
        amount = float(input("Enter amount: "))
        transactions.append({"date": date, "type": "Expense", "amount": amount})
        print("Expense added successfully!")

    elif choice == "3":
        goal_name = input("Enter goal name: ")
        target_amount = float(input("Enter target amount: "))
        deadline = input("Enter deadline (YYYY-MM-DD): ")
        saving_goals[goal_name] = {"target_amount": target_amount, "deadline": deadline, "progress": 0.0}
        print("Saving goal set successfully!")

    elif choice == "4":
        goal_name = input("Enter goal name: ")
        if goal_name in saving_goals:
            amount = float(input("Enter amount: "))
            saving_goals[goal_name]["progress"] += amount
            print("Saving goal progress updated successfully!")
        else:
            print("Saving goal not found. Please set a saving goal first.")

    elif choice == "5":
        income = sum(t["amount"] for t in transactions if t["type"] == "Income")
        expenses = sum(t["amount"] for t in transactions if t["type"] == "Expense")
        balance = income - expenses
        print(f"Income: {income:.1f}")
        print(f"Expenses: {expenses:.1f}")
        print(f"Balance: {balance:.1f}")
        print("Saving Goals:")
        for goal_name, goal in saving_goals.items():
            print(f"{goal_name}: {goal['progress']:.1f}/{goal['target_amount']:.1f}")

        print("\n**Transactions Table**")
        print("| Date       | Type     | Amount |")
        print("|------------|----------|--------|")
        for transaction in transactions:
            print(f"| {transaction['date']} | {transaction['type']} | {transaction['amount']:.1f} |")
        print()

        print("**Saving Goals Table**")
        print("| Goal Name      | Target Amount | Deadline     | Progress |")
        print("|----------------|---------------|--------------|----------|")
        for goal_name, goal in saving_goals.items():
            print(f"| {goal_name} | {goal['target_amount']:.1f} | {goal['deadline']} | {goal['progress']:.1f} |")
        print()

    elif choice == "6":
        for goal_name, goal in saving_goals.items():
            days_left = (datetime.datetime.strptime(goal["deadline"], "%Y-%m-%d") - datetime.datetime.today()).days
            if days_left <= 0:
                print(f"Alert! You have missed the deadline for {goal_name}.")
            else:
                print(f"Alert! You have only {days_left} days left to reach your saving goal for {goal_name}.")

    elif choice == "7":
        break

    else:
        print("Invalid option. Please try again.")