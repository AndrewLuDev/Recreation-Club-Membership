import os
import getpass
from replit import db

allAccounts = []
loginInfo = {}

class accountInfo:
  def __init__(self, username, password, role, name, phone, paid, unpaid, address):
    self.username = username
    self.password = password
    self.role = role
    self.name = name
    self.phone = phone
    self.paid = paid          # number of paid sessions in a row
    self.unpaid = unpaid
    self.address = address

def printTitle():
  print("RECREATION CLUB MEMBERSHIP")
  print("--------------------------")

def printSelections(selections):
  selectionNum = 0  
  for select in selections:
    selectionNum += 1
    print(str(selectionNum) + ". " + str(select))


def main():
    #clears the database
    #clearAll()

    if "admin" not in db.keys():
      db["admin"] = ["admin", "password", "Coach", "Coach123", "6490001234", 0, 0, "123 Address St."]
  
    for user in db.keys():
      #db[user][0]
      #tempUser = accountInfo(username0, password1, role2, name3, phone4, paid5, unpaid6, address7)
      tempUser = accountInfo(db[user][0], db[user][1], db[user][2], db[user][3], db[user][4], db[user][5], db[user][6], db[user][7])
      allAccounts.append(tempUser)
      #loginInfo[username] = password
      loginInfo[db[user][0]] = db[user][1]

      
    mainMenu(loginInfo)

def mainMenu(loginInfo):
  selection = ''
  selections = ["Create Account", "Login", "Quit"]
  while selection.lower() != 'q' and selection != '3':
    printTitle()
    printSelections(selections)
      
    selection = input("Selection Number: ")
    
    if selection == '1':
      register(loginInfo)
    elif selection == '2':
      login('')
    elif selection == '3' or selection.lower() == 'q':
      print("Quitting")
    else:
      os.system('clear')
      mainMenu(loginInfo)
      print("Invalid selection.\n")

def memberScreen(user):
  selections = ["Schedules", "Your Bookings", "Make a Payment", "Logout" ]
  selection = ''
  while selection.lower() != 'q':
    printTitle()
    print("LOGGED IN AS: MEMBER")
    printSelections(selections)

    selection = input("Selection Number: ")

    if selection == '1':
      listSchedule()
    elif selection == '2':
      for item in allAccounts:
        if item.username == user:
          print("you have 0 bookings")
    elif selection == '3':
      printTitle()
      print("LOGGED IN AS: MEMBER")
      makePayment(user)

def listMembers():
  print("Listing All Members:\n")
  ##############################################
  ###############tabulate this later############
  ##############################################
  #Format: Name, Phone number, number of paid classes in a row, number of unpaid classes
  numMembers = 0
  memberList = []
  for username in db.keys():
    if db[username][2] == "Member":
      numMembers += 1
      memberList.append(username)
      #print Member's name, phone number, paid classes in a row and unpaid classes
      print(str(numMembers) + ".", db[username][3], db[username][4], db[username][5], db[username][6])
    else:
      #debugging: prints whoever else is in the database (ie. coaches/treasurers)
      print("somethingsomething",db[username][3], db[username][4], db[username][5], db[username][6])
      
####################################################################################
def modifySpecificMember(user, username):
  
  descNum = input("\nWhich description do you wish to modify?\nEnter the description number: ")

  if int(descNum) < 1 or int(descNum) > 5:
    print("Invalid description nubmer. Please enter a number from 1 to 5")
  else:
    if descNum == '1':
      db[username][3] = input("Please enter the member's First and Last name: \n")
    elif descNum == '2':
      db[username][4] = input("Please enter the member's phone number: \n")
    elif descNum == '3':
      db[username][5] = input("Please enter the member's number of paid classes in a row")
    elif descNum == '4':
      db[username][6] = input("Please enter the member's number of unpaid classes: \n")
    elif descNum == '5':
      db[username][7] = input("Please enter the member's address: \n")
    print("\nThe member's information has been updated.")

  contModify = input("\nContinue modifying this member? Please input Y/N \nOption: ")

  while contModify.lower() != 'n':
    if contModify.lower() == 'y':
      modifySpecificMember(user, username)
    else:
      contModify = input("Invalid option. Please type Y or N\nOption: ")
      

  os.system('clear')
  printTitle()
  listMembers()
  modifyMembers(user)
  
