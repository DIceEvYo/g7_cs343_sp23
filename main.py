from database import Database
from tkinter import *

"""
Total of 11 Required (chance that there might be more) Pages::
1. Log In
2. Sign Up
3. Tenant List
4. Add New Tenant
5. Add New Expense
6. Expense Record Table
7. Expenses UI
8. Rental Income Record
9. Annual Summary
10. Rental Payment
11. Edit Profile
"""


# newWindow = Tk()
# newWindow.title("Landlord")
# newWindow.geometry('640x360')
# #Log In Screen
# LogNlbl = Label(newWindow, text="Welcome back Landlord!",
#                 font=("Arial", 25)).pack()
# button = Button(newWindow).place(relx = 0.5, rely = 0.5)

# newWindow.mainloop()

#https://www.geeksforgeeks.org/create-first-gui-application-using-python-tkinter/#
#https://www.geeksforgeeks.org/how-to-change-the-tkinter-label-font-size/
#https://docs.google.com/document/d/14x8v2uO6NDCCJBbFalxzG08It_grOTvClJ_zzuFdYtY/edit

"""
Group 7 James Lynch, Karla Chuprinski, 
Dev Paul, Vu Phan, William Gomez, Camelia Sama
04/30/23
"""
TheDatabase = Database('tenants.txt')

#print(TheDatabase)
#for dataEntry in TheDatabase:
#  print(dataEntry)
#print(TheDatabase.getTenantList())
TheDatabase.printDataBase()

def main():
  print("Welcome! Please login!")
  getTenantList = true
  if (getTenantList):
    TheDatabase.getTenantList()
    
  for i in range(total_rows):
            for j in range(total_columns):
                 
                e = Entry(newWindow, width=20, fg='blue',
                               font=('Arial',16,'bold'))
                 
                e.grid(row=i, column=j)
                e.insert(END, lst[i][j])
              
  newWindow.mainLoop()
class LandlordApplication:

  def readTenants(self):
    #Reads information from tenants file
    #Organized by lastName, firstName, unitNumber, phoneNumber, email
    tenantFile = open("tenants.txt", "r")
    tenants = []
    index = 0
    for tenant in tenantFile:
      tenants.append([])
      for data in tenant.split(","):
        tenants[index].append(data.replace("\n", ""))
      index += 1
    print(tenants)
    tenantFile.close()

  """
    self.lastName = lastName
      self.firstName = firstName
      self.unitNumber = unitNumber
      self.phoneNumber = phoneNumber
      self.email = email
    """

  def createTenant(self):  #Writes to file
    dataString = ""
    data = input("Please enter tenant last name: ")
    dataString = dataString + data + ","
    data = input("Please enter tenant first name: ")
    dataString = dataString + data + ","
    data = input("Please enter unit number: ")
    dataString = dataString + data + ","
    data = input("Please enter phone number: ")
    dataString = dataString + data + ","
    data = input("Please enter email: ")
    dataString = dataString + data + "\n"
    
    newTenantFile = open("tenants.txt", "a")
    newTenantFile.write(dataString)
    newTenantFile.close()

  def createAccount():
    print("Create Account ")
    landlordFirstName = input("Enter first name: ")
    landlordLastName = input("Enter last name: ")
    landlordEmail = input("Enter email: ")
    user = input("Enter a username: ")
    password = input("Enter a password: ")

    accountInfo = {
      'firstName': landlordFirstName,
      'lastName': landlordLastName,
      'email': landlordEmail,
      'user': user,
      'password': password
    }
    # Store user and password in a database or file
    with open('landlordAccount.txt', 'a') as file:
      file.write(str(accountInfo))
    return landlordFirstName, landlordLastName, landlordEmail, user, password

  def login(user, password):
    with open('landlordAccount.txt', 'r') as file:
      for line in file:
        pass


program = LandlordApplication()

program.createTenant()
program.createTenant()

program.readTenants()

print(TheDatabase.getTenant(1))
