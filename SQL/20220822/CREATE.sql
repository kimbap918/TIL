CREATE TABLE users (
  id INT PRIMARY KEY,
  name TEXT,
  role_id INT
);

INSERT INTO users VALUES
(1, '관리자', 1),
(2, '김철수', 2),
(3, '이영희'),

CREATE TABLE role (
  id INT PRIMARY KEY,
  title TEXT
);

INSERT INTO role VALUES
(1, 'admin',),
(2, 'staff',),
(3, 'student');

CREATE TABLE articles (
  id INT PRIMARY KEY,
  title TEXT,
  content TEXT,
  user_id INT
)

INSERT INTO 

