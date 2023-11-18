#!/usr/bin/python3
"""
Script that lists all states with a name starting with N from the database
hbtn_0e_0_usa
"""

import sys
import MySQLdb


def main():
    """
    Main function
    """


    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    )

    for row in cursor.fetchall():
        print(row)

    cursor.close()

    db.close()

if __name__ == "__main__":
    main()
