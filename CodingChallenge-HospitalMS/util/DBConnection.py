import pyodbc
try:
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=SRIDHAR/LOCALHOST;'
                          'Database=HospitalManagementSystem;'
                          'Trusted_Connection=yes;')
    print("Connected Successfully")
except pyodbc.Error as e:
    print("Connection failed:", e)
    exit()
c = conn.cursor()
# Adjust your SQL query to select data from a table
sql_query = "SELECT * FROM doctor"  # Replace YourTableName with the actual table name
c.execute(sql_query)
data = c.fetchall()
for row in data:
    print(row[0], " ", row[1], " ", row[3])

c.close()
conn.close()