#####################################################################################

def modifyMembers(user):
  numMembers = 0
  memberList = []
  for username in db.keys():
    if db[username][2] == "Member":
      numMembers += 1
      memberList.append(username)

  userNum = int(input("\nModify Member number: "))
        
  #(name, phone, paid, unpaid, address)
  username = memberList[userNum-1]
  printSelections([db[username][3], db[username][4], db[username][5], db[username][6], db[username][7]])

  modifySpecificMember(user, username)

#####################################################################################

def coachScreen(user):
  selections = ["Schedules", "View Members List", "Send Reminders", "Logout"]
  selection = ''


  os.system('clear')
  printTitle()
  print("LOGGED IN AS: COACH")
  printSelections(selections)
  
  while selection.lower() != 'q':

    selection = input ("Selection Number: ")

    while selection.lower() != 'b':
      if selection == '1':
        listSchedule()
      elif selection == '2':
        listMembers()
        selection = input("\n'M' to Modify Members\n'B' Back to Menu\nOption: ")
        
        os.system('clear')
        printTitle()
        if selection.lower() == 'm':
          listMembers()
          modifyMembers(user)
        elif selection.lower() == 'b':
          coachScreen(user)
        else:
          print("Invalid Selection.\n")
      elif selection == '3':
        sendReminders()
      elif selection == '4' or selection.lower() == 'q':
        print("Logging out.\n")
        mainMenu(loginInfo)
        

        

        
def makePayment(user):
  os.system('clear')
  selections = ["Paypal", "Credit Card", "Bitcoin", "Cancel Payment"]
  print("200 classes have not yet been paid for")
  printSelections(selections)
  
  selection = input("Selection Number: ")
  if selection == '1':
    print("Paypal payment option is currently unavailable. Please try again later\n")
  elif selection == '2':
    print("Credit Card payment option is currently unavailable. Please try again later\n")
  elif selection == '3':
    print("Bitcoin payment option is currently unavailable. Please try again later\n")
  elif selection == '4' or selection.lower() == 'q':
    print("Cancelling payment.")
    os.system('clear')
    memberScreen(user)
  makePayment(user)


def register(loginInfo):
  username = input("Enter a username: ")
  while username in loginInfo.keys():  
    print ("Username is already taken.")
    username = input("Enter a username: ")
    
  password = getpass.getpass(prompt="Enter password: ")
  while len(password) < 8:     
    print("Password has to be greater than 8 characters.")
    password = getpass.getpass(prompt="Enter password: ")
  
  defaultRole = "Member"
  name = input("Please enter your first and last name:\n")
  phone = input("Please enter your phone number:\n")
  paid = 0
  unpaid = 0
  address = input("Please enter your address:\n")
  
  newUser = accountInfo(username, password, defaultRole, name, phone, paid, unpaid, address)
  
  db[username] = [username, password, defaultRole, name, phone, paid, unpaid, address]
  #print(db[username])

  allAccounts.append(newUser)
  loginInfo[username] = password
  
  print(f"ACCOUNT CREATED: for user {username}")

  
  #debugging code, comment out when running program 4 real
  print()
  for user in db.keys():
    print(db[user][0], db[user][1])
  print()


def login(username):
  #printTitle()
  #print("")
  if username != '':
    pass
  else:
    username = input("Enter username: ")
  if username not in loginInfo.keys():
    while username not in loginInfo.keys():
      print("Username does not exist. If you wish to register an account please type 'R'.")
      username = input("Enter username or type 'R' to register: ")
      if username.lower() == 'r':
        os.system('clear')
        printTitle()
        print("Registering an account:")
        register(loginInfo)
        break
      elif username in loginInfo.keys():
        login(username)
  else:
    password = getpass.getpass(prompt="Enter password: ")
  
    if loginInfo[username] == password:
        #success case
        print(f"\nLOGGED IN: Hello {username}.\n")
        for tempUser in allAccounts:
          if tempUser.username == username:
            if tempUser.role == "Member":
              memberScreen(username)
            elif tempUser.role == "Coach":
              coachScreen(username)
            elif tempUser.role == "Treasurer":
              treasurerScreen(username)
    else:
        print(f"LOGIN FAILED: {username} is not registered or password is incorrect")

def clearAll():
  #deletes all info from database
  for key in db.keys():
    del db[key]


main()