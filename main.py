
# Task 1 

CREATE TABLE Author (
    AuthorID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
);


# Task 2 

CREATE TABLE Books (
    BookID INT PRIMARY KEY,
    Title VARCHAR(100),
    AuthorID INT,
    FOREIGN KEY (AuthorID) REFERENCES Author(AuthorID)
);


# Task 3 

INSERT INTO Author (AuthorID, FirstName, LastName, BirthDate)
VALUES 
    (1, 'Tom', 'Jons', '1988'),
    (2, 'Giorgi', 'Janelidze', '1977'),
    (3, 'Kaxa', 'Kakabadze', '1990'),
    (4, 'Ana', 'Baramidze', '1987'),
    (5, 'David', 'Koperfilm', '1972');

INSERT INTO Books (BookID, Title, AuthorID)
VALUES
    (1, 'Book 1', 1),
    (2, 'Book 2', 2),
    (3, 'Book 3', 3),
    (4, 'Book 4', 4),
    (5, 'Book 5', 5);
    
    
# Task 4

UPDATE Books
SET Title = 'New Book'
WHERE BookID = 3;


# Task 5


DELETE FROM Author;


DELETE FROM Books;



# Task 6 


DROP TABLE Author;

DROP TABLE Books;
