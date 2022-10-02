import os
def anmenu():
    print("""
    Press 1: To Install ansible
    Press 2: To Solve Installation problem/Error
    Press 3: To check Inventories
    Press 4: To Install Software in Managed/Target Node
    Press 5: To run Command in Managed/Target Node
    Press 6: To Setup Web Server in Managed/Target Node
    Press 7: To Check modules list in Ansible System
    Press 8: To Check manual of module
    Press 9: To Check Target Node details
    Press 10: To exit
    """)

def runanmenu():
    while True:
            print()
            print("Enter Your Choice : ", end='')
            userinp = int(input())
            if userinp == 1:
                os.system("dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm -y ; yum install ansible -y")
            elif userinp == 2:
                os.system("yum update -y; cd /etc/yum.repos.d/ ; rm -f *.repo ; dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm -y ; yum install ansible -y")
            elif userinp == 3:
                os.system("ansible all --list-hosts")
            elif userinp == 4:
                ipoftnode = input("Enter Ip address of Target Node : ")
                swname  = input("Enter software name : ") 
                os.system("ansible {0} -m package -a 'name={1} state=present'".format(ipoftnode , swname))
            elif userinp == 5:
                ipoftnode = input("Enter Ip address of Target Node : ")
                cmdname  = input("Enter Command name : ") 
                os.system("ansible {0} -m command -a {1}".format(ipoftnode , cmdname))
            elif userinp == 6:
                ipoftnode = input("Enter Ip address of Target Node : ")
                os.system("ansible {0} -m package -a 'name=httpd state=present' ; ansible {0} -m copy -a 'dest=/var/www/html src=/root/b.html' ; ansible {0} -m service -a 'name=httpd state=started enabled=yes' ; ansible {0} -m firewalld -a 'state=disabled immediate=yes port=80/tcp'"
.format(ipoftnode))
            elif userinp == 7:
                os.system("ansible-doc -l")
            elif userinp == 8:
                mname = input("Enter module name : ")
                os.system("ansible-doc {0}".format(mname))
            elif userinp == 9:
                ipoftnode = input("Enter Ip address of Target Node : ")
                os.system("ansible {0} -m setup".format(ipoftnode))
            elif userinp == 10:
                break
            else:
                print("Not Supported")
            input("Press Enter to Continue ........")
            os.system("clear")
            anmenu()