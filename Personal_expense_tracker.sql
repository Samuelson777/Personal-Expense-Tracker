/*Create a Database:*/
CREATE DATABASE expense_tracker;
USE expense_tracker;

/*Create Tables:*/
-- Create Categories Table
CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(255) NOT NULL
);

-- Create Expenses Table
CREATE TABLE Expenses (
    expense_id INT AUTO_INCREMENT PRIMARY KEY,
    amount DECIMAL(10, 2) NOT NULL,
    date DATE NOT NULL,
    category_id INT,
    description TEXT,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

/*Insert Sample Data*/
-- Insert Categories
INSERT INTO Categories (category_name) VALUES ('Food');
INSERT INTO Categories (category_name) VALUES ('Transportation');
INSERT INTO Categories (category_name) VALUES ('Entertainment');
INSERT INTO Categories (category_name) VALUES ('Utilities');
INSERT INTO Categories (category_name) VALUES ('Other');

/* View Categories*/
SELECT * FROM Categories;

-- View Expenses
SELECT * FROM Expenses;

-- View Expenses with Category Names
SELECT e.expense_id, e.amount, e.date, c.category_name, e.description
FROM Expenses e
JOIN Categories c ON e.category_id = c.category_id;

SELECT * FROM Categories;
SELECT * FROM Expenses;