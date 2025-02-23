# Alt-school-project

# Introduction

This project is designed to assess the understanding of Object-Oriented Programming (OOP) concepts in Python by implementing two classes: Expense and ExpenseDatabse. These classes are used to model and manage financial expenses effectively.

The system provides functionalities to:

Create expense records.

Store multiple expenses.

Search expenses by title or ID.

Update expenses.

Remove expenses.


## Features
-- UUID-based unique identifiers for each expense.

-- Automatic timestamping for expense creation and updates.

-- CRUD (Create, Read, Update, Delete) operations for managing expenses.

-- Search functionality to find expenses by title or ID.


## Technologies Used

Python 3

Object-Oriented Programming (OOP)

UUID for unique identification

Datetime for timestamp management


## Class Implementations

### Expense Class

This class represents an individual financial expense.

#### Attributes:

id (str) - A unique identifier (UUID format).

title (str) - The title of the expense.

amount (float) - The amount spent.

created_at (datetime) - Timestamp of creation (UTC).

updated_at (datetime) - Timestamp of the last update (UTC).

#### Methods:

__init__(self, title, amount): Initializes an expense with a title, amount, and timestamps.

update(self, title=None, amount=None): Updates the title and/or amount, and refreshes the updated_at timestamp.

to_dict(self): Returns a dictionary representation of the expense.

NB: I used $ for amount spent

### ExpenseDatabase Class

This class manages a collection of expenses.

#### Attributes:

expenses (list) - A list storing instances of the Expense class.

#### Methods:

__init__(self): Initializes an empty expense list.

add_expense(self, expense): Adds an Expense instance to the list.

remove_expense(self, expense_id): Removes an expense by its id.

get_expense_by_id(self, expense_id): Finds an expense by its id.

get_expense_by_title(self, title): Returns a list of expenses that match the given title.

to_dict(self): Converts all stored expenses into a list of dictionaries.


## How to run the code
I tested my code via two methods.
The first method was creating a .ipynb file so as to the both the expense, expense database ad main.py codes to confirm the code is runing with no error. For the second method, i used 'python main.py' which I ran on the main.py file via vscode terminal.

After confirming my code is running, i the commited my project to my github repository.


## Clone the Repository: 
To clone my repository, I created a new one, made it public, enabled the readme, chose python at the gitignore and the chose MIT as license. I then right clicked to copy the repository link, opened my command prompt from  my local computer and cloned the repository using the code below.
```sh
git clone https://github.com/Chinelonweke/Alt-school-project.git 




