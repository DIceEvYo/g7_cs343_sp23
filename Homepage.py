from addNewTenant import *
import expenseRecordTable
import tenantList
import addNewTenant
from annualSummary import *

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

    #TODO
    def addExpenseButtonClicked():
        homePageWindow.destroy()
        addNewExpense()

    def annualSummaryButtonClicked():
        homePageWindow.destroy()
        annualSummary()

    """Window Contents"""
    #Add buttons for the different features
    Button(homePageWindow, text="View Expenses", font=font, command=expenseButtonClicked).grid(row=6, column=0, padx=10, pady=10)
    Button(homePageWindow, text="Tenant List", font=font, command=tenantListButtonClicked).grid(row=6, column=1, padx=10, pady=10)
    Button(homePageWindow, text="Add Tenant", font=font, command=addTenantButtonClicked).grid(row=6, column=2, padx=10, pady=10)
    Button(homePageWindow, text="Add Expenses", font=font, command=addExpenseButtonClicked).grid(row=7, column=0, padx=10, pady=10)
    Button(homePageWindow, text="Annual Summary", font=font, command=annualSummaryButtonClicked).grid(row=7, column=1, padx=10, pady=10)

    #Start the main loop
    homePageWindow.mainloop()