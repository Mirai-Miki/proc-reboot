proc-reboot

A python script for unix based systems that runs a list of processes and
restarts them when they end for any reason.

PROC - is the list of process Paths. Add any processes you wish to run
       to this list.

running the script with stdout piped into a log file is the ideal way
to run. eg "$ python proc-reboot > log.txt 2>1&"
