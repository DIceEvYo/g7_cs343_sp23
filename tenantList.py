from tkinter import *
from tkinter import ttk
import Homepage
import database3


def TenantList():
    """
    Displays the name, email, and phone from the list of tenants.
    """

    """Database Initialization"""
    database3.dropTableTenantList()
    database3.createTableTenantList()
    database3.readTenantListFile()

    """Window Initialization"""
    tenantListWindow = Tk()
    tenantListWindow.geometry('640x360')
    tenantListWindow.title('Tenant List')
    tenantListWindow['bg'] = 'white'
    tenantListWindow.config(bg='white')
    font = ("Arial", 12)
    title_font = ("Arial bold", 18)
    
    treeColumns = ('name', 'unit', 'phone', 'email')
    #Create a Frame widget to display the list of tenants
    frame = Frame(tenantListWindow, bd=2, relief=SOLID, bg='white')
    frame.pack(expand=True, fill=BOTH, padx=20, pady=20)
    tree = ttk.Treeview(frame, columns=treeColumns, show='headings')

    """Window Commands"""
    def homePage():
        #Return user to the login page.
        tenantListWindow.destroy()
        Homepage.homepage()

    def filterByName():
        #Organizes Tenant_List by Name, ASC
        database3.recordPerformQuery("""SELECT tenant_list.first_name, tenant_list.last_name, 
        tenant_list.apartment_number, tenant_list.phone_number, tenant_list.email
                    FROM tenant_list  
                    ORDER BY tenant_list.first_name, tenant_list.last_name""", "tempQuery.txt")
        updateDisplay()

    def filterByUnit():
        #Organizes Tenant_List by Unit, ASC
        database3.recordPerformQuery("""SELECT tenant_list.first_name, tenant_list.last_name, 
                tenant_list.apartment_number, tenant_list.phone_number, tenant_list.email 
                            FROM tenant_list 
                            ORDER BY tenant_list.apartment_number""", "tempQuery.txt")
        updateDisplay()

    def filterByPhone():
        #Organizes Tenant_List by Phone, ASC
        database3.recordPerformQuery("""SELECT tenant_list.first_name, tenant_list.last_name, 
                tenant_list.apartment_number, tenant_list.phone_number, tenant_list.email  
                            FROM tenant_list
                            ORDER BY tenant_list.phone_number""", "tempQuery.txt")
        updateDisplay()

    def filterByMail():
        #Organizes Tenant_List by Email, ASC
        database3.recordPerformQuery("""SELECT tenant_list.first_name, tenant_list.last_name, 
                tenant_list.apartment_number, tenant_list.phone_number, tenant_list.email  
                            FROM tenant_list
                            ORDER BY tenant_list.email""", "tempQuery.txt")
        updateDisplay()
  
    def readTenantsToTable():
        for tenant in tenants:
            name = tenant[1] + ' ' + tenant[2]
            unit = tenant[3]
            phone = tenant[4]
            email = tenant[5]
            tree.insert('', 'end', values=(name, unit, phone, email))

    def updateDisplay():
        #Uses the tempquery from one of the org functions and updates the tree to display the new order.
        with open('tempQuery.txt', 'r') as tempFile:
            newTenants = [line.strip().split(',') for line in tempFile]
        tempFile.close()
        for val in tree.get_children():
            tree.delete(val)
        for newTenant in newTenants:
            name = newTenant[0] + " " + newTenant[1]
            unit = newTenant[2]
            phone = newTenant[3]
            email = newTenant[4]
            tree.insert('', 'end', values=(name, unit, phone, email))

    """Window Contents"""
    #Read tenant information from the tenant.txt file
    with open('tenant_list.txt', 'r') as file:
      tenants = [line.strip().split(',') for line in file]
    file.close()

    Label(frame,
          text="Tenant List",
          font=title_font,
          padx=20,
          pady=20,
          bg='white').pack(expand=True, fill=BOTH)

    tree.heading('name', text='Name', command=filterByName)
    tree.heading('unit', text='Unit', command=filterByUnit)
    tree.heading('phone', text='Phone', command=filterByPhone)
    tree.heading('email', text='Email', command=filterByMail)
  
    readTenantsToTable()
    #Add each tenant to the list
    #Display the list of tenants in the window with a scrollbar
    scrollbar = ttk.Scrollbar(frame, orient='vertical', command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    tree.pack(side=LEFT, fill=BOTH, padx=20, pady=20, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)
  
    #Add a button to return to the home page
    Button(tenantListWindow, text="Homepage", font=font,
           command=homePage).pack(fill=X,
                                           expand=True,
                                           side=BOTTOM,
                                           padx=20,
                                           pady=20)
    #Start the main loop
    tenantListWindow.mainloop()
  
