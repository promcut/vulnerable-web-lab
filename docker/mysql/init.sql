CREATE DATABASE IF NOT EXISTS vulnerable_lab;

USE vulnerable_lab;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    role VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS comments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    text TEXT
);

INSERT INTO users (id, username, password, role) VALUES
(1,'admin','admin123','admin'),
(2,'alice','pass123','user'),
(3,'bob','bobpass','user');