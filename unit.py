"""
Group 7 James Lynch, Karla Chuprinski, 
Dev Paul, Vu Phan, William Gomez, Camelia Sama
04/30/23
"""
class Unit:
  def __init__(self, unitNumber, unitPrice, tenant):
    self._number = unitNumber
    self._price = unitPrice
    self._tenant = tenant
    
    def getUnitNumber(self):
      return self._unitNumber

    def getUnitPrice(self):
      return self._price

    def getUnitTenant(self):
      return self._tenant

    def isUnitOccupied(self):
      if (self._tenant == None):
        return False
      else:
        return True