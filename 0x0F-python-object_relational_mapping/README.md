
# 0x0F. Python - Object-relational Mapping 🌐

Welcome to the Python - Object-relational Mapping project of the ALX Higher-Level Programming curriculum! This repository contains tasks that demonstrate the use of ORM in Python, specifically using SQLAlchemy, to interact with databases in a more Pythonic way.

## Table of Contents

-   [Tasks](#tasks)
    -   [0. Get all states](#0-get-all-states)
    -   [1. Filter states](#1-filter-states)
    -   [2. Filter states by user input](#2-filter-states-by-user-input)
    -   [3. SQL Injection...](#3-sql-injection)
    -   [4. Cities by states](#4-cities-by-states)
    -   [5. All cities by state](#5-all-cities-by-state)
    -   [6. First state model](#6-first-state-model)
    -   [7. All states via SQLAlchemy](#7-all-states-via-sqlalchemy)
    -   [8. First state](#8-first-state)
    -   [9. Contains  `a`](#9-contains-a)
    -   [10. Get a state](#10-get-a-state)
    -   [11. Add a new state](#11-add-a-new-state)
    -   [12. Update a state](#12-update-a-state)
    -   [13. Delete states](#13-delete-states)
    -   [14. Cities in state](#14-cities-in-state)
    -   [15. City relationship](#15-city-relationship)
    -   [16. List relationship](#16-list-relationship)
    -   [17. From city](#17-from-city)
-   [How to Run](#how-to-run)
-   [Dependencies](#dependencies)
-   [Author](#author)

## Tasks

### 0. Get all states

📜 Task: Write a script that lists all `states` from the database `hbtn_0e_0_usa`.

### 1. Filter states

🔍 Task: Write a script that lists all `states` with a name starting with `N` from the database `hbtn_0e_0_usa`.

### 2. Filter states by user input

📝 Task: Write a script that takes in an argument and displays all values in the `states` table where `name` matches the argument.

### 3. SQL Injection...

💉 Task: Write a script that takes in arguments and displays all values in the `states` table where `name` matches the argument. Safe from SQL injections.

### 4. Cities by states

🏙️ Task: Write a script that lists all `cities` from the database `hbtn_0e_4_usa`.

### 5. All cities by state

🌆 Task: Write a script that takes in the name of a state as an argument and lists all `cities` of that state.

### 6. First state model

👤 Task: Write a python file that contains the class definition of a `State` and an instance `Base = declarative_base()`.

### 7. All states via SQLAlchemy

📜 Task: Write a script that lists all `State` objects from the database `hbtn_0e_6_usa`.

### 8. First state

📝 Task: Write a script that prints the first `State` object from the database `hbtn_0e_6_usa`.

### 9. Contains `a`

🔍 Task: Write a script that lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa`.

### 10. Get a state

🔍 Task: Write a script that prints the `State` object with the `name` passed as argument from the database `hbtn_0e_6_usa`.

### 11. Add a new state

➕ Task: Write a script that adds the `State` object “Louisiana” to the database `hbtn_0e_6_usa`.

### 12. Update a state

📝 Task: Write a script that changes the name of a `State` object from the database `hbtn_0e_6_usa`.

### 13. Delete states

❌ Task: Write a script that deletes all `State` objects with a name containing the letter `a` from the database `hbtn_0e_6_usa`.

### 14. Cities in state

🌆 Task: Write a Python file similar to model_state.py named model_city.py that contains the class definition of a `City`.

### 15. City relationship

🌆 Task: Improve the files model_city.py and model_state.py, and save them as relationship_city.py and relationship_state.py:

-   `State`  class must have a relationship with  `City`  class
-   Write a script that creates the  `State`  "California" with the  `City`  "San Francisco" in the database  `hbtn_0e_100_usa`

### 16. List relationship

📜 Task: Write a script that lists all `State` objects and corresponding `City` objects from the database `hbtn_0e_101_usa`

### 17. From city

🏙️ Task: Write a script that lists all `City` objects from the database `hbtn_0e_101_usa`

## How to Run

1.  **Clone the repository:**
     
    `git clone https://github.com/Linf0rd/alx-higher_level_programming.git`
    
    `cd alx-higher_level_programming/0x0F-python-object_relational_mapping` 
    
2.  **Run the scripts:**
    
    `./<script_name>.py <mysql_username> <mysql_password> <database_name>` 
    

## Dependencies

-   **MySQL:** Ensure you have MySQL installed.
    
   
    `sudo apt-get install mysql-server` 
    
-   **SQLAlchemy:** Install using pip.
    
    `pip install SQLAlchemy` 
    

## Author

👨‍💻 Linf0rd