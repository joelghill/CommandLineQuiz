
import subprocess
import os

initial_d = ''

introduction = ('The command line is a text interface for your computer.' 
	+ 'It\'s a program that takes in commands, which it passes on to the computer\'s operating system to run.'
	+ 'The following intactive quiz will guide you through some of the basic commands you can use to navigate your computer.')


q1h = '####### Files, Folders, and Directories ########'

def initialize():
	initial = os.getcwd() + "/FakeComputer"
	os.chdir(initial)
	return initial

def writeCommand(command):
	p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	for line in p.stdout.readlines():
	    print line,
	retval = p.wait()

def change_d(dir):
	print("Initial Directory:  " + initial_d)
	if(dir[0] == "/"):
		os.chdir(os.getcwd()+ dir)
	else:
		os.chdir(os.getcwd()+ "/" + dir)


initial_d = initialize()

while(True):
	c = raw_input('Enter a command: ')
	if(c == 'exit'):
		break
	elif(c[:3] == "cd "):
		change_d(c[3:])
	elif(c[:3] == "pwd"):
		print ("PRINT WORKING DIRECTORY")
	else:
		writeCommand(c)

