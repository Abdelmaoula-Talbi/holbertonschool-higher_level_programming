--  creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IN hbtn_0d_usa IF NOT EXISTS states (id INT UNIQUE PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256) NOT NULL);
