import sqlite3

# Create/Open database file
database = "school.db"

conn = sqlite3.connect(database)

print("Database created successfully")

cursor = conn.cursor()

# Create Students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Students(
    Student_ID INTEGER PRIMARY KEY,
    Name TEXT,
    Class TEXT,
    Age INTEGER
);
""")

# Create Teachers table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Teachers(
    Teacher_ID INTEGER PRIMARY KEY,
    Name TEXT,
    Subject TEXT,
    Salary REAL
);
""")

conn.commit()

print("Tables created successfully")

conn.close()

print("Database closed")