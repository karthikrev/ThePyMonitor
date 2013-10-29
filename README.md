ThePyMonitor
============

Python based monitoring system.
------------------------------


Features:
--------
1. Pluggable format of input.
    ie you can use xml or json or nagios_format or another python program to input your configurations ( to monitor your servers/services )
2. Pluggable protocol.
    ie you can use nrpe or MQ's or xmlrpc's or other protocols to communicate to the nodes
3. Use the data.
    ie Use the probed data to graph or email alert or IM alert or send to prediction_tools

Architectural diagram:
---------------------
https://docs.google.com/drawings/d/1ygof8i1qVcabZBiHoPN7tNNkSpbVaVYN6zy6mGHXlnU
    


Overall flow:
------------
1. Configurations are present in (sqlite | xml | mysql | ...) .
2. Reading configs Server knows WHOM to monitor WHAT and WHEN.
3. Server makes an (xmlrpc|http|tcp|nrpe|zmq|.....) connection with a validating string to client and then the connection is closed.
4. Client runs the probe/monitor and gets the output.
5. Client makes a new (http|tcp|nrpe|.....) connection to server responding with validating_string + output + timestamp back to server.
6. Server saves the historical data in (sqlite | mysql | rrd | graphite | ...)

 
