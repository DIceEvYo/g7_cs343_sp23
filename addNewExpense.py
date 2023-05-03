from tkinter import *
from datetime import datetime


def addNewExpense():
  #Create the window to add a new tenant
  newWindow = Tk()
  newWindow.geometry('640x360')
  newWindow.title('Add New Expense')
  newWindow.config(bg='white')
  font = ("Arial", 12)
  title_font = ("Arial bold", 18)

  #Disable automatic window size adjustment
  newWindow.grid_propagate(False)

  #Set a minimum size for the window
  newWindow.wm_minsize(640, 360)

  #Function to save tenant information in a file
  def saveExpense():
    expensetittle = e1.get()
    amountpaid = e2.get()
    thepayee = e3.get()
    category = e4.get()
    date = e5.get()
    paidby = e6.get()

    #Format the date of entry
    date = datetime.strptime(date, "%m/%d/%Y").strftime("%Y-%m-%d")
    #Add tenant information to the tenant.txt file
    with open('expense_record.txt', 'a') as file:
      file.write(
        f"{expensetittle},{amountpaid},{thepayee},{category},{date},{paidby}\n"
      )
    #Close the window
    newWindow.destroy()

  #Create labels and input fields for each input field
  Label(newWindow,
        text="Expense Tittle:",
        font=font,
        padx=20,
        pady=10,
        bg='white').grid(row=0, column=0)
  e1 = Entry(newWindow)
  e1.grid(row=0, column=1)

  Label(newWindow,
        text="Amount Paid:",
        font=font,
        padx=20,
        pady=10,
        bg='white').grid(row=1, column=0)
  e2 = Entry(newWindow)
  e2.grid(row=1, column=1)

  Label(newWindow, text="The Payee:", font=font, padx=20, pady=10,
        bg='white').grid(row=2, column=0)
  e3 = Entry(newWindow)
  e3.grid(row=2, column=1)

  Label(newWindow, text="Category:", font=font, padx=20, pady=10,
        bg='white').grid(row=3, column=0)
  e4 = Entry(newWindow)
  e4.grid(row=3, column=1)

  Label(newWindow,
        text="Date (MM/DD/YYYY):",
        font=font,
        padx=20,
        pady=10,
        bg='white').grid(row=4, column=0)
  e5 = Entry(newWindow)
  e5.grid(row=4, column=1)

  Label(newWindow, text="Paid By:", font=font, padx=20, pady=10,
        bg='white').grid(row=5, column=0)
  e6 = Entry(newWindow)
  e6.grid(row=5, column=1)

  # Ajouter un bouton pour enregistrer les informations du locataire
  Button(newWindow, text="Submit", font=font,
         command=saveExpense).grid(row=6, column=0, columnspan=2, pady=20)

  # Lancer la boucle principale
  newWindow.mainloop()
