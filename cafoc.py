#!/usr/bin/python

# Program name: CAFOC aka Config Automation For Old Crap
# Verion .004beta 
#

import sys
import telnetlib
import datetime


#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)

def the_engine(device_list,command_list,var03a,var06a,var04a,var05a):
	if '-D' in sys.argv:
		print str(datetime.datetime.now()) + ' - Debugging info : Entering the engine'
		print str(datetime.datetime.now()) + ' - Debugging info :'+ var03a
		print str(datetime.datetime.now()) + ' - Debugging info :'+ var06a
		print str(datetime.datetime.now()) + ' - Debugging info :'+ var04a
		print str(datetime.datetime.now()) + ' - Debugging info :'+ var05a
		print str(datetime.datetime.now()) + ' - Debugging info :'+ str(command_list)
		print'\n\n\n'

	for line in device_list:
		#print 'line : '+ line

		if '-D' in sys.argv:
			print str(datetime.datetime.now()) + ' - Debugging info : Attempting Device : ' + str(line)
			#print str(datetime.datetime.now()) + ' - Debugging info : ' + str(type(line))
			#print str(datetime.datetime.now()) + ' - Debugging info : ' + line
			
		#host = var03a
		host=line
		password = var06a
		command=var04a
		user=var05a 
		
		if '-D' in sys.argv:
			#print str(datetime.datetime.now()) + ' - Debugging info : Device : '+host
			print str(datetime.datetime.now()) + ' - Debugging info : Password : '+password
			print str(datetime.datetime.now()) + ' - Debugging info : Command : '+command
			print str(datetime.datetime.now()) + ' - Debugging info : User : '+user
		
		
		#if '-u' in sys.arv and 
		
		#if '-u' in sys.argv:
		if host is 'na':
			#var11=0
			#for line in sys.argv:
			#		var11=var11+1
			#		if line == '-u':
			#				break
			#print '*** The username is : '+sys.argv[var11]
			#print '*** The password is : '+password
			
			telnet  = telnetlib.Telnet(host)
			telnet.read_until('Username:', 1)
			telnet.write(user + '\r')
			telnet.read_until('Password:', 1)
			telnet.write(password + '\r')
			telnet.write('en' + '\r\n')
			telnet.write(password + '\r')
				
		else:			
			telnet  = telnetlib.Telnet(host)
			telnet.read_until('Password:', 3)
			telnet.write(password + '\r')
			telnet.write('en' + '\r\n')
			telnet.write(password + '\r')
		
		
		telnet.write('terminal length 0' + '\r\n')
		
		#telnet.write('show clock' + '\r\n')
		
		if len(command_list)>1:
			for line in command_list:
				telnet.write(line + '\r\n')
		
		else:
				telnet.write(var04a + '\r\n')
		#telnet.write('show ip int brief | inc up' + '\r\n')
		#telnet.write('show int desc | inc up' + '\r\n')
		telnet.write('exit' + '\r')
		
		b=telnet.read_all()
		print b		
		
def telNetCall(var03a,var06a,var04a,var05a,device_list):
	for line in device_list:
	#host  = "ip_address"
	#password = "password"
		host = var03a
		password = var06a
		command=var04a
		user=var05a 
		
		telnet  = telnetlib.Telnet(host)
		telnet.read_until('Password:', 3)
		telnet.write(password + '\r')
		telnet.write('en' + '\r\n')
		telnet.write(password + '\r')
		#telnet.write('show clock' + '\r\n')
		telnet.write(var04a + '\r\n')
		#telnet.write('show ip int brief | inc up' + '\r\n')
		#telnet.write('show int desc | inc up' + '\r\n')
		telnet.write('exit' + '\r')
		
		b=telnet.read_all()
		print b
		
		# pending debug : print 'host : '+host
		# pending debug : print 'passwod : '+password
		# pending debug : print 'command : '+command
		# pending debug : print 'user : '+user
		# pending debug : pass
		print device_list
		
