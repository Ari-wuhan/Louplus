/*数据库模式*/
DROP TABLE IF EXISTS entries;

CREATE TABLE entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title STRING NOT NULL,
    text STRING NOT NULL
);