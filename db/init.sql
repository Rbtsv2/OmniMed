CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE
);

CREATE TABLE analyses (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    data TEXT,
    result TEXT
);