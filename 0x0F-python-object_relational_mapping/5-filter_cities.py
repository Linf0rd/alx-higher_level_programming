#!/usr/bin/python3
"""
Script that lists all cities of a state from the database hbtn_0e_4_usa.
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
        db=sys.argv[3],
    )

    cursor = db.cursor()

    cursor.execute(
        """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """,
        (state_name,),
    )

    cities = [row[0] for row in cursor.fetchall()]

    print(", ".join(cities))

    cursor.close()

    db.close()


if __name__ == "__main__":
    main()
