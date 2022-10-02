import os
def linuxmenu():
	print("""
	Press 1 : To run date
	Press 2 : To Run cal
	Press 3 : To Make dir
	Press 4 : To Run list
	Press 5 : To Get Ip address
	Press 6 : To Setup Web Server
	Press 7 : To Setup C++
	Press 8 : To Configure yum  
	Press 9 : To Install Any Software
        Press 10: Check Software installed or not in OS
	Press 11: To Create file  
	Press 12: To Create User  
	Press 13: To Delete User  
        Press 14: To Create Group
        Press 15: To Add user in Group
        Press 16: To Check Internet Connectivity
        Press 17: To Stop SELinux
	Press 18: To Start SELinux
	Press 19: To Check status of SELinux Security
	Press 20: To Set Privileges Escalation(Sudo Power) in user 
	Press 21: To Setup SSH key Setup between 2 systems
	Press 22: To back main menu
	""")

def runlinuxmenu():
	while True:
		print()
		print("Enter Your choice : ", end='')
		userinp = int(input())
		if userinp == 1:
			os.system("date")
		elif userinp == 2:
			os.system("cal")
		elif userinp == 3:
			foldername = input("Enter folder name : ")
			os.system("mkdir {0}".format(foldername))
		elif userinp == 4:
			os.system("ls")
		elif userinp == 5:
			os.system("ifconfig enp0s3")
		elif userinp == 6:
			os.system("yum install httpd -y ; cd /var/www/html; echo new > index.html ; systemctl enable httpd --now")  		
		elif userinp == 7:
			os.system("yum install gcc-c++ -y")		
		elif userinp == 8:
			os.system("cp dvd.repo /etc/yum.repos.d/ ; yum repolist")		
		elif userinp == 9:
			softwarename = input("Enter Software name : ")
			os.system("yum install {0} -y".format(softwarename))
		elif userinp == 10:
			softwarename = input("Enter Software name to check : ")
			os.system("rpm -q (0)".format(softwarename))
		elif userinp == 11:
			fname=input("Enter File Name")
			os.system("touch {0}".format(fname))
		elif userinp == 12:
			uname = input("Enter Username to create")  
			os.system("useradd {0}".format(uname))      
		elif userinp == 13:
			duname = input("Enter Username to delete")  
			os.system("userdel {0}".format(dunname))        
		elif userinp == 14:
			gname = input("Enter Groupname to create")  
			os.system("groupadd {0}".format(gname))      
		elif userinp == 15:
			uname = input("Enter Username to create")  
			os.system("useradd {0}".format(uname))      
			gname = input("Enter Groupname to create")  
			os.system("groupadd {0}".format(gname))      
			print("Add {0} user in group".format(uname))
			os.system("useradd -G (1) {0}".format(uname, gname))        
		elif userinp == 16:
			os.system("ping 8.8.8.8")
		elif userinp == 17:
			os.systeM("setenforce 0")
		elif userinp == 18:
			os.systeM("setenforce 1")
		elif userinp == 19:
			os.systeM("getenforce")
		elif userinp == 20:
			uname = input("Enter Username to create : ")  
			os.system("useradd {0}".format(uname))
			os.system("echo (0) 	ALL=ALL    NOPASSWD: ALL >> /etc/sudoers".format(uname)) 
		elif userinp == 21:
			print("SSH key Generating ......")
			os.system("ssh-keygen")
			ipadd = input("Enter Ip of 2nd system : ")
			os.system("ssh-copy-id root@{0}".format(ipadd))
			print("Setup successfull Check via login")
		elif userinp == 22:
			break
		input("Press Enter to Continue ........")
		os.system("clear")
		linuxmenu()
