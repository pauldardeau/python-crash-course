import sqlite3
import sys


# online docs: https://docs.python.org/3/library/sqlite3.html

db_file_path = "testdb.sqlite3"

try:
    conn = sqlite3.connect(db_file_path)
except Error as e:
    print("error: unable to open database")
    print(e)
    sys.exit(1)


if conn is not None:
    cur = conn.cursor()

    # create table if it doesn't already exist
    sql = "CREATE TABLE IF NOT EXISTS movie (" + \
             "name text PRIMARY KEY NOT NULL," + \
             "year integer NOT NULL," + \
             "genre text NOT NULL" + \
          ");"
    cur.execute(sql)
    cur.close()

    # insert some movies
    sql = "INSERT INTO movie (name,year,genre) " + \
          "VALUES (?,?,?)"

    cur = conn.cursor()
    cur.execute(sql, ["Planet of the Apes", 1968, "scifi"])
    cur.execute(sql, ["2001: A Space Odyssey", 1968, "scifi"])
    cur.execute(sql, ["The War of the Worlds", 1953, "scifi"])
    cur.execute(sql, ["Ferris Bueller's Day Off", 1986, "comedy"])
    conn.commit()
    cur.close()

    # query movies of a particular genre
    sql = "SELECT name, year " + \
          "FROM movie " + \
          "WHERE genre = ?"

    cur = conn.cursor()
    res = cur.execute(sql, ["scifi"])
    rows = res.fetchall()

    for row in rows:
        print("%s %d" % (row[0], row[1]))
    cur.close()

    conn.close()

