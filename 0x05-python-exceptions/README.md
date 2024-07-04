
# 0x05. Python - Exceptions 🚨

Welcome to the Python Exceptions project of the ALX Higher-Level Programming curriculum! This repository contains tasks and scripts focused on handling errors and exceptions in Python, ensuring robust and fault-tolerant code.

## Table of Contents

-   [Tasks](#tasks)
    -   [0. Safe list printing](#0-safe-list-printing)
    -   [1. Safe printing of an integers list](#1-safe-printing-of-an-integers-list)
    -   [2. Print and count integers](#2-print-and-count-integers)
    -   [3. Integers division with debug](#3-integers-division-with-debug)
    -   [4. Divide a list](#4-divide-a-list)
    -   [5. Raise exception](#5-raise-exception)
    -   [6. Raise a message](#6-raise-a-message)
    -   [7. Safe integer print with error message](#7-safe-integer-print-with-error-message)
    -   [8. Safe function](#8-safe-function)
    -   [9. ByteCode -> Python #4](#9-bytecode---python-4)
-   [How to Run](#how-to-run)
-   [Dependencies](#dependencies)
-   [Author](#author)

## Tasks

### 0. Safe list printing

🔢 Task: Write a function that prints `x` elements of a list and only integers.

### 1. Safe printing of an integers list

🔢 Task: Write a function that prints an integer list and only the integers.

### 2. Print and count integers

🔢 Task: Write a function that prints the first `x` elements of a list and returns the number of integers printed.

### 3. Integers division with debug

➗ Task: Write a function that divides 2 integers and prints the result.

### 4. Divide a list

➗ Task: Write a function that divides element by element 2 lists.

### 5. Raise exception

🚨 Task: Write a function that raises a type exception.

### 6. Raise a message

🚨 Task: Write a function that raises a name exception with a message.

### 7. Safe integer print with error message

🔢 Task: Write a function that prints an integer or raises an exception with a message.

### 8. Safe function

🔧 Task: Write a function that executes a function safely.

### 9. ByteCode -> Python #4

🔢 Task: Write the Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode:


```
  3           0 LOAD_CONST               1 (0)
              3 STORE_FAST               2 (result)

  4           6 SETUP_LOOP              94 (to 103)
              9 LOAD_GLOBAL              0 (range)
             12 LOAD_CONST               2 (1)
             15 LOAD_CONST               3 (3)
             18 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             21 GET_ITER
        >>   22 FOR_ITER                77 (to 102)
             25 STORE_FAST               3 (i)

  5          28 SETUP_EXCEPT            49 (to 80)

  6          31 LOAD_FAST                3 (i)
             34 LOAD_FAST                0 (a)
             37 COMPARE_OP               4 (>)
             40 POP_JUMP_IF_FALSE       58

  7          43 LOAD_GLOBAL              1 (Exception)
             46 LOAD_CONST               4 ('Too far')
             49 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             52 RAISE_VARARGS            1
             55 JUMP_FORWARD            18 (to 76)

  9     >>   58 LOAD_FAST                2 (result)
             61 LOAD_FAST                0 (a)
             64 LOAD_FAST                1 (b)
             67 BINARY_POWER
             68 LOAD_FAST                3 (i)
             71 BINARY_TRUE_DIVIDE
             72 INPLACE_ADD
             73 STORE_FAST               2 (result)
        >>   76 POP_BLOCK
             77 JUMP_ABSOLUTE           22

 10     >>   80 POP_TOP
             81 POP_TOP
             82 POP_TOP

 11          83 LOAD_FAST                1 (b)
             86 LOAD_FAST                0 (a)
             89 BINARY_ADD
             90 STORE_FAST               2 (result)

 12          93 BREAK_LOOP
             94 POP_EXCEPT
             95 JUMP_ABSOLUTE           22
             98 END_FINALLY
             99 JUMP_ABSOLUTE           22
        >>  102 POP_BLOCK

 13     >>  103 LOAD_FAST                2 (result)
            106 RETURN_VALUE
```

## How to Run

1.  **Clone the repository:**
        
    `git clone https://github.com/Linf0rd/alx-higher_level_programming.git`
    
    `cd alx-higher_level_programming/0x05-python-exceptions` 
    
2.  **Run the Python scripts:**
        
    `python3 <script_name>.py` 
    

## Dependencies

-   **Python:**  Ensure you have Python installed.
        
    `sudo apt-get install python3` 
    

## Author

👨‍💻 Linf0rd