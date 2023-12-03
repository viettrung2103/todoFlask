CREATE TABLE tasks (
task_id INTEGER,
name TEXT NOT NULL,
description TEXT NOT NULL,
is_done BOOLEAN DEFAULT False,
PRIMARY KEY(task_id)
);