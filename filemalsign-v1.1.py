#!/usr/bin/env python
# -*- coding: utf-8 -*-

__description__ = 'FILEMalSign is just a very simple script for know if a file is a malware.'
__version__ = '1.1'
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
		if (entry.find(sha256h) > 0):
			sigid,sha256,malint=entry.split(":")
			print Back.WHITE + Style.DIM + Fore.BLACK + "\nMalware" + Fore.BLUE + Style.DIM + "Intelligence" + Fore.BLACK + Style.DIM + ": " + Fore.RED + malint
			sys.exit(1)

if __name__ == '__main__': 	
	if len(sys.argv) < 2:
		sys.exit(1)

	signDB = "malsignDB"	
	malint = ""
			
	if len(sys.argv) > 2:
		md5 = hashlib.md5(open(sys.argv[2],'rb').read())
		md5h = md5.hexdigest()
		sha1 = hashlib.sha1(open(sys.argv[2],'rb').read())
		sha1h = sha1.hexdigest()
		sha256 = hashlib.sha256(open(sys.argv[2],'rb').read())
		sha256h = sha256.hexdigest()
       	print Fore.GREEN + Style.DIM + "\nFilename: "  + Fore.WHITE + Style.DIM + (sys.argv[2])
        print Fore.GREEN + Style.DIM + "Filesize: " + Fore.WHITE + Style.DIM + str(os.path.getsize(sys.argv[2])) + " bytes"
		print Fore.GREEN + Style.DIM + "MD5: " + Fore.WHITE + Style.DIM +  md5h
		print Fore.GREEN + Style.DIM + "SHA1: " + Fore.WHITE + Style.DIM +  sha1h
		print Fore.GREEN + Style.DIM + "SHA256: " + Fore.WHITE + Style.DIM + sha256h
        	check(malint)
        print Fore.RED + "\nMaybe you're forgetting to add the '-o' parameter. The correct use is 'python FILEMalSign.py -o [filepath]'. Please check it and try again.\n"
        print "or"
        print "\nNo AV veredict was found. You can taking the data sha256 and add the signature in malsignDB file for detect it or let me know sharing sha256 hash data to jamieres-[at]-gmail-[dot]-com and I will add it for you.\n"

