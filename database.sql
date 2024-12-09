CREATE DATABASE test_db2 CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

CREATE TABLE learn_en (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    content_en TEXT COLLATE utf8mb4_general_ci,
    content_vi TEXT COLLATE utf8mb4_general_ci,
    comment TEXT COLLATE utf8mb4_general_ci
);

INSERT INTO learn_en (content_en, content_vi, comment) VALUES
('Good morning, how are you today?', 'Chào buổi sáng, bạn có khỏe không?', 'chào hỏi');

SELECT User, Host FROM mysql.user;

CREATE USER 'tuantd'@'%' IDENTIFIED BY 'admin123';

-- full quyền với DB = test_db2
GRANT ALL PRIVILEGES ON test_db2.* TO 'tuantd'@'%';

FLUSH PRIVILEGES;