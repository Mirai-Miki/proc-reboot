# Author: Mirai-Miki
# Process rebooter for Unix systems.
# Restarts any process that stops for any reason.

from subprocess import Popen
from time import sleep
import os
import signal
import sys
import datetime

# add CMD for each processor to be run. Must match order of PROC paths
CMD = ["node"]
# Add paths of processors to PROC list
PROC = ["/home/pi/programs/discord/dice/bot.js"]
# Length of time before each reboot in seconds
WAIT = 10

################################# Functions ###################################

def receiveSignal(signalNumber, frame):
	print(currentTime()+" -- Shutting Down")
	for i in range(len(pid)):
		os.killpg(os.getpgid(pid[i]), signal.SIGKILL)
		print(currentTime()+" -- Killed: "+str(pid[i]))
		
	print(currentTime()+" -- Shutdown Completed - Goodbye")
	exit()

def currentTime():
	currentTime = datetime.datetime.now()
	return currentTime.strftime("%H:%M:%S %d/%m/%Y")

################################ Main #########################################

if __name__ == '__main__':
	signal.signal(signal.SIGINT, receiveSignal)
	signal.signal(signal.SIGTERM, receiveSignal)
	pid = []
	print("PID: "+str(os.getpid()))
	sys.stdout.flush()

	for i in range(len(PROC)):
		pid.append(os.fork()) # Spin up new process
		if (pid[i] == 0): # This is the rebooter process
			os.setsid()
			while (True): # Forever reboot on proc end				
				print(currentTime()+" -- Booting: "+PROC[i])
				sys.stdout.flush()
				proc = Popen([CMD[i], PROC[i]])
				status = proc.wait()
				print((currentTime()+" -- "+PROC[i]+\
						" Exited with code: "+str(status)))
				sys.stdout.flush()
				sleep(WAIT)
	# After all procs have been started on a forever loop wait for shutdown
	signal.pause()