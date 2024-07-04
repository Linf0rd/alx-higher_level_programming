
# 0x06. Python - Classes and Objects 🐍

Welcome to the Classes and Objects project of the ALX Higher-Level Programming curriculum! This repository contains tasks and scripts focused on object-oriented programming in Python, specifically creating and manipulating classes and objects.

## Table of Contents

-   [Tasks](#tasks)
    -   [0. My first square](#0-my-first-square)
    -   [1. Square with size](#1-square-with-size)
    -   [2. Size validation](#2-size-validation)
    -   [3. Area of a square](#3-area-of-a-square)
    -   [4. Access and update private attribute](#4-access-and-update-private-attribute)
    -   [5. Printing a square](#5-printing-a-square)
    -   [6. Coordinates of a square](#6-coordinates-of-a-square)
    -   [7. Singly linked list](#7-singly-linked-list)
    -   [8. Print Square instance](#8-print-square-instance)
    -   [9. Compare 2 squares](#9-compare-2-squares)
    -   [10. ByteCode -> Python #5](#10-bytecode---python-5)
-   [How to Run](#how-to-run)
-   [Dependencies](#dependencies)
-   [Author](#author)

## Tasks

### 0. My first square

🔳 Task: Write a class `Square` that defines a square.

### 1. Square with size

🔳 Task: Write a class `Square` that defines a square by its size.

### 2. Size validation

✅ Task: Write a class `Square` that validates the size of the square.

### 3. Area of a square

🔢 Task: Write a class `Square` that calculates the area of the square.

### 4. Access and update private attribute

🔄 Task: Write a class `Square` that provides getter and setter for the size.

### 5. Printing a square

🖨️ Task: Write a class `Square` that prints the square with the character `#`.

### 6. Coordinates of a square

📏 Task: Write a class `Square` that defines a square with coordinates.

### 7. Singly linked list

🔗 Task: Write a class `Node` that defines a node of a singly linked list.

### 8. Print Square instance

🖨️ Task: Write a class `Square` that prints a string representation of the square.

### 9. Compare 2 squares

🔢 Task: Write a class `Square` that compares two square instances.

### 10. ByteCode -> Python #5

🔢 Task: Write the Python class `MagicClass` that does exactly the same as the following Python bytecode:


```
Disassembly of __init__:
 10           0 LOAD_CONST               1 (0)
              3 LOAD_FAST                0 (self)
              6 STORE_ATTR               0 (_MagicClass__radius)

 11           9 LOAD_GLOBAL              1 (type)
             12 LOAD_FAST                1 (radius)
             15 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             18 LOAD_GLOBAL              2 (int)
             21 COMPARE_OP               9 (is not)
             24 POP_JUMP_IF_FALSE       60
             27 LOAD_GLOBAL              1 (type)
             30 LOAD_FAST                1 (radius)
             33 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             36 LOAD_GLOBAL              3 (float)
             39 COMPARE_OP               9 (is not)
             42 POP_JUMP_IF_FALSE       60

 12          45 LOAD_GLOBAL              4 (TypeError)
             48 LOAD_CONST               2 ('radius must be a number')
             51 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             54 RAISE_VARARGS            1
             57 JUMP_FORWARD             0 (to 60)

 13     >>   60 LOAD_FAST                1 (radius)
             63 LOAD_FAST                0 (self)
             66 STORE_ATTR               0 (_MagicClass__radius)
             69 LOAD_CONST               3 (None)
             72 RETURN_VALUE

Disassembly of area:
 17           0 LOAD_FAST                0 (self)
              3 LOAD_ATTR                0 (_MagicClass__radius)
              6 LOAD_CONST               1 (2)
              9 BINARY_POWER
             10 LOAD_GLOBAL              1 (math)
             13 LOAD_ATTR                2 (pi)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE

Disassembly of circumference:
 21           0 LOAD_CONST               1 (2)
              3 LOAD_GLOBAL              0 (math)
              6 LOAD_ATTR                1 (pi)
              9 BINARY_MULTIPLY
             10 LOAD_FAST                0 (self)
             13 LOAD_ATTR                2 (_MagicClass__radius)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE
```

## How to Run

1.  **Clone the repository:**
        
    `git clone https://github.com/Linf0rd/alx-higher_level_programming.git`
    
    `cd alx-higher_level_programming/0x06-python-classes` 
    
2.  **Run the Python scripts:**
    
    `python3 <script_name>.py` 
    

## Dependencies

-   **Python:**  Ensure you have Python installed.
        
    `sudo apt-get install python3` 
    

## Author

👨‍💻 Linf0rd