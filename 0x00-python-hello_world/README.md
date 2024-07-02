
# 0x00. Python - Hello, World 🌍

Welcome to the Python Hello World project of the ALX Higher-Level Programming curriculum! This repository contains tasks and scripts that introduce the basics of Python programming, from writing simple scripts to understanding the intricacies of Python syntax and execution.

## Table of Contents

-   [Tasks](#tasks)
    -   [0. Run Python file](#0-run-python-file)
    -   [1. Run inline](#1-run-inline)
    -   [2. Hello, print](#2-hello-print)
    -   [3. Print integer](#3-print-integer)
    -   [4. Print float](#4-print-float)
    -   [5. Print string](#5-print-string)
    -   [6. Play with strings](#6-play-with-strings)
    -   [7. Copy - Cut - Paste](#7-copy---cut---paste)
    -   [8. Create a new sentence](#8-create-a-new-sentence)
    -   [9. Easter Egg](#9-easter-egg)
    -   [10. Linked list cycle](#10-linked-list-cycle)
    -   [11. Hello, write](#11-hello-write)
    -   [12. Compile](#12-compile)
    -   [13. ByteCode -> Python #1](#13-bytecode---python-1)
-   [How to Run](#how-to-run)
-   [Dependencies](#dependencies)
-   [Author](#author)

## Tasks

### 0. Run Python file

🔧 Task: Write a Shell script that runs a Python script. The Python file name will be saved in the environment variable `$PYFILE`.

### 1. Run inline

🛠️ Task: Write a Shell script that runs Python code. The Python code will be saved in the environment variable `$PYCODE`.

### 2. Hello, print

👋 Task: Write a Python script that prints exactly "Programming is like building a multilingual puzzle", followed by a new line.

### 3. Print integer

🔢 Task: Complete a source code in Python to print the integer stored in the variable `number`, followed by "Battery street", followed by a new line.

### 4. Print float

💧 Task: Complete a source code in Python to print the float stored in the variable `number` with a precision of 2 digits.

### 5. Print string

📝 Task: Complete a source code in Python to print a string stored in the variable `str` three times, followed by its first 9 characters.

### 6. Play with strings

🔠 Task: Complete a source code in Python to print `Welcome to Holberton School!` by concatenating strings stored in variables.

### 7. Copy - Cut - Paste

✂️ Task: Complete a source code in Python to copy, cut, and paste parts of a string.

### 8. Create a new sentence

🖋️ Task: Complete a source code in Python to print `object-oriented programming with Python` followed by a new line.

### 9. Easter Egg

🥚 Task: Write a Python script that prints "The Zen of Python" by Tim Peters, followed by a new line.

### 10. Linked list cycle

🔗 Task: Write a function in C that checks if a singly linked list has a cycle in it.

### 11. Hello, write

📜 Task: Write a Python script that prints exactly "and that piece of art is useful - Dora Korpar, 2015-10-19", followed by a new line.

-   Use the function  `write`  from the  `sys`  module
-   You are not allowed to use  `print`
-   Your script should print to  `stderr`
-   Your script should exit with the status code 1

### 12. Compile

⚙️ Task: Write a script that compiles a Python script file.

-   The Python file name will be stored in the environment variable  `$PYFILE`
-   The output filename has to be  `$PYFILEc`  (e.g.,  `export PYFILE=my_main.py`  => output filename:  `my_main.pyc`)

### 13. ByteCode -> Python #1

🔢 Task: Write the Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode:


 
 
              3 LOAD_CONST		 1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE 

## How to Run

1.  **Clone the repository:**
        
    `git clone https://github.com/Linf0rd/alx-higher_level_programming.git`
    
    `cd alx-higher_level_programming/0x00-python-hello_world` 
    
2.  **Run the Python scripts:**
       
    `python3 <script_name>.py` 
    

## Dependencies

-   **Python:**  Ensure you have Python installed.
        
    `sudo apt-get install python3` 
    

## Author

👨‍💻 Linf0rd
