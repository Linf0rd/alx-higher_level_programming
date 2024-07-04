# 0x01. Python - if/else, loops, functions 🐍

Welcome to the If/Else, Loops, Functions project of the ALX Higher-Level Programming curriculum! This repository contains tasks and scripts that dive into Python control flow, including conditional statements, loops, and defining functions.

## Table of Contents

-   [Tasks](#tasks)
    -   [0. Positive anything is better than negative nothing](#0-positive-anything-is-better-than-negative-nothing)
    -   [1. The last digit](#1-the-last-digit)
    -   [2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game](#2-i-sometimes-suffer-from-insomnia-and-when-i-cant-fall-asleep-i-play-what-i-call-the-alphabet-game)
    -   [3. When I was having that alphabet soup, I never thought that it would pay off](#3-when-i-was-having-that-alphabet-soup-i-never-thought-that-it-would-pay-off)
    -   [4. Hexadecimal printing](#4-hexadecimal-printing)
    -   [5. 00...99](#5-0099)
    -   [6. Inventing is a combination of brains and materials. The more brains you use, the less material you need](#6-inventing-is-a-combination-of-brains-and-materials-the-more-brains-you-use-the-less-material-you-need)
    -   [7. islower](#7-islower)
    -   [8. To uppercase](#8-to-uppercase)
    -   [9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important](#9-there-are-only-3-colors-10-digits-and-7-notes-its-what-we-do-with-them-thats-important)
    -   [10. a + b](#10-a--b)
    -   [11. a ^ b](#11-a--b)
    -   [12. Fizz Buzz](#12-fizz-buzz)
    -   [13. Insert in sorted linked list](#13-insert-in-sorted-linked-list)
    -   [14. Smile in the mirror](#14-smile-in-the-mirror)
    -   [15. Remove at position](#15-remove-at-position)
    -   [16. ByteCode -> Python #2](#16-bytecode---python-2)
-   [How to Run](#how-to-run)
-   [Dependencies](#dependencies)
-   [Author](#author)

## Tasks

### 0. Positive anything is better than negative nothing

🔢 Task: Complete a source code in Python to print whether the number stored in the variable `number` is positive or negative.

### 1. The last digit

🔢 Task: Complete a source code in Python to print the last digit of the number stored in the variable `number`.

### 2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game

🔠 Task: Write a Python script that prints the ASCII alphabet in lowercase, not followed by a new line.

### 3. When I was having that alphabet soup, I never thought that it would pay off

🔠 Task: Write a Python script that prints the ASCII alphabet in lowercase, except `q` and `e`, not followed by a new line.

### 4. Hexadecimal printing

📝 Task: Write a Python script that prints all numbers from 0 to 98 in decimal and in hexadecimal.

### 5. 00...99

🔢 Task: Write a Python script that prints numbers from 0 to 99.

### 6. Inventing is a combination of brains and materials. The more brains you use, the less material you need

📏 Task: Write a Python script that prints all possible different combinations of two digits.

### 7. islower

🔡 Task: Write a function in Python that checks for lowercase characters.

### 8. To uppercase

🔠 Task: Write a function in Python that prints a string in uppercase followed by a new line.

### 9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important

🔢 Task: Write a function in Python that prints the last digit of a number.

### 10. a + b

➕ Task: Write a function in Python that adds two integers and returns the result.

### 11. a ^ b

✖️ Task: Write a function in Python that computes `a` to the power of `b` and returns the value.

### 12. Fizz Buzz

🔢 Task: Write a function in Python that prints the numbers from 1 to 100, but for multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz".

### 13. Insert in sorted linked list

🔗 Task: Write a function in C that inserts a number into a sorted singly linked list.

### 14. Smile in the mirror

🪞 Task: Write a Python script that prints the ASCII alphabet in reverse order, alternating lowercase and uppercase (z in lowercase and Y in uppercase) not followed by a new line.

### 15. Remove at position

🔢 Task: Write a function in Python that removes a character at the position `n` of a string.

### 16. ByteCode -> Python #2

🔢 Task: Write the Python function `def magic_calculation(a, b, c):` that does exactly the same as the following Python bytecode:


```
  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
```

## How to Run

1.  **Clone the repository:**
        
    `git clone https://github.com/Linf0rd/alx-higher_level_programming.git`
    
    `cd alx-higher_level_programming/0x01-python-if_else_loops_functions` 
    
2.  **Run the Python scripts:**
        
    `python3 <script_name>.py` 
    

## Dependencies

-   **Python:**  Ensure you have Python installed.
        
    `sudo apt-get install python3` 
    

## Author

👨‍💻 Linf0rd