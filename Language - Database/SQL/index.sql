-- Create a table books
-- id, title, author, genre (default Non-Fiction)

-- title, author, genre
-- "1984", "Stacee Ianitti", "Self-Help"
-- "Brave New World", "Vinnie McKane",	"Historical Fiction"
-- "To Kill a Mockingbird", "Mohandas Lavis", "Thriller"
-- "Lord of the Flies", "Latashia Itscowics", "Non-Fiction"
-- "The Grapes of Wrath", "Issi Heinz", "Fiction"
-- "Brave New World",	"Damara Oldroyde",	"Fiction"
-- "The Great Gatsby", "Anthiathia Molesworth", "Fantasy"
-- "Moby Dick", "Issi Heinz", "Mystery"
-- "Pride and Prejudice", "Carita Croy", "Thriller"

CREATE TABLE book (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    genre TEXT DEFAULT 'Non-Fiction'
);

INSERT INTO book (title, author, genre) VALUES ('1984', 'Stacee Ianitti', 'Self-Help');
INSERT INTO book (title, author, genre) VALUES ('Brave New World', 'Vinnie McKane', 'Historical Fiction');
INSERT INTO book (title, author, genre) VALUES ('To Kill a Mockingbird', 'Mohandas Lavis', 'Thriller');
INSERT INTO book (title, author, genre) VALUES ('Lord of the Flies', 'Latashia Itscowics', 'Non-Fiction');
INSERT INTO book (title, author, genre) VALUES ('The Grapes of Wrath', 'Issi Heinz', 'Fiction');
INSERT INTO book (title, author, genre) VALUES ('Brave New World', 'Damara Oldroyde', 'Fiction');
INSERT INTO book (title, author, genre) VALUES ('The Great Gatsby', 'Anthiathia Molesworth', 'Fantasy');
INSERT INTO book (title, author, genre) VALUES ('Moby Dick', 'Issi Heinz', 'Mystery');
INSERT INTO book (title, author, genre) VALUES ('Pride and Prejudice', 'Carita Croy', 'Thriller');

