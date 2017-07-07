#!/usr/bin/env python
# -*- coding: utf-8 -*-

__description__ = 'FILEMalSign is just a very simple script for know if a file is a malware.'
__version__ = '1.0'
__author__ = 'Jorge (Pistus) Mieres'
__contact__ = 'jamieres-[at]-gmail-[dot]-com'

import sys,os,hashlib,colorama
from colorama import Fore, Back, Style, init
init()

def check(malint):
	signDB = "malsignDB"
	
	try:
		FILE  = open (signDB,"r" )   
		entries = FILE.readlines()
		FILE.close()

	except IOError:
		print "\nThe AV nomenclature can not be checked because the malsignDB file does not exist. Please check if this file exist in same folder and try again.\n"
		sys.exit(1)
		
	for entry in entries:
		if (entry.find(defhash) > 0):
			sigid,sha256,malint=entry.split(":")
			print Back.WHITE + Style.DIM + Fore.BLACK + "\nMalware" + Fore.BLUE + Style.NORMAL + "Intelligence" + Fore.BLACK + Style.NORMAL + ": " + Fore.RED + malint
			sys.exit(1)

if __name__ == '__main__': 	
	if len(sys.argv) < 2:
		sys.exit(1)

	signDB = "malsignDB"	
	malint = ""
			
	if len(sys.argv) > 2:
		sha256 = hashlib.sha256(open(sys.argv[2],'rb').read())
		defhash = sha256.hexdigest()
       		print "\nFilename: "  + Style.DIM + (sys.argv[2])
        	print Fore.WHITE + Style.NORMAL + "Filesize: " + Style.DIM + str(os.path.getsize(sys.argv[2])) + " bytes"
		print Fore.WHITE + Style.NORMAL + "Sha256: " + Style.DIM + defhash
        	check(malint)
        print Fore.RED + "\nMaybe you're forgetting to add the '-o' parameter. The correct use is 'python FILEMalSign.py -o [filepath]'. Please check it and try again.\n"
        print "or"
        print "\nNo AV veredict was found. You can taking the data sha256 and add the signature in malsignDB file for detect it or let me know sharing sha256 hash data to jamieres-[at]-gmail-[dot]-com and I will add it for you.\n"

