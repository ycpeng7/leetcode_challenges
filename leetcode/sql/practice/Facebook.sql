/*
Design the normalized tables needed to support Facebook circa 2008.  Some example queries that are needed are:

For a given user, show all of their friends, ordered by how many friends they have in common.
Show all the posts that a user has “liked”
For a given post, show all the comments on that post, ordered chronologically.
Show the feed for a given user, which should show all their friend’s posts, ordered chronologically.
*/

/*
DATA MODELING

USERS:
user_id INT PK
first_name VARCHAR
last_name VARCHAR

FRIENDS:
user_id1 INT PK FK
user_id2 INT PK FK

POSTS:
post_id INT PK
user_id INT FK
post_datetime DATETIME
post_content VARCHAR

LIKES:
user_id INT PK FK
post_id INT PK FK
like_datetime DATETIME

COMMENTS:
comment_id INT PK
user_id INT FK
post_id INT FK

*/

-- For a given user, show all of their friends, ordered by how many friends they have in common.
CREATE PROCEDURE showFriends(IN user_id INT)
BEGIN
    SELECT f1.user_id2 as friendofUser
    FROM friends f1
    LEFT JOIN friends f2
    ON f1.user_id2 = f2.user_id1
    AND f2.user_id2 <> user_id
    GROUP BY f1.user_id2
    WHERE f2.user_id2 IN f1.user_id2
    ORDER BY COUNT(*) DESC;
END;
