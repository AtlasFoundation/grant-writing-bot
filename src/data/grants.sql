CREATE DATABASE grant_db;
USE grant_db;

CREATE TABLE grants (
    grant_id INT(11) NOT NULL AUTO_INCREMENT,
    grant_name VARCHAR(255) NOT NULL,
    sponsor_name VARCHAR(255) NOT NULL,
    deadline DATE NOT NULL,
    award_amount FLOAT NOT NULL,
    website_link VARCHAR(255) NOT NULL,
    PRIMARY KEY (grant_id)
);

CREATE TABLE users (
    user_id INT(11) NOT NULL AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(255) NOT NULL,
    PRIMARY KEY (user_id)
);
