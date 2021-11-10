import mysql
from mysql.connector import Error


def connect():
    """Connect to MySQL database"""
    conn = None
    try:
        conn = mysql.connector.connect(
            host="localhost", database="CT", user="root", password="rraug27$"
        )
        if conn.is_connected():
            cur = conn.cursor()

            insert_stat = """
                    SELECT * FROM CT.users; 
                """
            cur.execute(insert_stat)

            rows = cur.fetchall()
            print(rows)

            print("Connected to MySQL database")

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == "__main__":
    connect()
