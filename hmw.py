import psycopg2


connection = psycopg2.connect(
    user='postgres',
    password='asif2017',
    host='localhost',
    port='5432',
    database='work'
)


cursor = connection.cursor()


query = '''
CREATE TABLE     work (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    salary INT,
    exp_date DATE NOT NULL,
    lang BOOLEAN,
    company VARCHAR(100)
);
'''


def show(cursor):
    print(*[desc[0].ljust(10) for desc in cursor.description], sep='')
    print('-'*80)
    print('\n'.join(' - '.join(str(z)  for z in i) for i in cursor.fetchall()))


info_list = [
    # basliq, sirket, maas, bitme tarixi, xarici dil telebi
    ('iOS developer', 'A2Z Technologies', 3500, '2022-07-18', True),
    ('Tender üzrə mütəxəssis', 'A2Z Technologies', 1500, '2022-06-11', False),
    ('Məlumat bazası üzrə inzibatçı', 'ABB ASC', 1500, '2022-07-12', True),
    ('Database Administrator', 'A2Z Technologies', 2500, '2022-07-14', True),
    ('Front-End Developer', 'AzəriMed QSC', 1500, '2022-07-23', False),
    ('Proqram təminatının testləşdirilməsi üzrə mühəndis',
     'ABB ASC', 1500, '2022-08-10', False),
    ('Back-end üzrə proqramçı', 'ABB ASC', 4100, '2022-07-11', True),
    ('Biznes analitika üzrə Baş mütəxəssis ', 'ABB ASC', 2200, '2022-07-03', True),
    ('Android proqramçı', 'ABB ASC', 1300, '2022-07-22', True),
    ('Front-end üzrə proqramçı', 'ABB ASC', 3200, '2022-07-06', True),
    ('Full stack PHP proqramçı', 'AzəriMed QSC', 2400, '2022-07-17', False),
    ('Avtomatlaşdırılmış əməliyyat sistemi üzrə proqramçı',
     'ABB ASC', 2700, '2022-07-15', True),
    ('Proqram təminatı üzrə mühəndis', 'Kontakt Home', 2700, '2022-07-13', False),
    ('Hüquqşünas', 'Kontakt Home', 1500, '2022-07-03', False),
    ('Çatdırılma xidmətləri üzrə fəhlə', 'Kontakt Home', 500, '2022-07-15', True),
    ('PHP developer', 'ARIS', 1500, '2022-07-11', True),
    ('Məhsul üzrə menecer', 'Kontakt Home', 2800, '2022-07-05', True),
    ('Proqram təminatı üzrə aparıcı mühəndis',
     'Kontakt Home', 2500, '2022-07-02', False),
    ('İT sənədləşməsi üzrə mütəxəssis', 'Azericard', 1500, '2022-07-25', True),
    ('Information Security Specialist', 'DEFSCOPE LLC', 2500, '2022-07-03', False),
    ('IT Helpdesk', 'Azericard', 1500, '2022-07-30', True),
    ('Cybersecurity Business Development Internship',
     'DEFSCOPE LLC', 2900, '2022-07-19', False),
    ('Vue.js developer', 'ARIS', 1500, '2022-07-29', True),
]


query = '''
INSERT INTO work (title, company, salary, exp_date, lang) VALUES(%s, %s, %s, %s, %s);
'''

for info in info_list:
    cursor.execute(query, info)


query = '''
UPDATE work SET salary = salary*1.15 WHERE salary<2000 AND exp_date>'2022-07-10';
'''

query = '''
DELETE FROM work WHERE company LIKE '%PHP%';
'''

query = '''
SELECT company, ROUND(AVG(salary)) FROM work WHERE exp_date>'2022-07-14' GROUP BY company HAVING ROUND(AVG(salary))>2000;
'''

# query = '''
# SELECT * FROM work;
# '''


cursor.execute(query)
show(cursor)
# connection.commit()


