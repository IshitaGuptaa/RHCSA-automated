#!/usr/bin/python36
import subprocess as s


print("Note the program is only valid for the systems known to your system. as the first time we use ssh it asks for yes/no, important factor for security")


print("""
Press 1: NFS Server configuration
Press 2: NFS Client configuration
Press 3: Remove connection from server end
Press 4: Remove client's side  connection
Press 5: to exit
""")

print("enter ur choice : " , end='')
# os.system("echo  enter your choice  |  festival  --tts")

ch = input()

print(ch)

if int(ch) == 1:
	
	IPsys = input("Enter server system's IP you want to trigger: ")
	Passwd = input ("Enter system's password: ")
	clientIP=input("Enter Client's IP: ")

	s.getoutput("sshpass -p {} ssh root@{} yum install nfs-utils nfs-utils-lib -y ".format(Passwd,IPsys))
	
	s.getoutput("sshpass -p {} ssh root@{} systemctl start nfs;systemctl enable nfs ".format(Passwd,IPsys))
	
	s.getoutput("sshpass -p {} ssh root@{} mkdir nfsServer; echo '/nfsServer/ {}(rw,sync,no_root_squash)'> /etc/exports ".format(Passwd,IPsys,clientIP))
	
	s.getoutput("sshpass -p {} ssh root@{} systemctl restart nfs ".format(Passwd,IPsys))
	
elif int(ch) == 2:
	clientIP=input("Enter Client's IP: ")
	Passwd = input ("Enter system's password: ")
	s.getoutput("sshpass -p {} ssh root@{} yum install nfs-utils nfs-utils-lib -y ".format(Passwd,clientIP))
	
	s.getoutput("sshpass -p {} ssh root@{} systemctl start nfs;systemctl enable nfs ".format(Passwd,clientIP))
	
	s.getoutput("sshpass -p {} ssh root@{} mkdir /nfsClient; mount 192.168.0.105:/nfsServer /nfsClient/ ".format(Passwd,clientIP))
	
	print(a)
elif int(ch) == 3:
	IPsys = input("Enter server system's IP you want to trigger: ")
	Passwd = input ("Enter system's password: ")
	s.getoutput("sshpass -p {} ssh root@{} echo > /etc/exports ".format(Passwd,IPsys))
	s.getoutput("sshpass -p {} ssh root@{} systemctl restart nfs ".format(Passwd,IPsys))	
	
elif int(ch) == 4:
	clientIP=input("Enter Client's IP: ")
	Passwd = input ("Enter system's password: ")
	s.getoutput("sshpass -p {} ssh root@{} umount /nfsClient/;rm -rf /nfsClient ".format(Passwd,clientIP))
	
	
elif int(ch) == 5:
	print("exit")
else:
	print("i dont support")

