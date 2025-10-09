import mysql.connector as mysql

db = mysql.connect(
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    database='st-onl',
)

cursor = db.cursor(dictionary=True)

query = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
values = ('Kirill', 'Andropov')
cursor.execute(query, values)
student_id = cursor.lastrowid

query_2 = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
values2 = [('Outcomes Elementary Workbook2', student_id),
           ('Outcomes Elementary Students book2', student_id),
           ('Essential Grammar2', student_id)]
cursor.executemany(query_2, values2)

query3 = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
values3 = ('Forever alone2', 'sep 2025', 'dec 2025')
cursor.execute(query3, values3)
group_id = cursor.lastrowid

query4 = "UPDATE students SET group_id = %s WHERE id = %s"
values4 = (group_id, student_id)
cursor.execute(query4, values4)

query5_1 = "INSERT INTO subjects (title) VALUES (%s)"
values5_1 = ('Painting2',)
cursor.execute(query5_1, values5_1)
painting_id = cursor.lastrowid

query5_2 = "INSERT INTO subjects (title) VALUES (%s)"
values5_2 = ('Class hour2',)
cursor.execute(query5_2, values5_2)
class_hour_id = cursor.lastrowid

query5_3 = "INSERT INTO subjects (title) VALUES (%s)"
values5_3 = ('Cooking2',)
cursor.execute(query5_3, values5_3)
cooking_id = cursor.lastrowid

query6_1 = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
values6_1 = ('Draw Picture2', painting_id)
cursor.execute(query6_1, values6_1)
draw_picture_id = cursor.lastrowid

query6_2 = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
values6_2 = ('Draw human2', painting_id)
cursor.execute(query6_2, values6_2)
draw_human_id = cursor.lastrowid

query6_3 = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
values6_3 = ('Conversation about it2', class_hour_id)
cursor.execute(query6_3, values6_3)
conversation_id = cursor.lastrowid

query6_4 = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
values6_4 = ('Nothing to do2', class_hour_id)
cursor.execute(query6_4, values6_4)
nothing_id = cursor.lastrowid

query6_5 = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
values6_5 = ('Meat2', cooking_id)
cursor.execute(query6_5, values6_5)
meat_id = cursor.lastrowid

query6_6 = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
values6_6 = ('Fish2', cooking_id)
cursor.execute(query6_6, values6_6)
fish_id = cursor.lastrowid

query7 = "INSERT INTO marks (value, lesson_id, student_id) VALUES  (%s, %s, %s)"
values7 = [(5, draw_picture_id, student_id), (4, draw_human_id, student_id),
           (5, conversation_id, student_id), (3, nothing_id, student_id),
           (5, meat_id, student_id), (3, fish_id, student_id)]
cursor.executemany(query7, values7)

db.commit()

select_query1 = '''
SELECT value as mark_value
FROM marks
WHERE student_id = %s;
'''
cursor.execute(select_query1, (student_id,))
data1 = cursor.fetchall()
print(data1)

select_query2 = '''
SELECT title as book_title
FROM books
WHERE taken_by_student_id = %s;
'''
cursor.execute(select_query2, (student_id,))
data2 = cursor.fetchall()
print(data2)

select_query3 = '''
SELECT
    g.title as group_title,
    b.title as book_title,
    m.value as mark_value,
    l.title as lesson_title,
    sb.title as subject_title
FROM students s
JOIN `groups` g ON g.id = s.group_id
JOIN books b ON b.taken_by_student_id = s.id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON l.id = m.lesson_id
JOIN subjects sb ON sb.id = l.subject_id
WHERE s.id = %s;
'''
cursor.execute(select_query3, (student_id,))
data3 = cursor.fetchall()
print(data3)

db.close()
