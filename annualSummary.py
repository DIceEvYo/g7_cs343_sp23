from tkinter import *
from tkinter import ttk


def annualSummary():
  # Create the main window
  newWindow = Tk()
  newWindow.geometry('640x360')
  newWindow.title('Annual Summary')
  newWindow['bg'] = 'white'
  newWindow.config(bg='white')
  font = ("Arial", 8)
  title_font = ("Arial bold", 18)

  # Read the annual summary from the file
  with open('annualreport.txt', 'r') as file:
    lines = file.readlines()
    rental_sum = float(lines[0].strip())
    categories = [line.strip().split(',') for line in lines[1:6]]
    expense_sum = float(lines[6].strip())
    amount_gained = float(lines[7].strip())

  # Create a widget Frame to display the annual summary
  frame = Frame(newWindow, bd=2, relief=SOLID, bg='white')
  frame.pack(expand=True, fill=BOTH, padx=20, pady=20)

  # Add a label for the title of the page
  Label(frame,
        text="Annual Summary",
        font=title_font,
        padx=20,
        pady=20,
        bg='white').pack(expand=True, fill=BOTH)

  # Add a label for rental sum
  Label(frame,
        text=f"Rental sum: ${rental_sum:.2f}",
        font=font,
        padx=20,
        pady=5,
        bg='white').pack(fill=X)
  # Add labels for expense sum and amount gained
  Label(frame,
        text=f"Expense Sum: ${expense_sum:.2f}",
        font=font,
        padx=20,
        pady=5,
        bg='white').pack(fill=X)
  Label(frame,
        text=f"Amount Gained: ${amount_gained:.2f}",
        font=font,
        padx=20,
        pady=5,
        bg='white').pack(fill=X)

  # Create a widget Treeview to display the annual summary in a table
  tree = ttk.Treeview(frame, columns=('category', 'amount'), show='headings')

  # Add column headers
  tree.heading('category', text='Budget Category')
  tree.heading('amount', text='Amount Paid')

  # Add each category and the corresponding amount spent to the table
  for category, amount in categories:
    tree.insert('', 'end', values=(category, f'${float(amount):.2f}'))

  # Display the annual summary in the window with a scrollbar
  scrollbar = ttk.Scrollbar(frame, orient='vertical', command=tree.yview)
  tree.configure(yscroll=scrollbar.set)
  tree.pack(side=LEFT, fill=BOTH, padx=20, pady=20, expand=True)
  scrollbar.pack(side=RIGHT, fill=Y)

  # Add a button to go back to the homepage
  Button(newWindow, text="Homepage", font=font,
         command=newWindow.destroy).pack(fill=X,
                                         expand=True,
                                         side=BOTTOM,
                                         padx=20,
                                         pady=20)

  # Start the main loop
  newWindow.mainloop()
