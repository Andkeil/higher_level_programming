-- Script list CA cities in database
SELECT id, name FROM cities WHERE state_id=(
       SELECT id FROM states WHERE id=1);
