from tkinter import *
import Homepage
import database3
import PIL
from PIL import Image, ImageTk

def addNewTenant():
  """
  Allows user to add a new tenant to the database.
  """

  """Window Initialization"""
  #Create window to add a new tenant
  addTenantWindow = Tk()
  addTenantWindow.geometry('640x360')
  addTenantWindow.title('Add New Tenant')
  addTenantWindow['bg'] = 'white'
  addTenantWindow.config(bg='white')
  font = ("Arial", 7)

  """Window Commands"""
  def homePage():
      # Return user to the home page.
      addTenantWindow.destroy()
      Homepage.homepage()

  def appendTenant():
      #Function to save tenant information to a file
      lastname = enterLast.get()
      firstname = enterFirst.get()
      unit = enterUnit.get()
      phone = enterPhone.get()
      email = enterEmail.get()
      if ((lastname != "") and (firstname != "") and (unit != "") and (phone != "") and (email != "")):
          """
          First check if all fields have been filled, then add to file.
          If we had more time, to improve this application, we would add more 
          security measures to prevent attacks such as buffer overflow.
          """
          #Update tenant_list.txt and the database.
          database3.addRecordTenantList(firstname,lastname,unit,phone,email)
          database3.writeTenantList()
          # Close the window
          addTenantWindow.destroy()
          Homepage.homepage()
          #User won't be allowed to append info without filling out all fields.
      else:
          # If insufficient data is provided, alert the user.
          errorLabel.config(text="Please enter all fields.", fg="red")

  """Window Contents"""
  #Create labels and entry fields for each input field
  Label(addTenantWindow, text="Last Name:", font=font, padx=20, pady=10, bg='white').grid(row=0, column=0)
  enterLast = Entry(addTenantWindow)
  enterLast.grid(row=0, column=1)

  Label(addTenantWindow, text="First Name:", font=font, padx=20, pady=10, bg='white').grid(row=0, column=2)
  enterFirst = Entry(addTenantWindow)
  enterFirst.grid(row=0, column=3)

  Label(addTenantWindow, text="Unit Number:", font=font, padx=20, pady=10, bg='white').grid(row=1, column=0)
  enterUnit = Entry(addTenantWindow)
  enterUnit.grid(row=1, column=1)

  Label(addTenantWindow, text="Phone:", font=font, padx=20, pady=10, bg='white').grid(row=1, column=2)
  enterPhone = Entry(addTenantWindow)
  enterPhone.grid(row=1, column=3)

  Label(addTenantWindow, text="Email", font=font, padx=20, pady=10, bg='white').grid(row=2, column=0)
  enterEmail = Entry(addTenantWindow)
  enterEmail.grid(row=2, column=1)

  #Add a button to save the tenant information
  Button(addTenantWindow, text="Submit", font=font,
         command=appendTenant).grid(row=3, column=1, columnspan=2, pady=20)

  # Add a button to return to the homepage
  Button(addTenantWindow, text="Homepage", font=font,
         command=homePage).grid(row=10, column=0, columnspan=2, pady=20)
  #Start the main loop
  errorLabel = Label(addTenantWindow, font=font)
  errorLabel.grid(row=9, column=0, columnspan=2, pady=20)

  # Display the best part of the program
  bestFriend = ImageTk.PhotoImage(PIL.Image.open("profile.png").resize((80, 80)))
  profile_label = Label(addTenantWindow, image=bestFriend, bg='white')
  profile_label.image = bestFriend
  profile_label.grid(row=3, column=0, padx=20, pady=20)

  addTenantWindow.mainloop()
