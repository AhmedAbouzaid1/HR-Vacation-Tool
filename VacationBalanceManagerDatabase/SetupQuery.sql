CREATE SCHEMA `vacation` ;
USE `vacation`;  

-- Create Customer table
CREATE TABLE VacationBalance (
  employee_id INT AUTO_INCREMENT PRIMARY KEY,
  annual_balance INT DEFAULT 21,
  sick_balance INT DEFAULT 14
);

INSERT INTO VacationBalance
VALUES(1, 21, 14);