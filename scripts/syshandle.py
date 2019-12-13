#!/usr/bin/env python
import sys 

def CheckPlatform():

	if sys.platform.startswith('win'):
	    #print ("Windows platform")
	    return "WIN32"
	elif sys.platform.startswith('linux'):
	    #print ("Linux platform")
	    return "LINUX"
	else:
		print ("Un-supported platform")
		quit()
