-- INSERT INTO students (name, second_name, group_id) VALUES ('Denis', 'Dmitrichev', 1);

-- INSERT INTO books (title, taken_by_student_id) VALUES ('Outcomes Elementary Workbook', 21456),
													  -- ('Outcomes Elementary Students book', 21456),
													  -- ('Essential Grammar', 21456);

-- INSERT INTO `groups` (title, start_date, end_date) VALUES ('Forever alone', 'sep 2025', 'dec 2025');

-- UPDATE students SET group_id = 21421 WHERE name = 'Denis' AND second_name = 'Dmitrichev'

-- INSERT INTO subjects (title) VALUES ('Painting'),
									-- ('Class hour'),
									-- ('Cooking');

-- INSERT INTO lessons (title, subject_id) VALUES ('Draw Picture', 12541),
											   -- ('Draw human', 12541),
											   -- ('Conversation about it', 12542),
											   -- ('Nothing to do', 12542),
											   -- ('Meat', 12543),
											   -- ('Fish', 12543);

-- INSERT INTO marks (value, lesson_id, student_id) VALUES ('5', 13263, 21456),
													 	-- ('4', 13264, 21456),
													 	-- ('5', 13265, 21456),
													 	-- ('3', 13266, 21456),
													 	-- ('5', 13267, 21456),
													 	-- ('3',13268, 21456);
SELECT value
FROM marks 
WHERE student_id = 21456;

SELECT title
FROM books
WHERE taken_by_student_id = 21456;

SELECT g.title, b.title, m.value, l.title, sb.title 
FROM students s
JOIN `groups` g ON g.id = s.group_id
JOIN books b ON b.taken_by_student_id = s.id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON l.id = m.lesson_id 
JOIN subjects sb ON sb.id = l.subject_id
WHERE  s.id = 21456;
