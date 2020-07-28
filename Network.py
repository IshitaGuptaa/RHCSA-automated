#!/usr/bin/python36
import subprocess as s


IPsys = input("Enter system's IP you want to trigger: ")
Passwd = input ("Enter system's IP: ")

print("Note the program is only valid for the systems known to your system. as the first time we use ssh it asks for yes/no, important factor for security")


print("""
Press 1: IP address show
Press 2: Network connections show
Press 3: New Connection add
Press 4: Network Connection delete
Press 5: to exit
""")

print("enter ur choice : " , end='')
# os.system("echo  enter your choice  |  festival  --tts")

ch = input()

print(ch)

if int(ch) == 1:
	a=s.getoutput("sshpass -p {} ssh root@{} ip addr show enp0s3 | grep inet |  tr -s ' ' | cut -b 7-22 | head -n 1".format(Passwd,IPsys))
	print(a)
elif int(ch) == 2:

	a=s.getoutput("sshpass -p {} ssh root@{} nmcli con show".format(Passwd,IPsys))
	print(a)
elif int(ch) == 3:
				
	IPrem = s.getoutput("sshpass -p {} ssh root@{} ip addr show enp0s3 | grep inet |  tr -s ' ' | cut -b 7-22 | head -n 1".format(Passwd,IPsys))
	print("Remote system's current IP that will be used to make connection static: {}".format(IPrem))
	a=s.getoutput("sshpass -p {} ssh root@{} nmcli con add con-name home1 ifname enp0s3 type ethernet ip4 192.168.0.105/24 gw4 192.168.0.1 ipv4.dns 8.8.8.8 connection.autoconnect yes".format(Passwd,IPsys))
	print(a)

elif int(ch) == 4:
	delete= input("Enter the connection you want to delete ")
	a=s.getoutput("sshpass -p {} ssh root@{} nmcli con delete {}".format(Passwd,IPsys,delete))
	print(a)
elif int(ch) == 5:
	print("exit")

else:
	print("i dont support")

