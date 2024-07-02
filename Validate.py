import sqlite3

# Create an SQLite database (you can choose a different database system if needed)
conn = sqlite3.connect("SERIALNUMBERS6262.db")
cursor = conn.cursor()

# Create a table for serial numbers
cursor.execute("""
    CREATE TABLE IF NOT EXISTS serial_numbers (
        id INTEGER PRIMARY KEY,
        serial_number TEXT UNIQUE,
        product_name TEXT,
        manufacturing_date DATE,
        manufacturer TEXT,
        status TEXT
    )
""")
conn.commit()

def add_serial_number(serial_number, product_name, manufacturing_date, manufacturer):
    try:
        cursor.execute("""
            INSERT INTO serial_numbers (serial_number, product_name, manufacturing_date, manufacturer, status)
            VALUES (?, ?, ?, ?, ?)
        """, (serial_number, product_name, manufacturing_date, manufacturer, "active"))
        conn.commit()
        print(f"Serial number {serial_number} added successfully.")
    except sqlite3.IntegrityError:
        print(f"Serial number {serial_number} already exists in the database.")

def validate_serial_number(serial_number):
    cursor.execute("SELECT COUNT(*) FROM serial_numbers WHERE serial_number = ?", (serial_number,))
    count = cursor.fetchone()[0]
    if count > 0:
        print(f"Serial number {serial_number} is valid.")
    else:
        print(f"Serial number {serial_number} does not exist in the database.")

# Example usage
add_serial_number("ABC123", "Widget A", "2024-07-01", "Company X")
validate_serial_number("ABC123")

# Close the database connection
conn.close()
