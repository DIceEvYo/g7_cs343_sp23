"""
Group 7 James Lynch, Karla Chuprinski, 
Dev Paul, Vu Phan, William Gomez, Camelia Sama
04/30/23

"""
import pandas as pd

#Estimated that there will be about 5-6 tables that work with data.
#Table that handles log in/sign up information
#Table that handles list of tenants
#Expense record Table
#Rental Income Record Table
#Rental Payment Table (possibility that it could be combined with Rental Income Record Table)
#Annual Summary (derives data from Rental Income Record and Expense Record)




# Series = Column
class Database:  
  def __init__(self, dataFilename):
    self.dataFileName = dataFilename
    Tenant = {'lastName' : [
              "last1", "last2", "last3", "last4", "last5"
            ], 
            'firstName' : [
              "first1", "first2", "first3", "first4", "first5"
            ], 
            'unitNumber': [
              1, 2, 3, 4, 5
            ], 
            'phoneNumber': [
              889, 800, 999, 222, 200
            ], 
            'email': [
              "email@email.com", "email@email.com", "email@email.com", "email@email.com", "email@email.com"
            ],
            'tenantID' : [
              1, 2, 3, 4, 5
            ]
           }  
  
    Unit = {'unitNumber' : [
                1
             ], 
             'unitPrice': [
               2
             ], 
             'tenantID' : [
               2
             ]
           }

    #Reads elements from the file tenants.txt. Elements separated by "," Next line is a new tenant.
    self.tenants = pd.read_csv(self.dataFileName, sep=',', names=["Last Name", "First Name", "Unit Number", "Phone", "Email"])

    month = {'Month':["January","Feburary","March","April","May","June","July","August","September","October","November","December"]}
    self.months = pd.DataFrame(month)

    #self.tenants = pd.DataFrame(Tenant)
    #self.df_unit = pd.DataFrame(Unit)

    #Rental Income Record:: Incoming Rental Payments
    #12 months (cols) Apartment # (rows)
    #Each time John receives payment he records in the appropriate row and columns

    #Expense Record:: Outgoing Rental Payments
    #Date, Payee (to whom John writes the check to), Amount Paid, Budget Category [mortgage, repair, utilities, tax, insurance, addBC()]
    #self.ExpenseRecord = pd.DataFrame({'date':[],'payee':[],'paid':[], 'budget_category':["mortgage","repair","utilities","tax","insurance"]})

  def getTenantList(self):
    return self.Data.loc([[]])
    
  def getTenant(self, tenantID):
    return self.Data.loc[tenantID-1]  
  
  def addTenant(self, tenantID): 
    pass

  def printDataBase(self):
    print(self.tenants.to_string())
    print(self.months.to_string())


  



  