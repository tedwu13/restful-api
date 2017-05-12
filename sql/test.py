import sqlite3

# connection to sql lite
# sql lite occupies a single file that has all the data
# substantially slower than SQL
connection = sqlite3.connect('data.db')


cursor = connection.cursor()

# CREATE TABLE ___table_name____
create_table = "CREATE TABLE users (id int, username text, password text)"
# this is a schema or how data is going to look like
cursor.execute(create_table)

#insert one user into users table
user = (1, 'ted wu', 'asdf')
insert_query = "INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert_query, user)


# insert multiple users into users table

users = [
    (1, 'ted1', 'asdf'),
    (2, 'ted2', 'asdf'),
    (3, 'ted3', 'asdf'),
]

cursor.executemany(insert_query, users)

select_query = "SELECT * from users"

for row in cursor.execute(select_query):
    print(row)

# save all of the changes into data.db
connection.commit()

connection.close()
