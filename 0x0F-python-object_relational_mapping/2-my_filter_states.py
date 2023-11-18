#!/usr/bin/python3
"""Script that displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import MySQLdb
import sys


def main():
    """
    Main function
    """

    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[4],
    )

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
            state_name
        )
    )

    for row in cursor.fetchall():
        print(row)

    cursor.close()

    db.close()


if __name__ == "__main__":
    main()
