import psycopg2
import os

try:
    




"""create data tables for the api."""
try:
    # drop existing tables if there are any
    drop_tables = "DROP TYPE IF EXISTS office_type; \
        DROP TABLE IF EXISTS users, parties, candidates, petitions, offices,votes"

            self.cursor.execute(drop_tables)

            office_type_enum = "CREATE TYPE office_type as ENUM(\
                'federal','legislative','local','state')"

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
                    name VARCHAR(100) NOT NULL
                );
            """
            # create candidates sql query definition
            candidates = """
                CREATE TABLE candidates(
                    id SERIAL PRIMARY KEY,
                    office_id INTEGER,
                    party_id INTEGER,
                    candidate_id INTEGER,
                    FOREIGN KEY(office_id) REFERENCES offices(id),
                    FOREIGN KEY(party_id) REFERENCES parties(id),
                    FOREIGN KEY(candidate_id) REFERENCES users(id)
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
                    FOREIGN KEY(created_by) REFERENCES users(id),
                    FOREIGN KEY(office_id) REFERENCES offices(id)
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
                    FOREIGN KEY(created_by) REFERENCES users(id),
                    FOREIGN KEY(office_id) REFERENCES offices(id),
                    FOREIGN KEY(candidate_id) REFERENCES users(id)
                );
            """

            # execute the queries to create the respective tables
            self.cursor.execute(users)
            self.cursor.execute(parties)
            self.cursor.execute(offices)
            self.cursor.execute(candidates)
            self.cursor.execute(petitions)
            self.cursor.execute(votes)
            self.cursor.execute(office_type_enum)

            # #persist the changes to the database
            self.connection.commit()

        except (Exception, psycopg2.Error) as create_error:
            print("an error occurred while creating the tables", create_error.args[0])