from tkinter import *
from tkinter import ttk
import database3
import Homepage

def rentalIncomeRecord():
    """
    Allows user to view the rental income record
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

    def orgByName():
        #Orders by name, ASC
        database3.recordPerformQuery("""
            SELECT rental_income.rowid, rental_income.month, rental_income.payment, 
            tenant_list.first_name, 
            tenant_list.last_name, tenant_list.apartment_number
            FROM rental_income, tenant_list
            WHERE rental_income.tenant_id = tenant_list.rowid
            ORDER BY tenant_list.first_name, tenant_list.last_name
            """, "tempQuery.txt")
        updateDisplay()

    def orgByApartment():
        #Orders by name, ASC
        database3.recordPerformQuery("""
            SELECT rental_income.rowid, rental_income.month, rental_income.payment, 
            tenant_list.first_name, 
            tenant_list.last_name, tenant_list.apartment_number
            FROM rental_income, tenant_list
            WHERE rental_income.tenant_id = tenant_list.rowid
            ORDER BY tenant_list.apartment_number
            """, "tempQuery.txt")
        updateDisplay()

    def orgByMonth():
        #Orders by name, ASC
        database3.recordPerformQuery("""
            SELECT rental_income.rowid, rental_income.month, rental_income.payment, 
            tenant_list.first_name, 
            tenant_list.last_name, tenant_list.apartment_number
            FROM rental_income, tenant_list
            WHERE rental_income.tenant_id = tenant_list.rowid
            ORDER BY rental_income.month
            """, "tempQuery.txt")
        updateDisplay()

    def updateDisplay():
        with open('tempQuery.txt', 'r') as f:
            newRental_income = [line.strip().split(',') for line in f]
            f.close()
        for val in tree.get_children():
            tree.delete(val)
        # Add each rental income record to the table
        for record in newRental_income:
            newMonth = record[1]
            newIncome = record[2]
            newTenantName = record[3] + " " + record[4]
            new_apt_num = record[5]
            # Find the row for the current apartment number
            newRow = None
            for newChild in tree.get_children():
                if tree.item(newChild, 'values')[0] == new_apt_num:
                    # print(tree.item(newChild, 'values'))
                    newRow = newChild
                    break
            # If the row does not exist, create it
            if not newRow:
                newRow = tree.insert('',
                                    'end',
                                    values=(new_apt_num, newTenantName, '', '', '', '', '', '', '', '', '',
                                            '', '', ''))
            # Update the corresponding newMonth column with the rental income
            newMonth = newMonth.replace(" ", "")
            if (newMonth.upper() == "01"):
                tree.set(newRow, 'Jan', newIncome)
            elif newMonth.upper() == '02':
                tree.set(newRow, 'Feb', newIncome)
            elif newMonth.upper() == '03':
                tree.set(newRow, 'Mar', newIncome)
            elif newMonth.upper() == '04':
                tree.set(newRow, 'Apr', newIncome)
            elif newMonth.upper() == '05':
                tree.set(newRow, 'May', newIncome)
            elif newMonth.upper() == '06':
                tree.set(newRow, 'Jun', newIncome)
            elif newMonth.upper() == '07':
                tree.set(newRow, 'Jul', newIncome)
            elif newMonth.upper() == '08':
                tree.set(newRow, 'Aug', newIncome)
            elif newMonth.upper() == '09':
                tree.set(newRow, 'Sep', newIncome)
            elif newMonth.upper() == '10':
                tree.set(newRow, 'Oct', newIncome)
            elif newMonth.upper() == '11':
                tree.set(newRow, 'Nov', newIncome)
            elif newMonth.upper() == '12':
                tree.set(newRow, 'Dec', newIncome)
                # Pack the Treeview widget
            tree.pack(expand=True, fill=BOTH)

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
    tree.heading('Apartment', text='Apartment Number', command=orgByApartment)
    tree.heading('Tenant', text='Tenant Name', command=orgByName)
    tree.heading('Jan', text='January', command=orgByMonth)
    tree.heading('Feb', text='February', command=orgByMonth)
    tree.heading('Mar', text='March', command=orgByMonth)
    tree.heading('Apr', text='April', command=orgByMonth)
    tree.heading('May', text='May', command=orgByMonth)
    tree.heading('Jun', text='June', command=orgByMonth)
    tree.heading('Jul', text='July', command=orgByMonth)
    tree.heading('Aug', text='August', command=orgByMonth)
    tree.heading('Sep', text='September', command=orgByMonth)
    tree.heading('Oct', text='October', command=orgByMonth)
    tree.heading('Nov', text='November', command=orgByMonth)
    tree.heading('Dec', text='December', command=orgByMonth)

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
        if (month.upper() == "01"):
            tree.set(row, 'Jan', income)
        elif month.upper() == '02':
          tree.set(row, 'Feb', income)
        elif month.upper() == '03':
          tree.set(row, 'Mar', income)
        elif month.upper() == '04':
          tree.set(row, 'Apr', income)
        elif month.upper() == '05':
          tree.set(row, 'May', income)
        elif month.upper() == '06':
          tree.set(row, 'Jun', income)
        elif month.upper() == '07':
          tree.set(row, 'Jul', income)
        elif month.upper() == '08':
          tree.set(row, 'Aug', income)
        elif month.upper() == '09':
          tree.set(row, 'Sep', income)
        elif month.upper() == '10':
          tree.set(row, 'Oct', income)
        elif month.upper() == '11':
          tree.set(row, 'Nov', income)
        elif month.upper() == '12':
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

