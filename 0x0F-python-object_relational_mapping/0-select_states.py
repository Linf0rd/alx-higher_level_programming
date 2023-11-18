#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def main():
    """
    Main function
    """

    username = input("Enter username: ")
    password = input("Enter password: ")
    database = input("Enter database name: ")

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    for row in cursor.fetchall():
        print(row)

    cursor.close()

    db.close()


if __name__ == "__main__":
    main()
