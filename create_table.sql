DROP TYPE IF EXISTS office_type;
DROP TABLE IF EXISTS users, parties, candidates, petitions, offices,votes;
CREATE TYPE office_type AS ENUM('federal','legislative','local','state');
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
CREATE TABLE parties(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    hq_address VARCHAR(200) NOT NULL,
    logo_url VARCHAR(256) NOT NULL
);

CREATE TABLE offices(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE candidates(
    id SERIAL PRIMARY KEY,
    office_id INTEGER,
    party_id INTEGER,
    candidate_id INTEGER,
    FOREIGN KEY(office_id) REFERENCES offices(id),
    FOREIGN KEY(party_id) REFERENCES parties(id),
    FOREIGN KEY(candidate_id) REFERENCES users(id)
);

CREATE TABLE petitions(
    id SERIAL PRIMARY KEY,
    created_on TIMESTAMP NOT NULL DEFAULT now(),
    created_by INTEGER,
    office_id INTEGER,
    petition_description TEXT NOT NULL,
    FOREIGN KEY(created_by) REFERENCES users(id),
    FOREIGN KEY(office_id) REFERENCES offices(id)
);

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
