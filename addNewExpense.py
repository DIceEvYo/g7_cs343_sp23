from tkinter import *
import database3
import Homepage

def addNewExpense():
  """
  Allows user to add a new tenant to the database.
  """

  """Window Initialization"""
  #Create the window to add a new tenant
  addNewExpWindow = Tk()
  addNewExpWindow.geometry('640x360')
  addNewExpWindow.title('Add New Expense')
  addNewExpWindow.config(bg='white')
  font = ("Arial", 12)

  """Window Commands"""
  def homePage():
      # Return user to the home page.
      addNewExpWindow.destroy()
      Homepage.homepage()

  #Function to save tenant information in a file
  def saveExpense():
      amountpaid = enterPaidAmnt.get()
      thepayee = enterPayee.get()
      category = enterCat.get()
      date = enterDate.get()
      if ((amountpaid != "") and (thepayee != "") and (category != "") and (date != "")):
          """
          First check if all fields have been filled, then add to file.
          If we had more time, to improve this application, we would add more 
          security measures to prevent attacks such as buffer overflow.
          """
          # Update tenant_list.txt and the database.
          database3.addRecordExpenseRecord(date,thepayee,amountpaid,category)
          database3.writeExpenseRecord()
          # Close the window
          addNewExpWindow.destroy()
          Homepage.homepage()
          # User won't be allowed to append info without filling out all fields.
      else:
          # If insufficient data is provided, alert the user.
          errorLabel.config(text="Please enter all fields.", fg="red")

  """Window Contents"""
  #Create labels and input fields for each input field
  Label(addNewExpWindow,
        text="Amount Paid:",
        font=font,
        padx=20,
        pady=10,
        bg='white').grid(row=1, column=0)
  enterPaidAmnt = Entry(addNewExpWindow)
  enterPaidAmnt.grid(row=1, column=1)

  Label(addNewExpWindow, text="The Payee:", font=font, padx=20, pady=10,
        bg='white').grid(row=2, column=0)
  enterPayee = Entry(addNewExpWindow)
  enterPayee.grid(row=2, column=1)

  Label(addNewExpWindow, text="Category:", font=font, padx=20, pady=10,
        bg='white').grid(row=3, column=0)
  enterCat = Entry(addNewExpWindow)
  enterCat.grid(row=3, column=1)

  Label(addNewExpWindow,
        text="Date (YYYY-MM-DD):",
        font=font,
        padx=20,
        pady=10,
        bg='white').grid(row=4, column=0)
  enterDate = Entry(addNewExpWindow)
  enterDate.grid(row=4, column=1)

  # Add a button to save the expense information
  Button(addNewExpWindow, text="Submit", font=font,
         command=saveExpense).grid(row=6, column=0, columnspan=2, pady=20)

  # Add a button to return to the homepage
  Button(addNewExpWindow, text="Homepage", font=font,
         command=homePage).grid(row=10, column=0, columnspan=2, pady=20)

  errorLabel = Label(addNewExpWindow, font=font)
  errorLabel.grid(row=9, column=0, columnspan=2, pady=20)
  # Start the main loop
  addNewExpWindow.mainloop()
