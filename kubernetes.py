import os
def kubemenu():
    print("""
    Press 1: To Install kubectl
    Press 2: To Start Minikube Cluster
    Press 3: To Stop Minikube Cluster
    Press 4: To Launch Pod via Deployment
    Press 5: To Expose Launch Pod
    Press 6: To Delete pod
    Press 7: To Scale in Pods
    Press 8: To Scale out Pods
    Press 9: To Check total pods Running
    Press 10: To Check details of Running Pod
    Press 11: To Check Cluster Info/IP
    Press 12: To Delete All in minikube cluster
    Press 13: To Exit
    """)

def runkubemenu():
    while True:
            print()
            print("Enter Your Choice : ", end='')
            userinp = int(input())
            if userinp == 1:
                pass
                """os.system("cat <<EOF > /etc/yum.repos.d/kubernetes.repo[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
EOF; yum install kubectl -y")"""
            elif userinp == 2:
                os.system("minikube start")
            elif userinp == 3:
                os.system("minikube stop")
            elif userinp == 4:
                podname = input("Enter Your Pod name : ")
                imgname = input("Enter image Name : ")
                os.system("kubectl create deploy {0} --image={1}".format(podname,imgname))
                print("Check Deployment .......")
                os.system("kubectl get deploy")
            elif userinp == 5:
                depname = input("Enter Your Deploy Name : ")
                os.system("kubectl expose deploy {0} --port=80 --type=NodePort".format(depname))
                print("See Exposed Pods .......")
                os.system("kubectl.exe get service")
            elif userinp == 6:
                podname = input("Enter Your Pod name : ")
                os.system("kubectl delete pod {0}".format(podname))
            elif userinp == 7:
                depname = input("Enter Your Deployment name : ")
                replicas = int(input("Enter replica number : "))
                os.system("kubectl.exe scale deploy {0} --replicas={1}".format(depname,replicas))
            elif userinp == 8:
                depname = input("Enter Your Deployment name : ")
                replicas = int(input("Enter replica number : "))
                os.system("kubectl.exe scale deploy {0} --replicas={1}".format(depname,replicas))
            elif userinp == 9:
                os.system("kubectl.exe get pods")
            elif userinp == 10:
                podname = input("Enter Your Pod name : ")
                os.system("kuberctl describe {0}".format(podname))
            elif userinp == 11:
                os.system("kubectl cluster-info")
            elif userinp == 12:
                os.system("kubectl delete all --all")
            elif userinp == 13:
                break
            input("Press Enter to Continue ........")
            os.system("cls")
            kubemenu()
kubemenu()
runkubemenu()