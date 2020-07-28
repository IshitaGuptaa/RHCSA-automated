#!/usr/bin/python36
import subprocess as s

print()

IPsys = input("Enter system's IP you want to trigger: ")
Passwd = input ("Enter system's IP: ")

print("Note the program is only valid for the systems known to your system. as the first time we use ssh it asks for yes/no, important factor for security")


print("""
Press 1: RAM & Storage available
Press 2: Linux Distro name & kernel name
Press 3: System MAC address
Press 4: Free up RAM
Press 5: to exit
""")

print("enter ur choice : " , end='')
# os.system("echo  enter your choice  |  festival  --tts")

ch = input()

print(ch)

if int(ch) == 1:
	a=s.getoutput("sshpass -p {} ssh root@{} df -hT | grep /dev/mapper/rhel-root| cut -c 34-36".format(Passwd,IPsys))
	print("Storage available: "+ a)
	a=s.getoutput("sshpass -p {} ssh root@{} free -m | grep Mem | cut -b 42-44".format(Passwd,IPsys))
	print("RAM available: "+a)

elif int(ch) == 2:

	a=s.getoutput("sshpass -p {} ssh root@{} cat /etc/*-release | grep NAME | head -1".format(Passwd,IPsys))
	print("Linux Distro: "+a)

	a=s.getoutput("sshpass -p {} ssh root@{} uname -r".format(Passwd,IPsys))
	print("Kernel Release: "+a)

elif int(ch) == 3:
				
	MACaddr =s.getoutput("ifconfig enp0s3 | grep ether | tr -s ' '| cut -c 8-15")
	MACaddr = MACaddr.replace(':','')
	a=s.getoutput("cat extra/mac-vendor.txt | grep {}|cut -d ' ' -f 2- ".format(MACaddr))
	print(a)

elif int(ch) == 4:

	s.getoutput("sshpass -p {} ssh root@{} echo 3>/proc/sys/vm/drop_caches".format(Passwd,IPsys))
	print("Done")
elif int(ch) == 5:
	print("exit")

else:
	print("i dont support")

