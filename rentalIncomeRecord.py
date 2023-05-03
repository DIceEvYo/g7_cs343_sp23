from tkinter import *
from tkinter import ttk

def rentalIncomeRecord():
    # Create the main window
    newWindow = Tk()
    newWindow.geometry('640x360')
    newWindow.title('Rental Income Record')
    newWindow['bg'] = 'white'
    newWindow.config(bg='white')
    font = ("Arial", 8)
    title_font = ("Arial bold", 12)

    # Read rental income information from the file rental_income.txt
    with open('rental_income.txt', 'r') as file:
        rental_income = [line.strip().split(',') for line in file]

    # Create a widget Frame to display the rental income record
    frame = Frame(newWindow, bd=2, relief=SOLID, bg='white')
    frame.pack(expand=True, fill=BOTH, padx=20, pady=20)

    # Add a label to display the title of the page
    Label(frame,
          text="Rental Income Record",
          font=title_font,
          padx=20,
          pady=20,
          bg='white').pack(expand=True, fill=BOTH)

    # Create a widget Treeview to display rental income information in a table
    tree = ttk.Treeview(frame,
                        columns=('Apartment', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
                                 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'),
                        show='headings')

    # Add column headers
    tree.heading('Apartment', text='Apartment Number')
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

    # Set column widths
    tree.column('Apartment', width=100)
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

    # Add each rental income record to the table
    for record in rental_income:
        apt_num = record[0]
        month = record[1]
        income = record[2]

        # Find the row for the current apartment number
        row = None
        for child in tree.get_children():
            if tree.item(child, 'values')[0] == apt_num:
                row = child
                break

        # If the row does not exist, create it
        if not row:
            row = tree.insert('',
                              'end',
                              values=(apt_num, '', '', '', '', '', '', '', '', '',
                                      '', '', ''))

        # Update the corresponding month column with the rental income
        if month.upper() == 'JAN':
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

    # Add a button to close the window
    Button(frame,
           text='Close',
           command=newWindow.destroy,
           font=font).pack(pady=20)
    
    # Start the main loop for the window
    newWindow.mainloop()

