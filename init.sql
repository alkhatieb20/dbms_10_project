CREATE TABLE courses (
    course_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    course_code VARCHAR(50) UNIQUE NOT NULL,
    course_name VARCHAR(200) NOT NULL
);

CREATE TABLE topics (
    topic_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    course_id INTEGER NOT NULL REFERENCES courses(course_id) ON DELETE CASCADE,
    topic_name VARCHAR(200) NOT NULL
);

CREATE TABLE questions (
    question_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    topic_id INTEGER NOT NULL REFERENCES topics(topic_id) ON DELETE CASCADE,
    question_text TEXT NOT NULL,
    latex_content TEXT,
    default_points INTEGER NOT NULL DEFAULT 0,
    difficulty VARCHAR(50)
);

CREATE TABLE exams (
    exam_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    course_id INTEGER NOT NULL REFERENCES courses(course_id) ON DELETE CASCADE,
    exam_title VARCHAR(200) NOT NULL,
    exam_date DATE NOT NULL,
    total_points INTEGER DEFAULT 0
);

CREATE TABLE exam_questions (
    exam_id INTEGER NOT NULL REFERENCES exams(exam_id) ON DELETE CASCADE,
    question_id INTEGER NOT NULL REFERENCES questions(question_id) ON DELETE CASCADE,
    sequence_order INTEGER NOT NULL,
    assigned_points INTEGER NOT NULL,
    PRIMARY KEY (exam_id, question_id)
);

INSERT INTO courses (course_code, course_name) VALUES 
('CS101', 'Introduction to Computer Science'),
('OS201', 'Operating Systems');

INSERT INTO topics (course_id, topic_name) VALUES 
(1, 'Data Representation'),
(2, 'Virtualization'),
(2, 'Hardware Components');

INSERT INTO questions (topic_id, question_text, latex_content, default_points, difficulty) VALUES 
(1, 'Explain RGB to CMYK', '', 10, 'Medium'),
(2, 'Server Virtualization', '', 15, 'Hard'),
(3, 'Memristors', '', 5, 'Easy');

INSERT INTO exams (course_id, exam_title, exam_date, total_points) VALUES 
(2, 'Exam: SoSe 2026', '2026-08-15', 30);

INSERT INTO exam_questions (exam_id, question_id, sequence_order, assigned_points) VALUES 
(1, 1, 1, 10),
(1, 2, 2, 15),
(1, 3, 3, 5);