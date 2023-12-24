import uuid
from datetime import datetime, timezone


class Expense:
    def __init__(self, title, amount):
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

    def update(self, title=None, amount=None):
        if title:
            self.title = title
        if amount:
            self.amount = amount
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }


class ExpenseDatabase:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, expense_id):
        self.expenses = [e for e in self.expenses if e.id != expense_id]

    def get_expense_by_id(self, expense_id):
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None

    def get_expenses_by_title(self, title):
        return [expense for expense in self.expenses if expense.title == title]

    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]


# Example

expense_db = ExpenseDatabase()

# This part of the code add expense to the database
expense1 = Expense("Groceries", 50.0)
expense2 = Expense("Dinner", 30.0)
expense_db.add_expense(expense1)
expense_db.add_expense(expense2)

# This part of the code update expense1. this shows that the code runs effectively
expense1.update(amount=60.0)

for expense in expense_db.expenses:
    print(expense.to_dict())

#this part of the code remove  expense2 from tghe database
expense_db.remove_expense(expense2.id)

for expense in expense_db.expenses:
    print(expense.to_dict())

