
# 0x0E. SQL - More Queries 🗄️

Welcome to the SQL - More Queries project of the ALX Higher-Level Programming curriculum! This repository contains advanced tasks focusing on using SQL to manage databases more effectively, including user privileges, joins, and constraints.

## Table of Contents

-   [Tasks](#tasks)
    -   [0. My privileges!](#0-my-privileges)
    -   [1. Root user](#1-root-user)
    -   [2. Read user](#2-read-user)
    -   [3. Always a name](#3-always-a-name)
    -   [4. ID can't be null](#4-id-cant-be-null)
    -   [5. Unique ID](#5-unique-id)
    -   [6. States table](#6-states-table)
    -   [7. Cities table](#7-cities-table)
    -   [8. Cities of California](#8-cities-of-california)
    -   [9. Cities by States](#9-cities-by-states)
    -   [10. Genre ID by show](#10-genre-id-by-show)
    -   [11. Genre ID for all shows](#11-genre-id-for-all-shows)
    -   [12. No genre](#12-no-genre)
    -   [13. Number of shows by genre](#13-number-of-shows-by-genre)
    -   [14. My genres](#14-my-genres)
    -   [15. Only Comedy](#15-only-comedy)
    -   [16. List shows and genres](#16-list-shows-and-genres)
    -   [17. Not my genre](#17-not-my-genre)
    -   [18. No Comedy tonight!](#18-no-comedy-tonight)
    -   [19. Rotten tomatoes](#19-rotten-tomatoes)
    -   [20. Best genre](#20-best-genre)
-   [How to Run](#how-to-run)
-   [Dependencies](#dependencies)
-   [Author](#author)

## Tasks

### 0. My privileges!

🛡️ Task: Write a script that lists all privileges of the MySQL users `root` and `user`.

### 1. Root user

👤 Task: Write a script that creates the MySQL user `user_0d_1` with all privileges.

### 2. Read user

🔍 Task: Write a script that creates the MySQL user `user_0d_2` with SELECT privileges on the database `hbtn_0d_2`.

### 3. Always a name

🏷️ Task: Write a script that creates the table `force_name` with a NOT NULL constraint on the column `name`.

### 4. ID can't be null

🆔 Task: Write a script that creates the table `id_not_null` with a NOT NULL constraint on the column `id`.

### 5. Unique ID

🔑 Task: Write a script that creates the table `unique_id` with a UNIQUE constraint on the column `id`.

### 6. States table

📋 Task: Write a script that creates the table `states`.

### 7. Cities table

🏙️ Task: Write a script that creates the table `cities`.

### 8. Cities of California

🌆 Task: Write a script that lists all cities of California from the database `hbtn_0d_usa`.

### 9. Cities by States

📋 Task: Write a script that lists all cities from the database `hbtn_0d_usa`.

### 10. Genre ID by show

🎭 Task: Write a script that lists all shows in the `hbtn_0d_tvshows` database with their genre ID.

### 11. Genre ID for all shows

📋 Task: Write a script that lists all genres in the `hbtn_0d_tvshows` database.

### 12. No genre

🚫 Task: Write a script that lists all shows in the `hbtn_0d_tvshows` database without a genre.

### 13. Number of shows by genre

🔢 Task: Write a script that lists the number of shows by genre in the `hbtn_0d_tvshows` database.

### 14. My genres

🎭 Task: Write a script that lists all genres in the `hbtn_0d_tvshows` database.

### 15. Only Comedy

😂 Task: Write a script that lists all comedy shows in the `hbtn_0d_tvshows` database.

### 16. List shows and genres

📋 Task: Write a script that lists all shows and their genres in the `hbtn_0d_tvshows` database.

### 17. Not my genre

🚫 Task: Write a script that lists all shows not in the genre "Comedy" in the `hbtn_0d_tvshows` database.

### 18. No Comedy tonight!

🚫 Task: Write a script that deletes all shows in the `hbtn_0d_tvshows` database with the genre "Comedy".

### 19. Rotten tomatoes

🍅 Task: Write a script that updates the genre "Drama" to "Comedy" in the `hbtn_0d_tvshows` database.

### 20. Best genre

🏆 Task: Write a script that lists the number of shows in each genre in the `hbtn_0d_tvshows` database, sorted by the number of shows in descending order.

## How to Run

1.  **Clone the repository:**
        
    `git clone https://github.com/Linf0rd/alx-higher_level_programming.git`
    
    `cd alx-higher_level_programming/0x0E-SQL_more_queries` 
    
2.  **Run the SQL scripts:**
    
    `mysql -u root -p < <script_name>.sql` 
    

## Dependencies

-   **MySQL:**  Ensure you have MySQL installed.
    
    `sudo apt-get install mysql-server` 
    

## Author

👨‍💻 Linf0rd