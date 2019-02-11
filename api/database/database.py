# #!api/database/database.py

# import psycopg2


# try:
#     connection = psycopg2.connect(
#         user="admin",
#         password="admin",
#         host="127.0.0.1",
#         port="5432",
#         database="test_politico",
#     )
# except (Exception, psycopg2.Error) as db_error:
#     print("An error occurred while trying to connect to the database", db_error)


# def create_tables(connection):
#     """create data tables for the api."""
#     cursor = connection.cursor()

#     try:
#         # drop existing tables if there are any
#         cursor.execute("DROP TABLE IF EXISTS users, parties, candidates, petitions, offices,votes")

#         # create users query definition
#         users = """
#             CREATE TABLE users(
#                 id INTEGER PRIMARY KEY,
#                 firstname VARCHAR(128) NOT NULL,
#                 lastname VARCHAR(128) NOT NULL,
#                 email VARCHAR(128) NOT NULL,
#                 phone_number VARCHAR(150) NOT NULL,
#                 passport_url VARCHAR(256) NOT NULL,
#                 is_admin  boolean NOT NULL DEFAULT FALSE
#             );
#         """
#         #create parties sql query definition
#         parties = """
#             CREATE TABLE parties(
#                 id INTEGER PRIMARY KEY,
#                 name VARCHAR(100) NOT NULL,
#                 hq_address VARCHAR(200) NOT NULL,
#                 logo_url VARCHAR(256) NOT NULL
#             );
#         """
#         #create offices sql query definition
#         offices = """
#             CREATE TABLE offices(
#                 id INTEGER PRIMARY KEY,
#                 name VARCHAR(100) NOT NULL,
#                 office_type VARCHAR(200) NOT NULL
#             );
#         """
#         # create candidates sql query definition
#         candidates = """
#             CREATE TABLE candidates(
#                 id INTEGER PRIMARY KEY,
#                 office_id INTEGER,
#                 party_id INTEGER,
#                 candidate_id INTEGER,
#                 FOREIGN KEY(office_id) REFERENCES offices(id),
#                 FOREIGN KEY(party_id) REFERENCES parties(id),
#                 FOREIGN KEY(candidate_id) REFERENCES users(id)
#             );
#         """
#         # create petitions sql query definition
#         petitions = """
#             CREATE TABLE petitions(
#                 id INTEGER PRIMARY KEY,
#                 created_on TIMESTAMP NOT NULL DEFAULT now(),
#                 created_by INTEGER,
#                 office_id INTEGER,
#                 petition_description TEXT NOT NULL,
#                 FOREIGN KEY(created_by) REFERENCES users(id),
#                 FOREIGN KEY(office_id) REFERENCES offices(id)
#             );
#         """

#         # create votes sql query definition
#         votes = """
#             CREATE TABLE votes(
#                 id INTEGER PRIMARY KEY,
#                 created_on TIMESTAMP NOT NULL DEFAULT now(),
#                 created_by INTEGER,
#                 office_id INTEGER,
#                 candidate_id INTEGER,
#                 FOREIGN KEY(created_by) REFERENCES users(id),
#                 FOREIGN KEY(office_id) REFERENCES offices(id),
#                 FOREIGN KEY(candidate_id) REFERENCES users(id)
#             );
#         """

#         # execute the queries to create the respective tables
#         cursor.execute(users)
#         cursor.execute(parties)
#         cursor.execute(offices)
#         cursor.execute(candidates)
#         cursor.execute(petitions)
#         cursor.execute(votes)

#         #persist the changes to the database
#         connection.commit()

#     except (Exception, psycopg2.Error) as create_error:
#         print("an error occurred while creating the tables", create_error)


# # to be used during testing database operations
# def drop_data_from_tables():
#     cursor = connection.cursor()
#     cursor.execute("DELETE FROM users;")
#     cursor.execute("DELETE FROM parties;")
#     cursor.execute("DELETE FROM candidates;")
#     cursor.execute("DELETE FROM petitions;")
#     cursor.execute("DELETE FROM votes;")

#     #persist the changes to the database
#     connection.commit()

