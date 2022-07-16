import psycopg2


connection = psycopg2.connect(
    user='postgres',
    password='asif2017',
    host='localhost',
    port='5432',
    database='hospital_db'
)


cursor = connection.cursor()


query = """
    CREATE TABLE department (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL
    );
"""


query = """
    CREATE TABLE doctor (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        department_id INTEGER NOT NULL,
        CONSTRAINT fk_department_id
        FOREIGN KEY (department_id)
        REFERENCES department (id)
        ON DELETE CASCADE
    );
"""


query = """
    CREATE TABLE category (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL
    );
"""


query = """
    CREATE TABLE post (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        doctor_id INTEGER NOT NULL,
        category_id INTEGER NOT NULL,
        FOREIGN KEY (doctor_id) REFERENCES doctor (id),  
        FOREIGN KEY (category_id) REFERENCES category (id) 
    );
"""


cursor.execute(query)
connection.commit()



