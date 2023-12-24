Expense Class:
__init__ method: This method initializes the attributes of the Expense class.
It generates a unique identifier (id) using uuid.uuid4(), sets the title and amount,
and records the creation time in UTC (created_at).
The updated_at attribute is set initially to the creation time.

update method: This method allows updating the title and/or amount of the expense.
If title or amount is provided, it updates the corresponding attribute(s).
It also updates the updated_at timestamp to the current UTC time.

to_dict method: This method returns a dictionary representation of the expense,
including id, title, amount, created_at, and updated_at in ISO format.

ExpenseDatabase Class:
__init__ method: This method initializes an empty list (expenses) to store instances of the Expense class.

add_expense method: This method adds an expense to the list of expenses in the database.

remove_expense method: This method removes an expense from the database based on its id.

get_expense_by_id method: This method retrieves an expense from the database based on its id.

get_expenses_by_title method: This method retrieves a list of expenses from the database based on their titles.

to_dict method: This method returns a list of dictionaries, each representing an expense in the database.
It leverages the to_dict method of the Expense class.

How to run the code

Open a Terminal or Command Prompt:
Open a terminal or command prompt on your computer.

Navigate to the Directory:
Use the cd command to navigate to the directory where you saved the Python file. 

Run the Script:
Run the script using the following command:
python expenses.py

Check the Output:
The script will execute, and if there are no errors, you should see the output in the terminal.