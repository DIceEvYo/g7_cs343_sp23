from addNewTenant import *
import expenseRecordTable
import tenantList
import addNewTenant
import addNewExpense
import addNewIncome
import annualSummary
import rentalIncomeRecord
import PIL
from PIL import Image, ImageTk

def homepage():
    """
    Once the correct credentials are entered, the user has access to various functionalities.
    """

    """Window Initialization"""
    homePageWindow = Tk()
    homePageWindow.geometry('640x360')
    homePageWindow.title('Homepage')
    homePageWindow['bg'] = 'white'
    homePageWindow.config(bg='white')
    font = ("Arial", 12)

    """Window Commands"""
    def expenseButtonClicked():
        homePageWindow.destroy()
        expenseRecordTable.expenseRecordTable()

    def tenantListButtonClicked():
        homePageWindow.destroy()
        tenantList.TenantList()

    def addTenantButtonClicked():
        homePageWindow.destroy()
        addNewTenant.addNewTenant()

    def rentalIncomeButtonClicked():
        homePageWindow.destroy()
        rentalIncomeRecord.rentalIncomeRecord()

    def addExpenseButtonClicked():
        homePageWindow.destroy()
        addNewExpense.addNewExpense()

    def addIncomeButtonClicked():
        homePageWindow.destroy()
        addNewIncome.addNewIncome()

    def annualSummaryButtonClicked():
        homePageWindow.destroy()
        annualSummary.annualSummary()

    """Window Contents"""
    #Add buttons for the different features
    Button(homePageWindow, text="View Expenses", font=font, command=expenseButtonClicked).grid(row=6, column=0, padx=10, pady=10)
    Button(homePageWindow, text="Tenant List", font=font, command=tenantListButtonClicked).grid(row=6, column=1, padx=10, pady=10)
    Button(homePageWindow, text="Add Tenant", font=font, command=addTenantButtonClicked).grid(row=6, column=2, padx=10, pady=10)
    Button(homePageWindow, text="Add Expenses", font=font, command=addExpenseButtonClicked).grid(row=7, column=0, padx=10, pady=10)
    Button(homePageWindow, text="Annual Summary", font=font, command=annualSummaryButtonClicked).grid(row=7, column=1, padx=10, pady=10)
    Button(homePageWindow, text="Rental Income", font=font, command=rentalIncomeButtonClicked).grid(row=7, column=2, padx=10, pady=10)
    Button(homePageWindow, text="Add Income", font=font, command=addIncomeButtonClicked).grid(row=8, column=1, padx=10, pady=10)

    #Display the best part of the program
    bestFriend = ImageTk.PhotoImage(PIL.Image.open("profile1.png").resize((80, 80)))
    profile_label = Label(homePageWindow, image=bestFriend, bg='white')
    profile_label.image = bestFriend
    profile_label.grid(row=0, column=0, padx=20, pady=20)

    Label(homePageWindow, text=f"Welcome!", font=font,
          bg='white').grid(row=0, column=1, padx=20, pady=20)

    #Start the main loop
    homePageWindow.mainloop()