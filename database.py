import sqlite3
try:
    connect = sqlite3.connect("data2.db", timeout=10)
    cursor = connect.cursor()

    cursor.execute("UPDATE COMPANY set AGE = 20 WHERE ID = 2")
    connect.commit()
    print("Record Updated Successfully");
except sqlite3.Error as e:
    print(f"SQL Lite Error as {e}")

finally:
    if connect:
        connect.close()