def main(varx):

	#-----------------------------------
	# Variables
	var01a='na'
	var02a='na'
	var03a='na'
	var04a='na'
	var05a='na'
	var06a='na'
	var07a='na'
	var08a='na'
	var09a='na'
	var10a='na'
	
	device_list=[]
	command_list=[]
	#-----------------------------------

	if '-v' in str(varx):
		print 'version: .004beta'
		quit()

	if '-h' in str(sys.argv):
		print'''
		Available arguments:
		-v version
		-h help
		-c command
		-u username
		-p password
		-n enable
		-m multiple devices, in single quotes, seperated by comma. Example: '10.0.0.1,10.0.0.2,10.0.0.3'
		-D debugging info
		-t todo
		-f output file. Example 'output.txt'
		-P load a plan
		
		Example usage:
		python cafoc.py -c 'show clock' -u admin -p ccna -d 10.0.0.200
		'''
		var01=len(sys.argv)
		var02=0
		for line in sys.argv:
			var02=var02+1
			if line == '-h':
				break
		#print 'location is:'+str(var02)
		quit()

	if '-D' in str(sys.argv):
		print str(datetime.datetime.now()) +  ' - Including debug output'
		log001 = str(datetime.datetime.now()) +  ' - Including debug output\n'
		with open("/var/log/cafoc.txt", "a") as myfile:
			myfile.write(log001)
	
		print str(datetime.datetime.now()) +  ' - Initial data input'
		log001 = str(datetime.datetime.now()) +  ' - Initial data input\n'
		with open("/var/log/cafoc.txt", "a") as myfile:
			myfile.write(log001)		

		#print'debug output is:'
		#print'location is:'
		
	if '-d' in str(sys.argv):
	# Device 
                var03=0
                for line in sys.argv:
                        var03=var03+1
                        if line == '-d':
                                break
		# pending debug : print'the device ip is: '+str(sys.argv[var03])
		var03a = str(sys.argv[var03])
		device_list.append(var03a)
		if '-D' in sys.argv:
			print str(datetime.datetime.now()) + ' - Debugging info : Device info : ' + var03a
			log001 = str(datetime.datetime.now()) + ' - Debugging info : Device info : \n'
			with open("/var/log/cafoc.txt", "a") as myfile:
				myfile.write(log001)
			
		#print'location is:'
	if '-c' in str(sys.argv):
	# Command
		var04=0
		for line in sys.argv:
			var04=var04+1
			if line == '-c':
				break
		# pending debug : print'the command is: '+str(sys.argv[var04])
		var04a = str(sys.argv[var04])
		
		if '-D' in sys.argv:
			print str(datetime.datetime.now()) + ' - Debugging info : Command entered : ' + var04a
			log001 = str(datetime.datetime.now()) + ' - Debugging info : Command entered : ' + var04a+'\n'
			with open("/var/log/cafoc.txt", "a") as myfile:
				myfile.write(log001)
		#print'the command ip is'
		#print'location is:'

	if '-f' in str(sys.argv):
	# File export
		print'the output will be directed to file:'
		print'location is:'

		
		
		
	if '-u' in str(sys.argv):
	# Username
		var05=0
		for line in sys.argv:
				var05=var05+1
				if line == '-u':
						break
		# pending debug : print'the username is: '+str(sys.argv[var05])
		var05a = str(sys.argv[var05])
		#print'username is:'
		#print'location is:'
		if '-D' in sys.argv:
			print str(datetime.datetime.now()) +  ' - Debugging info : Username : ' + var05a
			log001 = str(datetime.datetime.now()) +  ' - Debugging info : Username : ' + var05a+'\n'
			with open("/var/log/cafoc.txt", "a") as myfile:
				myfile.write(log001)

	if '-p' in str(sys.argv):
	#Password
		#print'password is:'
		#print'location is:'
		var06=0
		for line in sys.argv:
			var06=var06+1
			if line == '-p':
				break
		# pending debug : print'the password is: '+str(sys.argv[var06])
		var06a = str(sys.argv[var06])
		if '-D' in sys.argv:
			print str(datetime.datetime.now()) + ' - Debugging info : Password : ' + var06a
			log001 = str(datetime.datetime.now()) + ' - Debugging info : Password : ' + var06a+'\n'
			with open("/var/log/cafoc.txt", "a") as myfile:
				myfile.write(log001)
			
	if '-e' in str(sys.argv):
			#print'enable is:'
			#print'location is:'
			var07=0
			for line in sys.argv:
					var07=var07+1
					if line == '-e':
							break
			# pending debug : print'the enable password is: '+str(sys.argv[var07])

	if '-m' in str(sys.argv):
                #print'enable is:'
                #print'location is:'
                var08=0
                for line in sys.argv:
                        var08=var08+1
                        if line == '-m':
                                break
                # pending debug : print'the devices are: '#+str(sys.argv[var08])
		for line in sys.argv[var08].split(','):
			# pending debug : print line
			device_list.append(line)
		if '-D' in sys.argv:
			print str(datetime.datetime.now()) + ' - Debugging info : The device list is : ' + str(device_list)
			log001 = str(datetime.datetime.now()) + ' - Debugging info : The device list is : ' + str(device_list)+'\n'
			with open("/var/log/cafoc.txt", "a") as myfile:
				myfile.write(log001)
				

	if '-P' in sys.argv:
		print '-P was found'
		#print'enable is:'
		#print'location is:'
		var09=0
		for line in sys.argv:
				var09=var09+1
				if line == '-P':
						break	
		
		print str(datetime.datetime.now()) + ' - Debugging info : Playbook to open : '+ str(sys.argv[var09])
		file_object  = open(str(sys.argv[var09]), 'r') 
		for line in file_object:
			command_list.append(line)
			
		for line in command_list:
			print line.strip('\n')
			
	if '-D' in sys.argv:
		print str(datetime.datetime.now()) +  ' - Debugging info : ' + str(device_list)	
				
	#telNetCall(var03a,var06a,var04a,var05a)
	the_engine(device_list,command_list,var03a,var06a,var04a,var05a)
		
varx=sys.argv
main(varx)
