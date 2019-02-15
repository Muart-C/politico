import os
import psycopg2

try:
    dbname=os.getenv("DATABASE_POLITICO_TEST")
    user=os.getenv("DATABASE_USERNAME")
    password=os.getenv("DATABASE_PASSWORD")
    host=os.getenv("DATABASE_HOST")
    port=os.getenv("DATABASE_PORT")
    connection = psycopg2.connect(dbname=dbname,\
               user=user,host=host,\
                     password=password, port=port)
    cursor = connection.cursor()
except psycopg2.DatabaseError as error:
    print("error connecting to the database")

def create_tables():
    """create data tables for the api."""
    try:
        # drop existing tables if there are any
        drop_tables = "DROP TYPE IF EXISTS office_type; \
                DROP TABLE IF EXISTS users, parties, candidates, petitions, offices,votes"
        # drop all tables
        cursor.execute(drop_tables)

        # create users query definition
        users = """
                CREATE TABLE users(
                    id SERIAL PRIMARY KEY,
                    firstname VARCHAR(128) NULL,
                    lastname VARCHAR(128) NULL,
                    othername VARCHAR(128) NULL,
                    email VARCHAR(128) NOT NULL,
                    phone_number VARCHAR(150)  NULL,
                    passport_url VARCHAR(256)  NULL,
                    password VARCHAR(256) NOT NULL,
                    is_admin  boolean NOT NULL DEFAULT TRUE
                );
            """
        #create parties sql query definition
        parties = """
                CREATE TABLE parties(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    hq_address VARCHAR(200) NOT NULL,
                    logo_url VARCHAR(256) NOT NULL
                );
            """
        #create offices sql query definition
        offices = """
                CREATE TABLE offices(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    office_type VARCHAR(100) NOT NULL
                );
            """
        # create candidates sql query definition
        candidates = """
            CREATE TABLE candidates(
                    id SERIAL PRIMARY KEY,
                    office_id INTEGER,
                    party_id INTEGER,
                    candidate_id INTEGER,
                    FOREIGN KEY(office_id) REFERENCES offices(id) ON DELETE CASCADE,
                    FOREIGN KEY(party_id) REFERENCES parties(id) ON DELETE CASCADE,
                    FOREIGN KEY(candidate_id) REFERENCES users(id) ON DELETE CASCADE
                );
            """
        # create petitions sql query definition
        petitions = """
                CREATE TABLE petitions(
                    id SERIAL PRIMARY KEY,
                    created_on TIMESTAMP NOT NULL DEFAULT now(),
                    created_by INTEGER,
                    office_id INTEGER,
                    petition_description TEXT NOT NULL,
                    FOREIGN KEY(created_by) REFERENCES users(id) ON DELETE CASCADE,
                    FOREIGN KEY(office_id) REFERENCES offices(id) ON DELETE CASCADE
                );
            """

        # create votes sql query definition
        votes = """
                CREATE TABLE votes(
                    id SERIAL PRIMARY KEY,
                    created_on TIMESTAMP NOT NULL DEFAULT now(),
                    created_by INTEGER,
                    office_id INTEGER,
                    candidate_id INTEGER,
                    FOREIGN KEY(created_by) REFERENCES users(id) ON DELETE CASCADE,
                    FOREIGN KEY(office_id) REFERENCES offices(id) ON DELETE CASCADE,
                    FOREIGN KEY(candidate_id) REFERENCES users(id) ON DELETE CASCADE
                );
            """

        # execute the queries to create the respective tables
        cursor.execute(users)
        cursor.execute(parties)
        cursor.execute(offices)
        cursor.execute(candidates)
        cursor.execute(petitions)
        cursor.execute(votes)

        # #persist the changes to the database
        connection.commit()

    except (Exception, psycopg2.Error) as create_error:
        print("an error occurred while creating the tables", create_error.args[0])


#to be used during testing database operations
def drop_data_from_tables():
    cursor.execute("DELETE FROM users;")
    cursor.execute("DELETE FROM parties;")
    cursor.execute("DELETE FROM candidates;")
    cursor.execute("DELETE FROM petitions;")
    cursor.execute("DELETE FROM votes;")

    #persist the changes to the database
    connection.commit()


if __name__ == "__main__":
    create_tables()