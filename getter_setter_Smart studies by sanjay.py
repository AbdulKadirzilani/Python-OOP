class Employee:
    def __init__(self,name,company,v,retired = 'No'):
        self._name = name
        self.__company = company   # private attribute
        self.__retired = retired
        self.v=v

#company getter method
    def getCompany(self):
        return self.__company

    #company setter method
    def setCompany(self,value):
        self.__company = value
    def setName(self,name):
        self._name=name

    def getName(self):

            return self._name

e =Employee('Pranoy','Amazon',"zilani")
print(e.getCompany())
print(e.getName())

#    __company private attribute tai eke direct access kora jaina
#print(e.__company)

print(e.Employee.__company)

print(e._name)
print(e.v)


