-- Lists all cities in the database hbtn_0d_usa
SELECT c.id, c.name, s.name FROM cities AS c, states AS s WHERE c.state_id = s.id;