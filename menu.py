import os
import numpy as np
print()
print()
print("\t\t\tWelcome to Python Menu ")
os.system("tput setaf 5")
print("\t\t\t----------------------")
os.system("tput setaf 7")
print()
print("Do you want to run Commands Local/Remote : ", end='')
locremuser=input()
print()
print("""Press 1 : To run date
Press 2 : To Run cal
Press 3 : To Make dir
Press 4 : To Run list
Press 5 : To Get Ip address
Press 6 : To Setup Web Server
Press 7 : To Setup C++
Press 8 : To Configure yum  
Press 9 : To Install Any Software  
Press 10: To Generate random array
Press 11: To Search data using Linear Search Algorithm 
Press 12: To Search data using Binary Search Algorithm 
Press 13: To Sort data using Bubble Sorting Algorithm 
Press 14: To Sort data using Selection Sorting Algorithm
Press 15: To Setup Docker
Press 16: To Check Docker installed or not
Press 17: To Check all docker images 
Press 18: To Check Running containers in Docker
Press 19: To Check both Running/Stop containers in Docker
Press 20: To Launch a new container
Press 21: To Stop container
Press 22: To Start exist/Stop container
Press 23: To Delete a container
Press 24: To Delete All containers
Press 25: To Delete an Image
Press 26: To Delete all Images
Press 27: To Setup Web Server inside Container
Press 28: To Confirm Server properly working or not
Press 29: To Create Own Image 
Press 30: To Exit	""")
print()
if locremuser=='Remote':
	print()
	print("Enter the Ip address : ", end='')
	remip=input()
	while True:
		print("Enter Your choice : ", end='')
		userinp = int(input())
		if userinp == 1:
			os.system("ssh {0} date".format(remip))
		elif userinp == 2:
			os.system("ssh {0} cal".format(remip))
		elif userinp == 3:
			foldername = input("Enter folder name : ")
			os.system("ssh {0} mkdir {1}".format(remip, foldername))
		elif userinp == 4:
			os.system("ssh {0} ls".format(remip))
		elif userinp == 5:
			os.system("ssh {0} ifconfig enp0s3".format(remip))
		elif userinp == 6:
			os.system("ssh {0} yum install httpd -y ; cd /var/www/html; echo new > index.html ; systemctl start httpd; systemctl enable httpd".format(remip))  
		elif userinp == 7:
			os.system("ssh {0} yum install gcc-c++".format(remip))		
		elif userinp == 8:
			os.system("scp dvd.repo {0}:/etc/yum.repos.d/ ; ssh {0} yum repolist".format(remip))		
		elif userinp == 9:
			softwarename = input("Enter Software name : ") 
			os.system("ssh {0} yum install {1} -y".format(remip,softwarename))
		elif userinp == 10:
			arrsize = int(input("Enter Array Size : "))
			a = np.random.randint(1, 100, arrsize)
			print(a) 
		elif userinp == 11:
			arrsize = int(input("Enter Array Size : "))
			a = np.random.randint(1, 100, arrsize)
			print(a)
			searchitem = int(input("Enter Search item : "))
			for i in a:
				if i == searchitem:
					print("Found")
					break								
		elif userinp == 12:
			arrsize = int(input("Enter Array Size : "))
			a = np.random.randint(1, 100, arrsize)
			print(a)
			searchitem = int(input("Enter Search item : "))
			start = 0
			end = len(a)-1
			middle = int( (start + end) / 2 )
			while not(a[middle] == searchitem ):
				if a[middle] < searchitem:
					#print("Go Right side")
					start = middle + 1
					middle = int( (start + end ) / 2)
				elif a[middle] > searchitem:
					#print("Go Left Side")
					end = middle - 1
					middle = int ( ( start + end  ) / 2 )
				#print(start , middle , end)
				if a[middle] == searchitem:
						print("Found")
						break
		elif userinp == 13:
			arrsize = int(input("Enter Array Size : "))
			a = np.random.randint(1, 100, arrsize)
			print()
			print()
			print("Unsorted Data ........")
			print(a)
			for i in range(len(a)-1):
				for j in range(len(a) - 1- i):
				    if a[j] > a[j+1]:
				        a[j], a[j+1] = a[j+1] , a[j]
			print(a)
			print("Data Sorted Successfully .........")
			print()
			print()
		elif userinp == 14:
			myindex=0
			arrsize = int(input("Enter Array Size : "))
			a = np.random.randint(1, 100, arrsize)
			print()
			print()
			print("Unsorted Data ........")
			print(a)
			for i in range(len(a)):
				min_index = i
				for j in range(i , len(a)):
					if a[min_index] > a[j]:
						min_index = j
				a[i] , a[min_index] = a[min_index] , a[i]
			print(a)
			print("Data Sorted Successfully ........")
			print()
			print()
		elif userinp == 15:
			os.system("ssh {0} yum install yum-utils -y; yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/rhel/docker-ce.repo ; yum install docker-ce; systemctl start docker ; systemctl enable docker ".format(remip))
		elif userinp == 16:
			os.system("ssh {0} docker info".format(remip))
		elif userinp == 17:
			os.system("ssh {0} docker images".format(remip))
		elif userinp == 18:
			os.system("ssh {0} docker ps".format(remip))
		elif userinp == 19:
			os.system("ssh {0} docker ps -a".format(remip))
		elif userinp == 20:
			contname = input("Enter container name : ")
			imgname  = input("Enter Image name : ") 
			os.system("ssh {2} docker run -dit --name {0} {1}".format(contname , imgname, remip))
		elif userinp == 21:
			contname = input("Enter container name : ")
			os.system("ssh {1} docker stop {0}".format(contname, remip))
		elif userinp == 22:
			contname = input("Enter container name : ")
			os.system("ssh {1} docker start {0}".format(contname , remip))
		elif userinp == 23:
			contname = input("Enter container name : ")
			os.system("ssh {1} docker rm -f {0}".format(contname, remip))
		elif userinp == 24:
			os.system("ssh {0} docker rm -f $(docker ps -a -q)".format(remip))
		elif userinp == 25:
			imgname = input("Enter Image name : ")
			os.system("ssh {1} docker rmi -f  {0}".format(imgname , remip))
		elif userinp == 26:
			os.system("ssh {0} docker rmi -f $(docker images)".format(remip))
		elif userinp == 27:
			os.system("scp Dockerfile {0}:/root/ ; ssh {0} docker build -t webimg:v1 . ; docker run -dit webimg:v1 ; ".format(remip))
			print("Setup Done or not Check using curl 172.17.0.2")
		elif userinp == 28:
			contip = input("Enter container id address : ") 
			os.system("ssh {1} curl {0}".format(contip , remip))
		elif userinp == 29:
			imgn = input("Enter Image Name : ")
			os.system("ssh {1} docker build -t {0} .".format(imgn,remip))
		elif userinp == 30:
			os.system("exit")
			break
		else:
			print("Not Supported")
		#os.system("clear")
		#input()
		#print("Enter to continue...........")

