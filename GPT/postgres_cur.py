import psycopg2
conn = psycopg2.connect(database="public.accounts",
                        host="localhost",
                        user="postgres",
                        password="postgres",
                        port=5433)

cursor = conn.cursor()

# Required SQL command execution
cursor.execute("SELECT * FROM accounts")

# Retrive all the rows
cursor.fetchall()

# # Retrive first row
# cursor.fetchone()

# # Retrive Specific No. of Rows
# cursor.fetchmany(size=2)
