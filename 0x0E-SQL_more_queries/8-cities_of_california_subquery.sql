--  a script that lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT name, id from cities
WHERE state_id = (SELECT id FROM states WHERE name = 'california') ORDER BY id ASC;

