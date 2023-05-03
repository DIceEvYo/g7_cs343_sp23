from tkinter import *
from tkinter import ttk
import database3
import Homepage

def rentalIncomeRecord():
    """
    Allows user to view the expense record.
    """

    """Database Initialization"""
    database3.dropTableRentalIncome()
    database3.createTableRentalIncome()
    database3.readRentalIncomeFile()
    database3.dropTableTenantList()
    database3.createTableTenantList()
    database3.readTenantListFile()
    """
    Combines The Rental Income Table with the Tenant Table
    From Rental Income: Month, Payment
    From Tenants: First Name, Last Name, Apartment Number
    """
    database3.recordPerformQuery("""
    SELECT rental_income.rowid, rental_income.month, rental_income.payment, 
    tenant_list.first_name, 
    tenant_list.last_name, tenant_list.apartment_number
    FROM rental_income, tenant_list
    WHERE rental_income.tenant_id = tenant_list.rowid
    """, "comboRITenants.txt")

    """Window Initialization"""
    #Create the main window
    rentalIRWindow = Tk()
    rentalIRWindow.geometry('640x360')
    rentalIRWindow.title('Rental Income Record')
    rentalIRWindow['bg'] = 'white'
    rentalIRWindow.config(bg='white')
    font = ("Arial", 8)
    title_font = ("Arial bold", 12)

    """Window Commands"""
    def homePage():
        # Return user to the login page.
        rentalIRWindow.destroy()
        Homepage.homepage()

    """Window Contents"""
    #Read rental income information from the file rental_income.txt
    with open('comboRITenants.txt', 'r') as file:
        rental_income = [line.strip().split(',') for line in file]
    file.close()

    #Create a widget Frame to display the rental income record
    frame = Frame(rentalIRWindow, bd=2, relief=SOLID, bg='white')
    frame.pack(expand=True, fill=BOTH, padx=20, pady=20)

    #Add a label to display the title of the page
    Label(frame,
          text="Rental Income Record",
          font=title_font,
          padx=20,
          pady=20,
          bg='white').pack(expand=True, fill=BOTH)

    #Create a widget Treeview to display rental income information in a table
    tree = ttk.Treeview(frame,
                        columns=('Apartment', 'Tenant', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
                                 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'),
                        show='headings')

    #Add column headers
    tree.heading('Apartment', text='Apartment Number')
    tree.heading('Tenant', text='Tenant Name')
    tree.heading('Jan', text='January')
    tree.heading('Feb', text='February')
    tree.heading('Mar', text='March')
    tree.heading('Apr', text='April')
    tree.heading('May', text='May')
    tree.heading('Jun', text='June')
    tree.heading('Jul', text='July')
    tree.heading('Aug', text='August')
    tree.heading('Sep', text='September')
    tree.heading('Oct', text='October')
    tree.heading('Nov', text='November')
    tree.heading('Dec', text='December')

    #Set column widths
    tree.column('Apartment', width=100)
    tree.column('Tenant', width=100)
    tree.column('Jan', width=50)
    tree.column('Feb', width=50)
    tree.column('Mar', width=50)
    tree.column('Apr', width=50)
    tree.column('May', width=50)
    tree.column('Jun', width=50)
    tree.column('Jul', width=50)
    tree.column('Aug', width=50)
    tree.column('Sep', width=50)
    tree.column('Oct', width=50)
    tree.column('Nov', width=50)
    tree.column('Dec', width=50)

    #Add each rental income record to the table
    for record in rental_income:
        month = record[1]
        income = record[2]
        tenantName = record[3] + " " + record[4]
        apt_num = record[5]
        #Find the row for the current apartment number
        row = None
        for child in tree.get_children():
            if tree.item(child, 'values')[0] == apt_num:
                #print(tree.item(child, 'values'))
                row = child
                break
        #If the row does not exist, create it
        if not row:
            row = tree.insert('',
                              'end',
                              values=(apt_num, tenantName, '', '', '', '', '', '', '', '', '',
                                      '', '', ''))
        #Update the corresponding month column with the rental income
        month = month.replace(" ", "")
        if (month.upper() == "JAN"):
            tree.set(row, 'Jan', income)
        elif month.upper() == 'FEB':
          tree.set(row, 'Feb', income)
        elif month.upper() == 'MAR':
          tree.set(row, 'Mar', income)
        elif month.upper() == 'APR':
          tree.set(row, 'Apr', income)
        elif month.upper() == 'MAY':
          tree.set(row, 'May', income)
        elif month.upper() == 'JUN':
          tree.set(row, 'Jun', income)
        elif month.upper() == 'JUL':
          tree.set(row, 'Jul', income)
        elif month.upper() == 'AUG':
          tree.set(row, 'Aug', income)
        elif month.upper() == 'SEP':
          tree.set(row, 'Sep', income)
        elif month.upper() == 'OCT':
          tree.set(row, 'Oct', income)
        elif month.upper() == 'NOV':
          tree.set(row, 'Nov', income)
        elif month.upper() == 'DEC':
          tree.set(row, 'Dec', income)
            # Pack the Treeview widget
        tree.pack(expand=True, fill=BOTH)

    #Add a button to return to the homepage
    Button(rentalIRWindow, text="Homepage", font=font,
           command=homePage).pack(fill=X,
                                  expand=True,
                                  side=BOTTOM,
                                  padx=20,
                                  pady=20)
    #Start the main loop for the window
    rentalIRWindow.mainloop()

