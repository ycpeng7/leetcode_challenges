/*
Case study
https://docs.google.com/document/d/10fYfiTz9y04aY2UufnK90eM6C7QTEHahmv-qCvLTR_Q/edit#



Students at your hometown high school have decided to organize their social network using databases.
So far, they have collected information about sixteen students in four grades, 9-12. Here's the schema: 

Highschooler ( ID, name, grade ) 
English: There is a high school student with unique ID and a given first name in a certain grade. 

Friend ( ID1, ID2 ) 
English: The student with ID1 is friends with the student with ID2. Friendship is mutual,
    so if (123, 456) is in the Friend table, so is (456, 123). 

Likes ( ID1, ID2 ) 
English: The student with ID1 likes the student with ID2. Liking someone is not necessarily mutual,
     so if (123, 456) is in the Likes table, there is no guarantee that (456, 123) is also present.

*/


-- Q1. Find the names of all students who are friends with someone named Gabriel. 

SELECT name
FROM Highschooler
WHERE ID in (
    SELECT DISTINCT Friend.ID2
    FROM Highschooler LEFT JOIN Friend
    ON Highschooler.ID = Friend.ID1
    WHERE Highschooler.name = 'Gabriel');

-- Q2. For every student who likes someone 2 or more grades younger than themselves,
-- return that student's name and grade, and the name and grade of the student they like. 

SELECT h1.name, h1.grade, h2.name, h2.grade
FROM Likes
LEFT JOIN Highschooler h1
ON Likes.ID1 = h1.ID
LEFT JOIN Highschooler h2
ON Likes.ID2 = h2.ID
WHERE h1.grade >= h2.grade + 2;

-- Q3. For every pair of students who both like each other, return the name and grade of both students.
-- Include each pair only once, with the two names in alphabetical order.

SELECT h1.name, h1.grade, h2.name, h2.grade
FROM Likes l1
INNER JOIN Likes l2
ON l1.ID2 = l2.ID1 AND l1.ID1 = L2.ID2
LEFT JOIN Highschooler h1
ON l1.ID1 = h1.ID
LEFT JOIN Highschooler h2
ON l1.ID2 = h2.ID
WHERE h2.name > h1.name;

-- Q7. For each student A who likes a student B where the two are not friends,
-- find if they have a friend C in common (who can introduce them!).
-- For all such trios, return the name and grade of A, B, and C. 

-- T: A who likes B but two are not friends
-- h1: student A, h2: student B, h3: student C
SELECT h1.name, h1.grade, h2.name, h2.grade, h3.name, h3.grade 
FROM (
    SELECT *
    FROM Likes l1
    WHERE l1.ID2 NOT IN(
        SELECT ID2
        FROM Friend
        WHERE ID1 = l1.ID1
    )) T
INNER JOIN friend f1
ON T.ID1 = f1.ID1
INNER JOIN friend f2
ON T.ID2 = f2.ID1
LEFT JOIN Highschooler h1
ON T.ID1 = h1.ID
LEFT JOIN Highschooler h2
ON T.ID2 = h2.ID
LEFT JOIN Highschooler h3
ON f1.ID2 = h3.ID
WHERE f1.ID2 = f2.ID2;

-- Q9. Find the name and grade of all students who are liked by more than one other student.

SELECT name, grade
FROM Highschooler
WHERE ID IN (
    SELECT ID2
    FROM Likes
    GROUP BY ID2
    HAVING COUNT(*) > 1
);

