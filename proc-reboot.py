# Author: Mirai-Miki
# Process rebooter for Unix systems.
# Restarts any process that stops for any reason.

from subprocess import Popen
from time import sleep
import os
import signal
import sys

NODE = "node"
# Add paths of Bots to PROC list
PROC = ["/home/pi/programs/discord/dice/bot.js"]
WAIT = 10

################################# Functions ###################################

def receiveSignal(signalNumber, frame):
	print("Shutting Down")
	for i in range(len(pid)):
		os.killpg(os.getpgid(pid[i]), signal.SIGKILL)
		print("Killed: "+str(pid[i]))
		
	print("Shutdown Completed - Goodbye")
	exit()

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
			while (True): # Forever reboot on bots end
				print("Booting: "+PROC[i])
				sys.stdout.flush()
				proc = Popen([NODE, PROC[i]])
				status = proc.wait()
				print((PROC[i]+" Exited with code: "+str(status)))
				sys.stdout.flush()
				sleep(WAIT)
	# After all bots have been started on there forever loop wait for shutdown
	signal.pause()