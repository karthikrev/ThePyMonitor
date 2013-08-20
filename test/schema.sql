DROP TABLE IF EXISTS probe;

CREATE TABLE probe (
    id INTEGER PRIMARY KEY,
    name TEXT,
    parameter TEXT,
    isremote INTEGER,
    interval INTEGER, 
    warning FLOAT,
    error FLOAT
);

INSERT INTO probe VALUES ( 1, 'Idle_CPU', 'idle', 1, 1, NULL, NULL);
INSERT INTO probe VALUES ( 2, 'Used_CPU', 'used', 1, 3, NULL, NULL);
INSERT INTO probe VALUES ( 3, 'User_CPU', 'user', 1, 5, NULL, NULL);
INSERT INTO probe VALUES ( 4, 'System_CPU', 'system', 1, 1, NULL, NULL);
INSERT INTO probe VALUES ( 5, 'IO_Wait_CPU', 'iowait', 1, 2, NULL, NULL);
INSERT INTO probe VALUES ( 6, 'Free_memory', 'free_pct', 1, 7, NULL, NULL);
INSERT INTO probe VALUES ( 7, 'Free_memory', 'free', 1, 2, NULL, NULL);
INSERT INTO probe VALUES ( 8, 'Used_memory', 'used_pct', 1, 1, NULL, NULL);
INSERT INTO probe VALUES ( 9, 'Used_memory', 'used', 1, 1, NULL, NULL);
INSERT INTO probe VALUES (10, 'Used_swap', 'swap_used_pct', 1, 1, NULL, NULL);
INSERT INTO probe VALUES (11, '1 min load average', 'load1', 1, 1, NULL, NULL);
INSERT INTO probe VALUES (12, '5 min load average', 'load5', 1, 5, NULL, NULL);
INSERT INTO probe VALUES (13, '15 min load average', 'load15', 1, 15, NULL, NULL);
INSERT INTO probe VALUES (14, 'Running processes', 'running', 1, 2, NULL, NULL);
INSERT INTO probe VALUES (15, 'Total processes', 'total', 1, 5, NULL, NULL);

DROP TABLE IF EXISTS host;

CREATE TABLE host (
    id INTEGER PRIMARY KEY,
    name TEXT,
    address TEXT,
    port TEXT
);

INSERT INTO host VALUES (1, 'My laptop', 'localhost', '8080');
INSERT INTO host VALUES (2, 'My VM', 'karthik-vm1', '8081');

DROP TABLE IF EXISTS hostprobe;

CREATE TABLE hostprobe (
    id INTEGER PRIMARY KEY,
    probe_id INTEGER,
    host_id INTEGER,
    warning FLOAT,
    error FLOAT,
    FOREIGN KEY (probe_id) REFERENCES probe(id),
    FOREIGN KEY (host_id) REFERENCES host(id)
);

INSERT INTO hostprobe VALUES ( 1, 1, 1, NULL, NULL);
INSERT INTO hostprobe VALUES ( 2, 2, 1, NULL, NULL);
INSERT INTO hostprobe VALUES ( 3, 3, 1, NULL, NULL);
INSERT INTO hostprobe VALUES ( 4, 4, 2, NULL, NULL);
INSERT INTO hostprobe VALUES ( 5, 5, 1, NULL, NULL);
INSERT INTO hostprobe VALUES ( 6, 6, 1, NULL, NULL);
INSERT INTO hostprobe VALUES ( 7, 7, 1, NULL, NULL);
INSERT INTO hostprobe VALUES ( 8, 8, 1, NULL, NULL);
INSERT INTO hostprobe VALUES ( 9, 9, 2, NULL, NULL);
INSERT INTO hostprobe VALUES (10, 10, 1, NULL, NULL);
INSERT INTO hostprobe VALUES (11, 11, 1, NULL, NULL);
INSERT INTO hostprobe VALUES (12, 12, 1, NULL, NULL);
INSERT INTO hostprobe VALUES (13, 13, 2, NULL, NULL);
INSERT INTO hostprobe VALUES (14, 14, 1, NULL, NULL);
INSERT INTO hostprobe VALUES (15, 15, 2, NULL, NULL);

/******** USED AS QUEUE LIVE */

DROP TABLE IF EXISTS livequeue;

CREATE TABLE livequeue (
    id INTEGER PRIMARY KEY,
    hostprobe_id INTEGER,
    timestamp TEXT,
    dispatched INTEGER,
    FOREIGN KEY (hostprobe_id) REFERENCES hostprobe(id)
);

/********* PERF DATA  */

DROP TABLE IF EXISTS probereading;

CREATE TABLE perfdata (
    id INTEGER PRIMARY KEY,
    hostprobe_id INTEGER,
    timestamp TEXT,
    probe_value FLOAT,
    ret_code INTEGER,
    FOREIGN KEY (hostprobe_id) REFERENCES hostprobe(id)
);




