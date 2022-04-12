import os
import getpass
#from replit import db

allAccounts = []
accounts = {}

class accountInfo:
  def __init__(self, username, password, role, name, phone, paid, address):
    self.username = username
    self.password = password
    self.role = role
    self.name = name
    self.phone = phone
    self.paid = paid
    self.address = address

def printTitle():
  print("RECREATION CLUB MEMBERSHIP")
  print("--------------------------")

def printSelections(selections):
  selectionNum = 0  
  for select in selections:
    selectionNum += 1
    print(str(selectionNum) + ". " + select)


def main():
    selection = ''
    selections = ["Create Account", "Login", "Quit"]
    while selection.lower() != 'q':
      printTitle()
      printSelections(selections)
        
      selection = input("Selection Number: ")
      
      if selection == '1':
        register()
      elif selection == '2':
        login()
      elif selection == '3' or selection.lower() == 'q':
        print("Quitting")
        break

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


def register():
  username = input("Enter username: ")
  while username in accounts.keys():  
    print ("Username is already taken.")
    username = input("Enter username: ")
    
  password = getpass.getpass(prompt="Enter password: ")
  while len(password) < 8:     
    print("Password has to be greater than 8 characters.")
    password = getpass.getpass(prompt="Enter password: ")

  accounts[username] = password
  
  defaultRole = "Member"
  name = input("Please enter your first and last name:\n")
  phone = input("Please enter your phone number:\n")
  paid = 0
  address = input("Please enter your address:\n")
  
  newUser = accountInfo(username, password, defaultRole, name, phone, paid, address)
  allAccounts.append(newUser)
  
  print(f"ACCOUNT CREATED: for user {username}")

  print(allAccounts)
  print(newUser)

def login():
  username = input("Enter username: ")
  password = getpass.getpass(prompt="Enter password: ")
  
  if accounts[username] == password:
      #success case
      print(f"LOGGED IN: Hello {username}.")
      for item in allAccounts:
        if item.role == "Member":
          memberScreen(username)
 #     if allAccounts.role == 'Treasurer':
 #       treasurerScreen()
  #    elif role == 'Coach':
  #      coachScreen()
  #    elif role == 'Member':
  #      memberScreen()
  else:
      print(f"LOGIN FAILED: {username} is not registered or password is incorrect")


main()