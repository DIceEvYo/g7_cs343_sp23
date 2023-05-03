import database3

#If we want to deal with extra data work, then do this stuff, only if we have time.
"""
#Reads the username from the landlordAccount.txt file
    with open('landlordAccount.txt', 'r') as file:
        username = file.readline().strip()


    #Displays the total number of units, occupied units, remaining units and unpaid rents
    Label(homePageWindow, text="Total Units:", font=font, padx=20, pady=10, bg='white').grid(row=2, column=0)
    Label(homePageWindow, text="Occupied Units:", font=font, padx=20, pady=10, bg='white').grid(row=3, column=0)
    Label(homePageWindow, text="Available Units:", font=font, padx=20, pady=10, bg='white').grid(row=4, column=0)
    Label(homePageWindow, text="Unpaid Rent:", font=font, padx=20, pady=10, bg='white').grid(row=5, column=0)
    
    total_units = 50 #Replaces with the total number of units in the building
    occupied_units = 25 #Replace with the number of occupied units in the building
    available_units = total_units - occupied_units
    unpaid_rent = 1500 #Replace with the total amount of unpaid rent in the building

    Label(homePageWindow, text=str(total_units), font=font, bg='white').grid(row=2, column=1)
    Label(homePageWindow, text=str(occupied_units), font=font, bg='white').grid(row=3, column=1)
    Label(homePageWindow, text=str(available_units), font=font, bg='white').grid(row=4, column=1)
    Label(homePageWindow, text="$" + str(unpaid_rent), font=font, bg='white').grid(row=5, column=1)
    
    
    
    total_units = int(database3.performQuery(SELECT COUNT(tenant_list.apartment_number) FROM tenant_list)[0][0])
#Replaces with the total number of units in the building
occupied_units = 25 #Replace with the number of occupied units in the building
available_units = total_units - occupied_units
unpaid_rent = 1500 #Replace with the total amount of unpaid rent in the building

print("total units: " + str(total_units))
database3.displayPerformQuery(SELECT COUNT(tenant_list.apartment_number) FROM tenant_list WHERE tenant_list.)
#print("occupied units: " + str(occupied_units))
"""

database3.displayPerformQuery("""SELECT tenant_list.first_name, tenant_list.last_name, 
        tenant_list.apartment_number, tenant_list.phone_number, tenant_list.email FROM tenant_list  
                    ORDER BY tenant_list.first_name, tenant_list.last_name""")
