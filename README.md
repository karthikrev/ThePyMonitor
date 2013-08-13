ThePyMonitor
============

Overall flow:

1. Configurations are present in sqlite.
2. Server identifies clients WHO should run WHAT probe NOW.
3. Server makes a (http|tcp|nrpe|.....) connection with a validating string to client. The connection is closed.
4. Client runs the probe/monitor and gets the output.
5. Client makes a new (http|tcp|nrpe|.....) connection to server responding with validating_string + output + timestamp back to server.
6. Server saves the historical data in sqlite.
