
# 0x09. Python - Everything is Object 🧩

Welcome to the Everything is Object project of the ALX Higher-Level Programming curriculum! This repository contains tasks and scripts focused on understanding Python's object model, references, and the differences between mutable and immutable types.

## Table of Contents

-   [Tasks](#tasks)
    -   [0. Who am I?](#0-who-am-i)
    -   [1. Where are you?](#1-where-are-you)
    -   [2. Right count](#2-right-count)
    -   [3. Right count =](#3-right-count-)
    -   [4. Right count =](#4-right-count-)
    -   [5. Right count =+](#5-right-count-)
    -   [6. Is equal](#6-is-equal)
    -   [7. Is the same](#7-is-the-same)
    -   [8. Is really equal](#8-is-really-equal)
    -   [9. Is really the same](#9-is-really-the-same)
    -   [10. And with a list, is it equal](#10-and-with-a-list-is-it-equal)
    -   [11. And with a list, is it the same](#11-and-with-a-list-is-it-the-same)
    -   [12. And with a list, is it really equal](#12-and-with-a-list-is-it-really-equal)
    -   [13. And with a list, is it really the same](#13-and-with-a-list-is-it-really-the-same)
    -   [14. List append](#14-list-append)
    -   [15. List add](#15-list-add)
    -   [16. Integer incrementation](#16-integer-incrementation)
    -   [17. List incrementation](#17-list-incrementation)
    -   [18. List assignation](#18-list-assignation)
    -   [19. Copy a list object](#19-copy-a-list-object)
    -   [20. Tuple or not?](#20-tuple-or-not)
    -   [21. Tuple or not?](#21-tuple-or-not)
    -   [22. Tuple or not?](#22-tuple-or-not)
    -   [23. Tuple or not?](#23-tuple-or-not)
    -   [24. Who I am?](#24-who-i-am)
    -   [25. Tuple or not](#25-tuple-or-not)
    -   [26. Empty is not empty](#26-empty-is-not-empty)
    -   [27. Still the same?](#27-still-the-same)
    -   [28. Same or not?](#28-same-or-not)
    -   [29. #pythonic](#29-pythonic)
    -   [30. Low memory cost](#30-low-memory-cost)
    -   [31. int 1/3](#31-int-13)
    -   [32. int 2/3](#32-int-23)
    -   [33. int 3/3](#33-int-33)
    -   [34. Clear strings](#34-clear-strings)
-   [How to Run](#how-to-run)
-   [Dependencies](#dependencies)
-   [Author](#author)

## Tasks

### 0. Who am I?

🔍 Task: Print the type of an object.

### 1. Where are you?

📍 Task: Print the memory address of an object.

### 2. Right count

🔢 Task: Verify if a string can be converted to an integer.

### 3. Right count =

🔢 Task: Create a function that assigns an integer value to a variable.

### 4. Right count =

🔢 Task: Create a function that assigns a variable to another variable.

### 5. Right count =+

🔢 Task: Create a function that adds an integer to a variable.

### 6. Is equal

🔍 Task: Compare two objects using `==`.

### 7. Is the same

🔍 Task: Compare two objects using `is`.

### 8. Is really equal

🔍 Task: Compare two lists using `==`.

### 9. Is really the same

🔍 Task: Compare two lists using `is`.

### 10. And with a list, is it equal

🔍 Task: Create a list and compare it using `==`.

### 11. And with a list, is it the same

🔍 Task: Create a list and compare it using `is`.

### 12. And with a list, is it really equal

🔍 Task: Compare two identical lists using `==`.

### 13. And with a list, is it really the same

🔍 Task: Compare two identical lists using `is`.

### 14. List append

🔧 Task: Append an element to a list and print it.

### 15. List add

🔧 Task: Concatenate two lists and print them.

### 16. Integer incrementation

➕ Task: Increment an integer and print it.

### 17. List incrementation

➕ Task: Increment a list and print it.

### 18. List assignation

📑 Task: Assign a list to another variable and print it.

### 19. Copy a list object

📑 Task: Copy a list using slicing.

### 20. Tuple or not?

🔍 Task: Check if an object is a tuple.

### 21. Tuple or not?

🔍 Task: Check if an object with a single element is a tuple.

### 22. Tuple or not?

🔍 Task: Check if an object with multiple elements is a tuple.

### 23. Tuple or not?

🔍 Task: Check if an object with trailing comma is a tuple.

### 24. Who I am?

🔍 Task: What does this script print?


```
a = (1)
b = (1)
a is b
```

### 25. Tuple or not

🔍 Task: What does this script print?


```
a = (1, 2)
b = (1, 2)
a is b
```

### 26. Empty is not empty

🔍 Task: What does this script print?


```
a = ()
b = ()
a is b
```

### 27. Still the same?

🔍 Task: Will the last line of this script print `139926795932424`? Answer with Yes or No.


```
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```

### 28. Same or not?

🔍 Task: Will the last line of this script print `139926795932424`? Answer with Yes or No.


```
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```

### 29. #pythonic

🪄 Task: Write a function `magic_string()` that returns a string "BestSchool" n times the number of the iteration.

### 30. Low memory cost

🪄 Task: Write a class `LockedClass` with no class or object attribute that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called `first_name`.

### 31. int 1/3

🔍 Task: Assuming we are using a CPython implementation of Python3 with default options/configuration, how many int objects are created by the execution of the first and second line of the script?

```
a = 1
b = 1
```

### 32. int 2/3

🔍 Task: Assuming we are using a CPython implementation of Python3 with default options/configuration, how many int objects are created by the execution of each line, and are the int objects pointed by `a` and `b` deleted?

```
a = 1024
b = 1024
del a
del b
c = 1024
```

### 33. int 3/3

🔍 Task: Assuming we are using a CPython implementation of Python3 with default options/configuration, before the execution of line 2 (print("Love")), how many int objects have been created and are still in memory?

```
lol@admin:/tmp/so$ cat int.py 
print("I")
print("Love")
print("Python")
```

### 34. Clear strings

🔍 Task: Assuming we are using a CPython implementation of Python3 with default options/configuration, how many string objects are created by the execution of each line, and are the string objects pointed by `a` and `b` deleted?

```
admin@ubuntu:/python3$ cat string.py 
a = "SCHL"
b = "SCHL"
del a
del b
c = "SCHL"
```

## How to Run

1.  **Clone the repository:**
        
    `git clone https://github.com/Linf0rd/alx-higher_level_programming.git`
    
    `cd alx-higher_level_programming/0x09-python-everything_is_object` 
    
2.  **Run the Python scripts:**
        
    `python3 <script_name>.py` 
    

## Dependencies

-   **Python:**  Ensure you have Python installed.
   
    `sudo apt-get install python3` 
    

## Author

👨‍💻 Linf0rd