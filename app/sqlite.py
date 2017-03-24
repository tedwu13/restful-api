import sqlite3

connection = sqlite3.connect('example.db')

c = connection.cursor()

c.execute('''
          CREATE TABLE person
          (id INTEGER PRIMARY KEY ASC, name varchar(250) NOT NULL)
          ''')

c.execute('''
          CREATE TABLE address
          (id INTEGER PRIMARY KEY ASC, 
            street_name varchar(250) NOT NULL, 
            street_number varchar(250) NOT NULL,
            post_code varchar(250) NOT NULL,
            person_id INTEGER NOT NULL,
            FOREIGN KEY(person_id) REFERENCES person(id)
          )
          ''')

# # Python's SQLAlchemy and Declarative

# # There are three most important components in writing SQLAlchemy code:

# A Table that represents a table in a database.
# A mapper that maps a Python class to a table in a database.
# A class object that defines how a database record maps to a normal Python object.
# Instead of having to write code for Table, mapper and the class object at different places, SQLAlchemy's declarative allows a Table, a mapper and a class object to be defined at once in one class definition.

