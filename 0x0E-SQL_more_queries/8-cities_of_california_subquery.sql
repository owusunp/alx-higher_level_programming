-- The states table contains only one record where name = California 
SELECT id, name  FROM cities WHERE state_id = 
(SELECT id FROM states WHERE name = 'California')
ORDER  BY id ASC;
