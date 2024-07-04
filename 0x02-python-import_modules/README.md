
# 0x02. Python - import & modules 📦

Welcome to the Import & Modules project of the ALX Higher-Level Programming curriculum! This repository contains tasks and scripts that cover how to use import statements and modules in Python, helping to modularize and organize your code effectively.

## Table of Contents

-   [Tasks](#tasks)
    -   [0. Import a simple function from a simple file](#0-import-a-simple-function-from-a-simple-file)
    -   [1. My first toolbox!](#1-my-first-toolbox)
    -   [2. How to make a script dynamic!](#2-how-to-make-a-script-dynamic)
    -   [3. Infinite addition](#3-infinite-addition)
    -   [4. Who are you?](#4-who-are-you)
    -   [5. Everything can be imported](#5-everything-can-be-imported)
    -   [6. Build my own calculator!](#6-build-my-own-calculator)
    -   [7. Easy print](#7-easy-print)
    -   [8. ByteCode -> Python #3](#8-bytecode---python-3)
    -   [9. Fast alphabet](#9-fast-alphabet)
-   [How to Run](#how-to-run)
-   [Dependencies](#dependencies)
-   [Author](#author)

## Tasks

### 0. Import a simple function from a simple file

📦 Task: Write a Python script that imports the function `def add(a, b)` from a file named `add_0.py` and prints the result of the addition `1 + 2 = 3`.

### 1. My first toolbox!

🛠️ Task: Write a program that imports functions from the file `calculator_1.py` and prints the result of various operations (addition, subtraction, multiplication, division).

### 2. How to make a script dynamic!

📝 Task: Write a program that prints the number of and the list of its arguments.

### 3. Infinite addition

➕ Task: Write a program that prints the result of the addition of all arguments.

### 4. Who are you?

❓ Task: Write a program that prints all the names defined by the compiled module `hidden_4.pyc`.

### 5. Everything can be imported

📦 Task: Write a program that imports the variable `a` from a file named `variable_load_5.py` and prints its value.

### 6. Build my own calculator!

🧮 Task: Write a program that imports all functions from the file `calculator_1.py` and handles basic operations.

### 7. Easy print

🖨️ Task: Write a Python script that prints `#pythoniscool`, followed by a new line, without using the `print` function.

### 8. ByteCode -> Python #3

🔢 Task: Write the Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode:


```
 3           0 LOAD_CONST               1 (0)
              3 LOAD_CONST               2 (('add', 'sub'))
              6 IMPORT_NAME              0 (magic_calculation_102)
              9 IMPORT_FROM              1 (add)
             12 STORE_FAST               2 (add)
             15 IMPORT_FROM              2 (sub)
             18 STORE_FAST               3 (sub)
             21 POP_TOP

  4          22 LOAD_FAST                0 (a)
             25 LOAD_FAST                1 (b)
             28 COMPARE_OP               0 (<)
             31 POP_JUMP_IF_FALSE       94

  5          34 LOAD_FAST                2 (add)
             37 LOAD_FAST                0 (a)
             40 LOAD_FAST                1 (b)
             43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             46 STORE_FAST               4 (c)

  6          49 SETUP_LOOP              38 (to 90)
             52 LOAD_GLOBAL              3 (range)
             55 LOAD_CONST               3 (4)
             58 LOAD_CONST               4 (6)
             61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             64 GET_ITER
        >>   65 FOR_ITER                21 (to 89)
             68 STORE_FAST               5 (i)

  7          71 LOAD_FAST                2 (add)
             74 LOAD_FAST                4 (c)
             77 LOAD_FAST                5 (i)
             80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             83 STORE_FAST               4 (c)
             86 JUMP_ABSOLUTE           65
        >>   89 POP_BLOCK

  8     >>   90 LOAD_FAST                4 (c)
             93 RETURN_VALUE

 10     >>   94 LOAD_FAST                3 (sub)
             97 LOAD_FAST                0 (a)
            100 LOAD_FAST                1 (b)
            103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
            106 RETURN_VALUE
            107 LOAD_CONST               0 (None)
            110 RETURN_VALUE
```

### 9. Fast alphabet

🔤 Task: Write a Python script that prints the alphabet in uppercase, followed by a new line, without using loops or conditional statements.

## How to Run

1.  **Clone the repository:**
        
    `git clone https://github.com/Linf0rd/alx-higher_level_programming.git`
    
    `cd alx-higher_level_programming/0x02-python-import_modules` 
    
2.  **Run the Python scripts:**

    
    `python3 <script_name>.py` 
    

## Dependencies

-   **Python:**  Ensure you have Python installed.
    
    `sudo apt-get install python3` 
    

## Author

👨‍💻 Linf0rd