elif locremuser=='Local':
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
			os.system("yum install httpd -y ; cd /var/www/html; echo new > index.html ; systemctl start httpd; systemctl enable httpd")  		
		elif userinp == 7:
			os.system("yum install gcc-c++ -y")		
		elif userinp == 8:
			os.system("cp dvd.repo /etc/yum.repos.d/ ; yum repolist")		
		elif userinp == 9:
			softwarename = input("Enter Software name : ") 
			os.system("yum install {0} -y".format(softwarename))
		elif userinp == 10:
			print()
			arrsize = int(input("Enter Array Size : "))
			a = np.random.randint(1, 100, arrsize)
			print(a)
		elif userinp == 11:
			print()
			arrsize = int(input("Enter Array Size : "))
			a = np.random.randint(1, 100, arrsize)
			print(a)
			searchitem = int(input("Enter Search item : "))
			for i in a:
				if i == searchitem:
					print("Found")
					break					
		elif userinp == 12:
			print()
			arrsize = int(input("Enter Array Size : "))
			a = np.random.randint(1, 100, arrsize)
			print(a)
			sorta = sorted(a)
			print("Your Sorted data is : ")
			print(sorta)
			searchitem = int(input("Enter Search item : "))
			start = 0
			end = len(sorta)-1
			middle = int( (start + end) / 2 )	
			while not(sorta[middle] == searchitem ):
				if sorta[middle] < searchitem:
					#print("Go Right side")
					start = middle + 1
					middle = int( (start + end ) / 2)
				elif sorta[middle] > searchitem:
					#print("Go Left Side")
					end = middle - 1
					middle = int ( ( start + end  ) / 2 )
				#print(start , middle , end)
				if sorta[middle] == searchitem:
					print("Found")
				else:
					print("Not Found")
		elif userinp == 13:
			print()
			arrsize = int(input("Enter Array Size : "))
			a = np.random.randint(1, 100, arrsize)
			print("Unsorted Data ........")
			print()
			print()			
			print(a)
			for i in range(len(a)-1):
				for j in range(len(a) - 1- i):
				    if a[j] > a[j+1]:
				        a[j], a[j+1] = a[j+1] , a[j]
			print()
			print(a)
			print("Data Sorted Successfully .........")
			print()
		elif userinp == 14:
			print()
			myindex=0
			arrsize = int(input("Enter Array Size : "))
			a = np.random.randint(1, 100, arrsize)
			print()
			print("Unsorted Data ........")
			print()			
			print(a)
			for i in range(len(a)):
				min_index = i
				for j in range(i , len(a)):
					if a[min_index] > a[j]:
						min_index = j
				a[i] , a[min_index] = a[min_index] , a[i]
			print()			
			print(a)
			print()
			print("Data Sorted Successfully ........")
			print()			
		elif userinp == 15:
			os.system("yum install yum-utils -y; yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/rhel/docker-ce.repo ; yum install docker-ce; systemctl start docker ; systemctl enable docker")
		elif userinp == 16:
			os.system("docker info")
		elif userinp == 17:
			os.system("docker images")
		elif userinp == 18:
			os.system("docker ps")
		elif userinp == 19:
			os.system("docker ps -a")
		elif userinp == 20:
			contname = input("Enter container name : ")
			imgname  = input("Enter Image name : ") 
			os.system("docker run -dit --name {0} {1}".format(contname , imgname))
		elif userinp == 21:
			contname = input("Enter container name : ")
			os.system("docker stop {0}".format(contname))
		elif userinp == 22:
			contname = input("Enter container name : ")
			os.system("docker start {0}".format(contname))
		elif userinp == 23:
			contname = input("Enter container name : ")
			os.system("docker rm -f {0}".format(contname))
		elif userinp == 24:
			os.system("docker rm -f $(docker ps -a -q)")
		elif userinp == 25:
			imgname = input("Enter Image name : ")
			os.system("docker rmi -f  {0}".format(imgname))
		elif userinp == 26:
			os.system("docker rmi -f $(docker images)")
		elif userinp == 27:
			os.system("docker build -t webimg:v1 . ; docker run -dit webimg:v1 ; ")
			print("Setup Done or not Check using curl 172.17.0.2")
		elif userinp == 28:
			contip = input("Enter container id address : ") 
			os.system("curl {}".format(contip))
		elif userinp == 29:
			imgn = input("Enter Image Name : ")
			os.system("docker build -t {0} .".format(imgn))
		elif userinp == 30:
			break
		else:
			print("Not Supported")
		#input("Enter to continue...........")
		#os.system("clear")
else:
	print("Not Supported")
