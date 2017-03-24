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

