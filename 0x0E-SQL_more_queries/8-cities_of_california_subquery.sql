-- list all cities of CA in the database hbtn_0d_usa
-- results ordered by cities.id
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = "California");