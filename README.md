ThePyMonitor
============

Overall flow:

1. Configurations are present in sqlite.
2. Reading configs Server knows WHOM to monitor WHAT and WHEN.
3. Server makes a (xmlrpc|http|tcp|nrpe|.....) connection with a validating string to client and then the connection is closed.
4. Client runs the probe/monitor and gets the output.
5. Client makes a new (http|tcp|nrpe|.....) connection to server responding with validating_string + output + timestamp back to server.
6. Server saves the historical data in sqlite.

User Guide:
  Configuring:
  APIs to enable/disable/manipulate monitoring
  Dependencies:
  Failover:
  Security:


Design Docs
----------

Components:
1. Scheduler
2. Dispatcher
3. Receiver
also
 DataMgr
 ConnectionMgr
 Oscillator
 
