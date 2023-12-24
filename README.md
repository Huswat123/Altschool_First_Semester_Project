# Altschool_First_Semester_Project

# 1.0 Building an Expense Tracker Using Object Oriented Programing in Python
The objective of this project is to build an expense tracking syetm using object oriented programming concept in python. 


# Expense Class:

**init method:** This method initializes the attributes of the Expense class.
It generates a unique identifier (id) using uuid.uuid4(), sets the title and amount,
and records the creation time in UTC (created_at).
The updated_at attribute is set initially to the creation time.

**update method:** This method allows updating the title and/or amount of the expense.
If title or amount is provided, it updates the corresponding attribute(s).
It also updates the updated_at timestamp to the current UTC time.

**to_dict method:** This method returns a dictionary representation of the expense,
including id, title, amount, created_at, and updated_at in ISO format.

# ExpenseDatabase Class:

**init method:** This method initializes an empty list (expenses) to store instances of the Expense class.

**add_expense method:** This method adds an expense to the list of expenses in the database.

**remove_expense method:** This method removes an expense from the database based on its id.

**get_expense_by_id method:** This method retrieves an expense from the database based on its id.

**get_expenses_by_title method:** This method retrieves a list of expenses from the database based on their titles.

**to_dict method:** This method returns a list of dictionaries, each representing an expense in the database.
It leverages the to_dict method of the Expense class. 

# Note
The Expense class represents individual expenses with unique IDs, titles, amounts, creation times, and update times.
The ExpenseDatabase class manages a list of expenses, allowing addition, removal, and retrieval based on ID or title.
The code uses UUID for unique identification, datetime for timestamp management, and dictionary formats for easy conversion and serialization.

# 2.0 How to Clone The Repository

I clone the repository by using the git clone Comand. The git clone command is used to create a copy of a specific repository or branch within a repository.

Git is a distributed version control system. Maximize the advantages of a full repository on your own machine by cloning.

# Steps to Clone
The steps to Initiation a git clone.
1. Create a folder in the local machine and use "mkdir{directory_name} to initialize the folder
2. then, use "cd {directory_name}" to set the terminal to the directory of the folder
3. Clone the git repository into the folder created using this command:
   
```git clone https://github.com/Huswat123/Altschool_First_Semester_Project.git/```

This command creates a copy of the entire repository, including its files, commit history, and branches, on your local machine. It establishes a connection between your local copy and the remote repository, allowing you to pull updates and push changes back to the repository if you have the necessary permissions. It makes changes easier.

# Note
Any of the following terminals can be used to handle git provided it is already installed on your system; CommandPrompt, Git Bash, VS Code and Git GUI.

# 3.0 How to Run The Code
Here is a script that explains the implementation and demonstrate the functionality of the Expense Tracking System bit by bit using the Expense and ExpenseDatabase classes. to ensure that the code runs  effectively the following instances were created;

# 3.1 Creating an Expense Instances

```expense1 = Expense("Groceries", 50.0)```
```expense2 = Expense("Dinner", 30.0)```       

# 3.2 Creating an ExpenseDatabase Instances

```expense_db = ExpenseDatabase()```

# 3.3 Adding Expenses to the Database

```expense_db.add_expense(expense1)```
```expense_db.add_expense(expense2)```

This part of the code add expense to the database

# 3.4  Updating an Expense
```expense1.update(amount=60.0)```

This part of the code update expense1 by changing the amount from 50.0 to 60.0

# 3.5 Removing An Expemse
```expense_db.remove_expense(expense2.id)```

This part of the code remove  expense2 from tghe database

# 3.6 Converting an ExpenseDatabase to Dictionary
```for expense in expense_db.expenses:```
    ```print(expense.to_dict())```

 # Note
  The to_dict method is likely designed to convert the ExpenseDatabase contents into a dict of dictionaries for easy representation or serialization.

Overall, the code provides a basic illustration of the functionalities of expense tracking system using the defined classes. the 

