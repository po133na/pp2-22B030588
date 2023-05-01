import psycopg2

conn = psycopg2.connect(
    database="PhoneBook",
    user="postgres",
    password="12345",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Function that returns all records based on a pattern (example of pattern: part of name, surname, phone number)
pattern = """
CREATE OR REPLACE FUNCTION get_data(pattern VARCHAR)
RETURNS SETOF PhoneBook AS $$
BEGIN
    RETURN QUERY SELECT * FROM PhoneBook WHERE name LIKE '%' || pattern || '%' OR last_name LIKE '%' || pattern || '%' OR phone LIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;
"""

# Create procedure to insert new user by name and phone, update phone if user already exists
procedure = """
CREATE OR REPLACE PROCEDURE insert_user(IN name VARCHAR, IN surname VARCHAR, IN phone VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS(SELECT 1 FROM PhoneBook WHERE name = insert_user.name AND surname = insert_user.surname) THEN
        UPDATE PhoneBook SET phone = insert_user.phone WHERE name = insert_user.name AND surname = insert_user.surname;
    ELSE
        INSERT INTO PhoneBook (name, surname, phone) VALUES (insert_user.name, insert_user.surname, insert_user.phone);
    END IF;
END;
$$;
"""

# Create procedure to insert many new users by list of name and phone. 
# Use loop and if statement in stored procedure. Check correctness of phone in procedure and return all incorrect data.
inserting_names = """
CREATE OR REPLACE PROCEDURE insert_users(
    IN user_list text[][]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INTEGER := 1;
    current_user text[];
BEGIN
    WHILE i <= array_length(user_list, 1) LOOP
        current_user := user_list[i];
        
        IF regexp_matches(current_user.phone, '[0-9]+') THEN
            IF EXISTS(SELECT 1 FROM PhoneBook WHERE name = current_user.name AND surname = current_user.surname) THEN
                UPDATE PhoneBook SET phone = current_user.phone WHERE name = current_user.name AND surname = current_user.surname;
            ELSE
                INSERT INTO PhoneBook (name, surname, phone) VALUES (current_user.name, current_user.surname, current_user.phone);
            END IF;
        END IF;
        
        i := i + 1;
    END LOOP;
END;
$$;
"""

#Create function to querying data from the tables with pagination (by limit and offset)
queue = """
CREATE OR REPLACE FUNCTION get_data1(
    table_name text, 
    limit integer, 
    offset integer
) RETURNS SETOF anyelement AS $$
BEGIN
    RETURN QUERY EXECUTE format('SELECT * FROM %I LIMIT %s OFFSET %s', table_name, limit, offset);
END;
$$ LANGUAGE plpgsql;
"""

#Implement procedure to deleting data from tables by username or phone
delete = """
CREATE OR REPLACE PROCEDURE delete_data(IN data VARCHAR(30))
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM contacts WHERE name = data OR surname = data OR phone = data;
END;
$$;
"""
try:
    cur.execute( delete )
    cur.execute('CALL delete_data(%s)', ('Doe',))

except psycopg2.DatabaseError as e:
    print(f"Error: {e}")
    conn.rollback()
finally:
    conn.commit()
    cur.close()
    conn.close()