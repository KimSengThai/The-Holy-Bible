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


CREATE TABLE reviewer (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    book_id INTEGER,
    FOREIGN KEY (book_id) REFERENCES book(id)
);


INSERT INTO review (name, email) VALUES ()


INSERT INTO book (title, author, genre) VALUES ('1984', 'Stacee Ianitti', 'Self-Help');
INSERT INTO book (title, author, genre) VALUES ('Brave New World', 'Vinnie McKane', 'Historical Fiction');
INSERT INTO book (title, author, genre) VALUES ('To Kill a Mockingbird', 'Mohandas Lavis', 'Thriller');
INSERT INTO book (title, author, genre) VALUES ('Lord of the Flies', 'Latashia Itscowics', 'Non-Fiction');
INSERT INTO book (title, author, genre) VALUES ('The Grapes of Wrath', 'Issi Heinz', 'Fiction');
INSERT INTO book (title, author, genre) VALUES ('Brave New World', 'Damara Oldroyde', 'Fiction');
INSERT INTO book (title, author, genre) VALUES ('The Great Gatsby', 'Anthiathia Molesworth', 'Fantasy');
INSERT INTO book (title, author, genre) VALUES ('Moby Dick', 'Issi Heinz', 'Mystery');
INSERT INTO book (title, author, genre) VALUES ('Pride and Prejudice', 'Carita Croy', 'Thriller');


-- Insert random data into the reviewer table
INSERT INTO reviewer (name, email, book_id) VALUES
  ('John Doe', 'john.doe@example.com', 1),
  ('Jane Smith', 'jane.smith@example.com', 2),
  ('Alice Johnson', 'alice.johnson@example.com', 3),
  ('Bob Brown', 'bob.brown@example.com', 4),
  ('Emily Davis', 'emily.davis@example.com', 5),
  ('Michael Wilson', 'michael.wilson@example.com', 6),
  ('Sarah Taylor', 'sarah.taylor@example.com', 7),
  ('David Martinez', 'david.martinez@example.com', 8),
  ('Jennifer Anderson', 'jennifer.anderson@example.com', 9),
  ('Christopher Thomas', 'christopher.thomas@example.com', 10);

-- Relational Databases
    -- Primary Key and Foreign Keys
-- JOIN Clause
-- Table Relationships
    -- one to many
    -- one to many


CREATE TABLE pets(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    pet_owner_id INTEGER NOT NULL,
    FOREIGN KEY (pet_owner_id) REFERENCES pet_owners(id)
);

CREATE TABLE pet_owners(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    gender TEXT NOT NULL,
    age INTEGER NOT NULL
);

INSERT INTO pet_owners (name, gender, age)
VALUES 
    ('John', 'Male', 25),
    ('Emma', 'Female', 30),
    ('Michael', 'Male', 40),
    ('Sophia', 'Female', 35),
    ('William', 'Male', 28),
    ('Olivia', 'Female', 45),
    ('James', 'Male', 22),
    ('Amelia', 'Female', 50),
    ('Benjamin', 'Male', 60),
    ('Charlotte', 'Female', 55);

SELECT p.name, p.type, o.name, o.age FROM pets p JOIN pet_owners o ON p.pet_owner_id = o.id;

-- music.sql notes
CREATE TABLE songs (_id INTEGER PRIMARY KEY, track INTEGER, title TEXT NOT NULL, album INTEGER);     
CREATE TABLE albums (_id INTEGER PRIMARY KEY, name TEXT NOT NULL, artist INTEGER);
CREATE TABLE artists (_id INTEGER PRIMARY KEY, name TEXT NOT NULL);

-- 1. Select the tile of all songs in the album "Forbidden"
SELECT title FROM songs JOIN albums ON songs.album = albums._id WHERE albums.name = "Forbidden";

-- 2. Repeat the previous query but this time display the songs in track number in the output to verify that it worked ok.
SELECT track, title FROM songs JOIN albums ON songs.album = albums._id WHERE albums.name = "Forbidden" ORDER BY track;

-- 3. Display all songs for the band "Deep Purple"
SELECT title, artists.name FROM songs JOIN albums ON songs.album = albums._id JOIN artists ON artists._id = albums.artist WHERE artists.name = "Deep Purple";

-- 4. Rename the band to "Mehitabel" from "Mehitabel_MODIFIED". Note that this is an exception to the advice to always full quality your column names. SET artists.name wont work, you just need to specify name.
-- 5. Check the answer
UPDATE artists SET name="Mehitabel" WHERE name="Mehitabel_MODIFIED";
SELECT * FROM artists WHERE name = "Mehitabel";

-- 6. Select the tiltes of all the songs by Aerosmith in alphabetical order. Include only the title in the output.
SELECT title FROM songs JOIN albums ON songs.album = albums._id JOIN artists ON artists._id = albums.artist WHERE artists.name = "Aerosmith" ORDER BY title;

-- 7. Replace the column that you used in the previous answer with count(title) to get just a count of the number of songs.
SELECT COUNT(title) FROM songs JOIN albums ON songs.album = albums._id JOIN artists ON artists._id = albums.artist WHERE artists.name = "Aerosmith" ORDER BY title;

-- 8. Get the same list as from step 7 but without any duplicates
SELECT COUNT(DISTINCT title) FROM songs JOIN albums ON songs.album = albums._id JOIN artists ON artists._id = albums.artist WHERE artists.name = "Aerosmith" ORDER BY title;

-- 9. Get the count of the songs without duplicates. Hint: It uses the same keyword as step 8 but the syntax may not be obvious.
SELECT COUNT(DISTINCT title) FROM songs;

-- Reference from above*
CREATE TABLE songs (_id INTEGER PRIMARY KEY, track INTEGER, title TEXT NOT NULL, album INTEGER);     
CREATE TABLE albums (_id INTEGER PRIMARY KEY, name TEXT NOT NULL, artist INTEGER);
CREATE TABLE artists (_id INTEGER PRIMARY KEY, name TEXT NOT NULL);


-- 10 Display all the artists and how many songs they have.
SELECT ar.name, COUNT(s.title) AS song_count 
FROM songs s 
JOIN albums a ON s.album = a._id 
JOIN artists ar ON a.artist = ar._id 
GROUP BY ar.name; 