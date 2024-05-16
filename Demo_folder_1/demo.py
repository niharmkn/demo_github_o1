import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Get user input
user_input = input("Enter a username: ")

# Construct the SQL query with user input (Vulnerable to SQL injection)
query = "SELECT * FROM users WHERE username = '" + user_input + "'"

# Execute the query
cursor.execute(query)

# Fetch the results
results = cursor.fetchall()

# Display the results
for row in results:
    print(row)

# Close the connection
conn.close()
