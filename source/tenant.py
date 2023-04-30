"""
Group 7 James Lynch, Karla Chuprinski, 
Dev Paul, Vu Phan, William Gomez, Camelia Sama
04/30/23
"""
class Tenant:
  def __init__(self, lastName, firstName, unitNumber, phoneNumber, email):
    self.lastName = lastName
    self.firstName = firstName
    self.unitNumber = unitNumber
    self.phoneNumber = phoneNumber
    self.email = email

 
  def getLastName(self):
    return self.lastName
    
  def getFirstName(self):
    return self.firstName
    
  def getUnitNumber(self):
    return self.unitNumber
    
  def getContactInformation(self):
    return self.phoneNumber, self.email
    
  def setLastName(self, lastName):
    self.lastName = lastName
    
  def setFirstName(self, firstName):
    self.firstName = firstName
    
  def setUnitNumber(self, unitNumber):
    self.unitNumber = unitNumber

  def setContactInformation(self, phoneNumber, email):
    self.phoneNumber = phoneNumber
    self.email = email

  

  