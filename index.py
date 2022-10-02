import linux as li
import dsa
import ml
import container as cont
import ansible as an
import kubernetes as kube
import os
def mainmenu():
	print("""
	Press 1: Go to Linux related Commands
	Press 2: Go to DSA related Commands
	Press 3: Go to ML related Commands
	Press 4: Go to Container Based Commands
        Press 5: Go to Ansible Based Commands 
        Press 6: Go to Kubernetes Based Commands 
        Press 7: Go to exit 
	""")
	print()

print()
print("\t\t\tWelcome to Python Menu ")
os.system("tput setaf 5")
print("\t\t\t----------------------")
os.system("tput setaf 7")

while True:
	mainmenu()
	userchoice = int(input("Enter Your Type : "))
	if userchoice == 1:
		li.linuxmenu()
		li.runlinuxmenu()
		#mainmenu()
	elif userchoice == 2:
		dsa.dsamenu()
		dsa.rundsamenu()
                #mainmenu()
	elif userchoice == 3:
		print()
		#mainmenu()
	elif userchoice == 4:
		cont.contmenu()
		cont.runcontmenu()
		#mainmenu()
	elif userchoice == 5:
		an.anmenu()
		an.runanmenu()
	elif userchoice == 6:
		kube.kubemenu()
		kube.runkubemenu()
	elif userchoice  == 6:
		break
	else:
		print("Not Supported")
		input("Press Enter to Continue ........")
		break
