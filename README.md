ThePyMonitor
============

Python based monitoring system, with pluggable a. client communication protocol b. Server configuration format c. Probed data store/graph

https://docs.google.com/drawings/d/1ygof8i1qVcabZBiHoPN7tNNkSpbVaVYN6zy6mGHXlnU/edit


Overall flow:

1. Configurations are present in (sqlite | xml | mysql | ...) .
2. Reading configs Server knows WHOM to monitor WHAT and WHEN.
3. Server makes an (xmlrpc|http|tcp|nrpe|zmq|.....) connection with a validating string to client and then the connection is closed.
4. Client runs the probe/monitor and gets the output.
5. Client makes a new (http|tcp|nrpe|.....) connection to server responding with validating_string + output + timestamp back to server.
6. Server saves the historical data in (sqlite | mysql | rrd | graphite | ...)

 
