import sqlite3
db = sqlite3.connect('/Users/alexnenkov/Desktop/School/Y1/Intro to Databases/SQLite 3/MySportFinal.db')
cursor = db.cursor()
sql_query = "SELECT * \
		   FROM emp"
cursor.execute(sql_query)
all_emp_rows = cursor.fetchall()
for emp_row in all_emp_rows:
    print(emp_row)
db.close()

