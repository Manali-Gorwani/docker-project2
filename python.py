import os
import getpass
os.system("tput setaf 2")
print("\t\t\tManali Project")
os.system("tput setaf 3")

print("Please type local")
location = input()

apass = "manali"
password = getpass.getpass("Enter Your Password")
if apass != password:
    print("Authentication failed")
    exit()

while True:
        print("""1. PRESS 1 TO SEE DATE 
press 2 : PRESS 2 TO SEE CALENDER
press 3 : TO START WEB SERVER
Press 4 : TO CREATE YOUR OWN WEBSITE OWNCLOUD 
Press 5 : TO STOP THE THE OF OWNCLOUD
Press 0 : TO EXIT FROM CONTAINER
        """)
        print("Enter Your Choice",end="")
        ch = input()
        print(ch)

        if location == "local":
            if int(ch)==1:
                os.system("date")
            elif int(ch)==2:
                os.system("cal")
            elif int(ch)==3:
                os.system("systemctl start httpd")
                os.system("tput setaf 2")
                print("SERVER STARTED")
            elif int(ch)==0:
                exit()
            elif int(ch)==4:
                os.system("docker-compose up -d")
            elif int(ch)==5:
                os.system("docker-compose stop")
            



