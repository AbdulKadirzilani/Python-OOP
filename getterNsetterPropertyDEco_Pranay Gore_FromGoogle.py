class Employee:
    def __init__(self,name,company,v,retired = 'No'):
        self._name = name
        self.__company = company   # private attribute
        self.__retired = retired
        self.v=v

#company getter method
    # @property
    # def getCompany(self):
    #     print("Property getter class Method")
    #     return self.__company
    #
    # #company setter method
    # @getCompany.setter
    # def getCompany(self,value):
    #     print("setter method property")
    #     self.__company = value



    @property
    def getCompany(self):
        print("Property getter class Method")
        return self.__company

    #company setter method
    @getCompany.setter
    def getCompany(self,value):
        print("setter method property")
        self.__company = value



e =Employee('Pranoy','Amazon',"zilani")
print(e.getCompany)
e.getCompany = "google"
print(e.getCompany)

#set vaule by calling the property method using class name

Employee.getCompany = "Microsoft"
print(Employee.getCompany)


#_company private attribute tai eke direct access kora jaina
#print(e.__company)

#print(e._Employee._company)



