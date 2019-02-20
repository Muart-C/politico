""" manage database set up """
import os
import psycopg2
from psycopg2.extras import DictCursor
from api.utils.validator import return_error

def create_tables():
    users = """
        CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            firstname VARCHAR(128) NULL,
            lastname VARCHAR(128) NULL,
            othername VARCHAR(128) NULL,
            email VARCHAR(128) NOT NULL,
            phone_number VARCHAR(150)  NULL,
            passport_url VARCHAR(256)  NULL,
            password VARCHAR(256) NOT NULL,
            is_admin  boolean NOT NULL DEFAULT TRUE
        );"""

    parties = """
        CREATE TABLE IF NOT EXISTS parties(
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            hq_address VARCHAR(200) NOT NULL,
            logo_url VARCHAR(256) NOT NULL
        );"""

    offices = """
        CREATE TABLE IF NOT EXISTS offices(
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            office_type VARCHAR(100) NOT NULL
        );"""

    candidates = """
        CREATE TABLE IF NOT EXISTS candidates(
            id SERIAL PRIMARY KEY,
            office_id INTEGER,
            party_id INTEGER,
            candidate_id INTEGER,
            PRIMARY KEY(id, office_id),
            FOREIGN KEY(office_id) REFERENCES offices(id) ON DELETE CASCADE,
            FOREIGN KEY(party_id) REFERENCES parties(id) ON DELETE CASCADE,
            FOREIGN KEY(candidate_id) REFERENCES users(id) ON DELETE CASCADE
        );"""

    petitions = """
        CREATE TABLE IF NOT EXISTS petitions(
            id SERIAL PRIMARY KEY,
            created_on TIMESTAMP NOT NULL DEFAULT now(),
            created_by INTEGER,
            office_id INTEGER,
            petition_description TEXT NOT NULL,
            FOREIGN KEY(created_by) REFERENCES users(id) ON DELETE CASCADE,
            FOREIGN KEY(office_id) REFERENCES offices(id) ON DELETE CASCADE
        );"""

    votes = """
        CREATE TABLE IF NOT EXISTS votes(
            id SERIAL NOT NULL,
            created_on TIMESTAMP NOT NULL DEFAULT now(),
            created_by INTEGER,
            office_id INTEGER,
            candidate_id INTEGER,
            PRIMARY KEY(id, created_by),
            FOREIGN KEY(created_by) REFERENCES users(id) ON DELETE CASCADE,
            FOREIGN KEY(office_id) REFERENCES offices(id) ON DELETE CASCADE,
            FOREIGN KEY(candidate_id) REFERENCES candidates(id) ON DELETE CASCADE
        );"""

    return [users, parties, offices, candidates, petitions, votes]

def drop_data_from_tables():
    delete_user_data = '''DELETE FROM users;'''
    delete_parties_data = '''DELETE FROM parties;'''
    delete_offices_data = '''DELETE FROM offices;'''
    delete_candidates_data = '''DELETE FROM candidates;'''
    delete_petitions_data = '''DELETE FROM petitions;'''
    delete_votes_data = '''DELETE FROM votes;'''

    return [delete_user_data, delete_parties_data,delete_offices_data,\
         delete_candidates_data, delete_candidates_data,\
              delete_petitions_data, delete_votes_data]


def drop_tables_if_exists():
    drop_tables = '''DROP TABLE IF EXISTS users,parties,offices,\
        candidates,petitions,votes CASCADE;'''
    return [drop_tables]
