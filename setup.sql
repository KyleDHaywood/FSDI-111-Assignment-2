CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    hobbies TEXT,
    active BOOLEAN NOT NULL DEFAULT 1
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Kyle",
    "Haywood",
    "Board games"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Brett",
    "Bryant",
    "Darts"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Ray",
    "Garcia",
    "Poker"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Jasmine",
    "Green-key",
    "Getting lost"
);