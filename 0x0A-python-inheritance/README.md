
# 0x0A. Python - Inheritance 🧬

Welcome to the Python - Inheritance project of the ALX Higher-Level Programming curriculum! This repository contains tasks focused on understanding and implementing inheritance in Python, including creating subclasses, using `super()`, and overriding methods.

## Table of Contents

-   [Tasks](#tasks)
    -   [0. Lookup](#0-lookup)
    -   [1. My list](#1-my-list)
    -   [2. Exact same object](#2-exact-same-object)
    -   [3. Same class or inherit from](#3-same-class-or-inherit-from)
    -   [4. Only sub class of](#4-only-sub-class-of)
    -   [5. Geometry module](#5-geometry-module)
    -   [6. Improve Geometry](#6-improve-geometry)
    -   [7. Integer validator](#7-integer-validator)
    -   [8. Rectangle](#8-rectangle)
    -   [9. Full rectangle](#9-full-rectangle)
    -   [10. Square #1](#10-square-1)
    -   [11. Square #2](#11-square-2)
    -   [12. My integer](#12-my-integer)
    -   [13. Can I?](#13-can-i)
-   [How to Run](#how-to-run)
-   [Dependencies](#dependencies)
-   [Author](#author)

## Tasks

### 0. Lookup

🔍 Task: Write a function that returns the list of available attributes and methods of an object.

### 1. My list

📝 Task: Write a class `MyList` that inherits from `list`. Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort).

### 2. Exact same object

📋 Task: Write a function that returns `True` if the object is exactly an instance of the specified class; otherwise `False`.

### 3. Same class or inherit from

🧩 Task: Write a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise `False`.

### 4. Only sub class of

🧬 Task: Write a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise `False`.

### 5. Geometry module

📏 Task: Write an empty class `BaseGeometry`.

### 6. Improve Geometry

⚙️ Task: Write a class `BaseGeometry` with a public instance method `def area(self):` that raises an `Exception` with the message `area() is not implemented`.

### 7. Integer validator

🔍 Task: Write a class `BaseGeometry` with a public instance method `def area(self):` and a method `def integer_validator(self, name, value):` that validates `value`.

### 8. Rectangle

🛠️ Task: Write a class `Rectangle` that inherits from `BaseGeometry`. Initialization with `width` and `height` must be validated by `integer_validator`.

### 9. Full rectangle

🏠 Task: Write a class `Rectangle` that inherits from `BaseGeometry`. Implement the `__str__` method to print the rectangle description.

### 10. Square #1

🏡 Task: Write a class `Square` that inherits from `Rectangle`. Initialization with `size` must be validated by `integer_validator`.

### 11. Square #2

🔲 Task: Write a class `Square` that inherits from `Rectangle`. Implement the `__str__` method to print the square description.

### 12. My integer

🔢 Task: Write a class `MyInt` that inherits from `int`. `MyInt` is a rebel. `MyInt` has `==` and `!=` operators inverted.

### 13. Can I?

🔍 Task: Write a function that adds a new attribute to an object if it’s possible.

## How to Run

1.  **Clone the repository:**
    
    `git clone https://github.com/Linf0rd/alx-higher_level_programming.git`
    
    `cd alx-higher_level_programming/0x0A-python-inheritance` 
    
2.  **Run the Python scripts:**
        
    `python3 <script_name>.py` 
    

## Dependencies

-   **Python:**  Ensure you have Python installed.
        
    `sudo apt-get install python3` 
    

## Author

👨‍💻 Linf0rd