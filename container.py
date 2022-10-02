import os
def contmenu():
	print("""
	Press 1:  To Setup Docker
	Press 2:  To Check Docker installed or not
	Press 3:  To Check all docker images 
	Press 4:  To Check Running containers in Docker
	Press 5:  To Check both Running/Stop containers in Docker
	Press 6:  To Launch a new container
	Press 7:  To Stop container
	Press 8:  To Start exist/Stop container
	Press 9:  To Delete a container
	Press 10: To Delete All containers
	Press 11: To Delete an Image
	Press 12: To Delete all Images
	Press 13: To Setup Web Server inside Container
	Press 14: To Confirm Server properly working or not
	Press 15: To Create Own Image 
	Press 16: To Back to main menu
	""")

def runcontmenu():
	while True:
		print()
		print("Enter Your choice : ", end='')
		userinp = int(input())
		if userinp == 1:
			os.system("yum install yum-utils -y; yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/rhel/docker-ce.repo ; yum install docker-ce; systemctl start docker ; systemctl enable docker")
		elif userinp == 2:
			os.system("docker info")
		elif userinp == 3:
			os.system("docker images")
		elif userinp == 4:
			os.system("docker ps")
		elif userinp == 5:
			os.system("docker ps -a")
		elif userinp == 6:
			contname = input("Enter container name : ")
			imgname  = input("Enter Image name : ") 
			os.system("docker run -dit --name {0} {1}".format(contname , imgname))
		elif userinp == 7:
			contname = input("Enter container name : ")
			os.system("docker stop {0}".format(contname))
		elif userinp == 8:
			contname = input("Enter container name : ")
			os.system("docker start {0}".format(contname))
		elif userinp == 9:
			contname = input("Enter container name : ")
			os.system("docker rm -f {0}".format(contname))
		elif userinp == 10:
			os.system("docker rm -f $(docker ps -a -q)")
		elif userinp == 11:
			imgname = input("Enter Image name : ")
			os.system("docker rmi -f  {0}".format(imgname))
		elif userinp == 12:
			os.system("docker rmi -f $(docker images)")
		elif userinp == 13:
			os.system("docker build -t webimg:v1 . ; docker run -dit webimg:v1 ; ")
			print("Setup Done or not Check using curl 172.17.0.2")
		elif userinp == 14:
			contip = input("Enter container id address : ") 
			os.system("curl {}".format(contip))
		elif userinp == 15:
			imgn = input("Enter Image Name : ")
			os.system("docker build -t {0} .".format(imgn))
		elif userinp == 16:
			break
		else:
			print("Not Supported")
		input("Press Enter to Continue ........")
		os.system("clear")
		contmenu()
