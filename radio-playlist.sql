CREATE TABLE Painting (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL,
    identifier VARCHAR UNIQUE NOT NULL 
);

CREATE TABLE Podcast (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL,
    url VARCHAR UNIQUE NOT NULL
);

CREATE TABLE PlayList (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    podcast INTEGER NOT NULL,
    radio_station INTEGER NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, 
    track INTEGER NOT NULL,
    FOREIGN KEY (podcast) REFERENCES Podcast (id),
    FOREIGN KEY (radio_station) REFERENCES RadioStation (id),
    FOREIGN KEY (track) REFERENCES Track (id)
);



CREATE TABLE RadioStation (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    call_number VARCHAR UNIQUE NOT NULL,
    painting INTEGER NOT NULL,
    slogan VARCHAR,
    FOREIGN KEY (painting) REFERENCES Painting (id)
);

CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL,
    sha1 VARCHAR NOT NULL,
    url VARCHAR NOT NULL
);

INSERT INTO Painting (name, identifier) VALUES ("Fantasy Island", "snowflake-ungodly-likely");
INSERT INTO Painting (name, identifier) VALUES ("Drive in the Dark", "flatly-rule-dreamlike");
INSERT INTO Painting (name, identifier) VALUES ("Nobel Prize 2016", "legend-properly-lagged");
INSERT INTO RadioStation (call_number, painting, slogan) VALUES ("KWRVY", 1, "The first and original pirate station");
INSERT INTO RadioStation (call_number, painting, slogan) VALUES ("WXEE", 2, "For your smooth driving pleasure");
INSERT INTO RadioStation (call_number, painting, slogan) VALUES ("K4TP", 3, "The talk and music pirate station");
