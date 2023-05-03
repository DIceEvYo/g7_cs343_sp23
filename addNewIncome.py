from tkinter import *
import database3
import Homepage
import tenantList

def addNewIncome():
  """
  Allows user to add a new tenant to the database.
  """

  """Window Initialization"""
  #Create the window to add a new tenant
  addNewIncWindow = Tk()
  addNewIncWindow.geometry('640x360')
  addNewIncWindow.title('Add New Income')
  addNewIncWindow.config(bg='white')
  font = ("Arial", 12)

  """Window Commands"""
  def homePage():
      # Return user to the home page.
      addNewIncWindow.destroy()
      Homepage.homepage()

  def goToTenants():
      #In case the user needs a reference, this button is here for them to check the list of tenants
      addNewIncWindow.destroy()
      tenantList.TenantList()

  #Function to save tenant information in a file
  def saveExpense():
      month = enterMonth.get()
      pay = enterPay.get()
      tid = enterTID.get()

      if ((month != "") and (pay != "") and (tid != "")):
          """
          First check if all fields have been filled, then add to file.
          If we had more time, to improve this application, we would add more 
          security measures to prevent attacks such as buffer overflow.
          """
          try:
              tid = int(tid)
              if(not(tid<0 or tid > tidMax)):
                  if(month =="01" or month=="02" or month=="03" or month=="04" or month=="05"
                          or month=="06" or month=="07" or month=="08" or month=="09" or month=="10" or month=="11" or month=="12"):
                      # Update tenant_list.txt and the database.
                      database3.addRecordRentalIncome(month, pay, tid)
                      database3.writeRentalIncome()
                      # Close the window
                      addNewIncWindow.destroy()
                      Homepage.homepage()
                  else:
                      errorLabel.config(text="Please Enter a Valid Month (01-12)", fg="red")
              else:
                  errorLabel.config(text="Please Enter a Valid Number", fg="red")
          except:
              errorLabel.config(text="Please Enter a Number", fg="red")
          # User won't be allowed to append info without filling out all fields.
      else:
          # If insufficient data is provided, alert the user.
          errorLabel.config(text="Please enter all fields.", fg="red")

  """Window Contents"""
  #Create labels and input fields for each input field
  Label(addNewIncWindow,
        text="Month: (01-12)",
        font=font,
        padx=20,
        pady=10,
        bg='white').grid(row=1, column=0)
  enterMonth = Entry(addNewIncWindow)
  enterMonth.grid(row=1, column=1)

  Label(addNewIncWindow, text="Payment", font=font, padx=20, pady=10,
        bg='white').grid(row=2, column=0)
  enterPay = Entry(addNewIncWindow)
  enterPay.grid(row=2, column=1)

  tidMax = int((database3.performQuery("""SELECT COUNT(tenant_list.rowid) FROM tenant_list""")[0][0]))
  msg = "Please enter a TenantID from 1 to " + str(tidMax) + "."
  Label(addNewIncWindow, text=msg, font=font, padx=20, pady=10,
        bg='white').grid(row=3, column=0)
  enterTID = Entry(addNewIncWindow)
  enterTID.grid(row=3, column=1)

  # Add a button to save the expense information
  Button(addNewIncWindow, text="Submit", font=font,
         command=saveExpense).grid(row=6, column=0, columnspan=2, pady=20)

  # Add a button to return to the homepage
  Button(addNewIncWindow, text="Homepage", font=font,
         command=homePage).grid(row=10, column=0, columnspan=2, pady=20)

  # Add a button to check tenant List
  Button(addNewIncWindow, text="Tenant List", font=font,
         command=goToTenants).grid(row=10, column=0, columnspan=2, pady=20)

  errorLabel = Label(addNewIncWindow, font=font)
  errorLabel.grid(row=9, column=0, columnspan=2, pady=20)
  # Start the main loop
  addNewIncWindow.mainloop()
