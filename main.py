import os
import getpass
from replit import db

allAccounts = []
loginInfo = {}

class accountInfo:
  def __init__(self, username, password, role, name, phone, paid, address):
    self.username = username
    self.password = password
    self.role = role
    self.name = name
    self.phone = phone
    self.paid = paid          # number of unpaid sessions
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
      db["admin"] = ["admin", "password", "Coach", "Coach123", "6490001234", 0, "123 Address St."]
  
    for user in db.keys():
      #db[user][0]
      #tempUser = accountInfo(username, password, defaultRole, name, phone, paid, address)
      tempUser = accountInfo(db[user][0], db[user][1], db[user][2], db[user][3], db[user][4], db[user][5], db[user][6])
      allAccounts.append(tempUser)
      #loginInfo[username] = password
      loginInfo[db[user][0]] = db[user][1]

      
    selection = ''
    selections = ["Create Account", "Login", "Quit"]
    while selection.lower() != 'q':
      printTitle()
      printSelections(selections)
        
      selection = input("Selection Number: ")
      
      if selection == '1':
        register(loginInfo)
      elif selection == '2':
        login()
      elif selection == '3' or selection.lower() == 'q':
        print("Quitting")
        break
      else:
        print("Invalid selection.")

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

def coachScreen(user):
  selections = ["Schedules", "View Members List", "Send Reminders", "Logout"]
  selection = ''
  while selection.lower() != 'q':
    printTitle()
    print("LOGGED IN AS: COACH")
    printSelections(selections)

    selection = input ("Selection Number: ")

    if selection == '1':
      listSchedule()
    elif selection == '2':
      print("Listing All Members:\n")
      ##############################################
      ###############tabulate this later############
      ##############################################
      #Format: Name, Phone number, number of classes unpaid
      numMembers = 0
      memberList = []
      for username in db.keys():
        if db[username][2] == "Member":
          numMembers += 1
          memberList.append(username)
          #print Member's name, phone number and unpaid classes
        #next 3 lines of code are for debugging
          print(str(numMembers) + ".", db[username][3], db[username][4], db[username][5])
        else:
          print("somethingsomething",db[username][3], db[username][4], db[username][5])
      userNum = int(input("\nModify Member number: "))

      #(name, phone, paid, address)
      username = memberList[userNum]
      printSelections([db[username][3], db[username][4], db[username][5], db[username][6]])

      descNum = input("\nWhich description do you wish to modify?\nEnter the description number: ")

      if descNum == '1':
        db[username][3] = input("Please enter the member's First and Last name: \n")
      elif descNum == '2':
        db[username][4] = input("Please enter the member's phone number: \n")
      elif descNum == '3':
        db[username][5] = input("Please enter the member's number of unpaid classes: \n")
      elif descNum == '4':
        db[username][6] = input("Please enter the member's address: \n")

        

        
def makePayment(user):
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
  username = input("Enter username: ")
  while username in loginInfo.keys():  
    print ("Username is already taken.")
    username = input("Enter username: ")
    
  password = getpass.getpass(prompt="Enter password: ")
  while len(password) < 8:     
    print("Password has to be greater than 8 characters.")
    password = getpass.getpass(prompt="Enter password: ")
  
  defaultRole = "Member"
  name = input("Please enter your first and last name:\n")
  phone = input("Please enter your phone number:\n")
  paid = 0
  address = input("Please enter your address:\n")
  
  newUser = accountInfo(username, password, defaultRole, name, phone, paid, address)
  
  db[username] = [username, password, defaultRole, name, phone, paid, address]
  #print(db[username])

  allAccounts.append(newUser)
  loginInfo[username] = password

  #debugging code, comment out when running program 4 real
  for user in db.keys():
    print(db[user][0], db[user][1])
  
  
  print(f"ACCOUNT CREATED: for user {username}")


def login():
  username = input("Enter username: ")
  password = getpass.getpass(prompt="Enter password: ")
  
  if loginInfo[username] == password:
      #success case
      print(f"LOGGED IN: Hello {username}.")
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