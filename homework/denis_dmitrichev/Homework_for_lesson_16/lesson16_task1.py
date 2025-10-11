import mysql.connector as mysql
import os
import dotenv
import csv

dotenv.load_dotenv()

db = mysql.connect(
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    database=os.getenv('DB_NAME'),
)

cursor = db.cursor()

select_query3 = '''
SELECT
*
FROM students s
JOIN `groups` g ON g.id = s.group_id
JOIN books b ON b.taken_by_student_id = s.id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON l.id = m.lesson_id
JOIN subjects sb ON sb.id = l.subject_id
;
'''
cursor.execute(select_query3)
data3 = cursor.fetchall()


base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'data.csv')

with open(eugene_file_path, newline='') as data_file:
    file_data = csv.reader(data_file)
    data = [row for row in file_data]

data_set = set()
for row in data:
    for item in row:
        data_set.add(item)

db_set = set()
for row in data3:
    for item in row:
        db_set.add(item)

for item in data_set:
    if item not in db_set:
        print(item)
