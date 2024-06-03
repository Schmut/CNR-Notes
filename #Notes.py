#Notes
#Note Maker program for premade notes 
class Email():
    #initializes variables
    def __init__(self,User,requester,distro_email=None):
        self.User = User
        self.requester = requester
        self.distro_email = distro_email
    #Create email account notes
    def create(self):
        print(requester,"requested for",User,"to be created")
        print("Connected to Office 365 admin center")
        print("Created an email for",User)
        print("Recorded email credentials")
        print("Set up multifactor authentication")
        print("Sent credentials to", requester)
        print("")
    #delete email account notes
    def delete(self):
        print(requester,"requested for",User,"to be terminated")
        print("Connected to Office 365 admin center")
        print("Blocked sign in for",User)
        print("Reset email credentials")
        print("Converted",User,"to a shared mailbox")
        print("Removed licenses")
        print("")
    #reset email password note
    def reset(self):
        print(requester,"requested for",User+"'s password to be reset")
        print("Connected to Office 365 admin center")
        print("Reset email password")
        print("Sent password to",requester)
        print("")
    #Distro note
    def distro(self):
        print(requester,"requested for",User,"to be added to",distro_email)
        print("Connected to Office 365 admin center")
        print("Added",User,"to",distro_email,"distribution list")
        print("")

class AD():
    #Initializes variables 
    def __init__(self,User,requester):
        self.User = User
        self.requester = requester
    #create active directory note
    def create(self):
        print(requester,"requested for",User,"to be created")
        print("Connected to Domain Controller")
        print("Created active directory credentials for",User)
        print("Recorded active directory credentials")
        print("Sent credentials to", requester)
        print("")
    #delete active directory note
    def delete(self):
        print(requester,"requested for",User,"to be terminated")
        print("Connected to the domain controller")
        print("Disabled",User +"'s active directory account")
        print("Moved",User,"to disabled user's list")
        print("")
    #reset active directory note
    def reset(self):
        print(requester,"requested for",User,"password to be reset")
        print("Connected to the domain controller")
        print("Reset",User,"password")
        print("Recorded password")
        print("Sent password to",requester)
        print("")

#runs program
while True:
    print ("Note Maker")
    User = input("Who is the user: ")
    requester = input("Who sent in the request: ")
    print("")
    options = input("""Choose an option
1. Email Creation
2. Active Directory Creation
3. Email termination
4. Active Directory termination
5. Reset email password
6. Reset active directory password
7. Add User to distribution list 
Option: """)

    if options == "7":
        print("")
        distro_email = input("What is the distribution list email?: ")
        print("")

    #connects option with text
    if options == "1":
        print("")
        e=Email(User,requester)
        e.create()
    elif options == "2":
        print("")
        a=AD(User,requester)
        a.create()
    elif options == "3":
        print("")
        e=Email(User,requester)
        e.delete()
    elif options == "4":
        print("")
        a=AD(User,requester)
        a.delete()
    elif options == "5":
        print("")
        e=Email(User,requester)
        e.reset()
    elif options == "6":
        print("")
        a=AD(User,requester)
        a.reset()
    elif options == "7":
        print("")
        e=Email(User,requester,distro_email)
        e.distro()
    else:
        print("")
        print("Option not available")
    
    again = input("Do you want to run the script again? (y/n): ")
    if again == "n":
        break
    elif again == "y":
        pass