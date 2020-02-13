class Student:

    def setName(self,a):
        self.__name = a
    def getName(self):
        return self.__name

    def setMarks(self,b):
        self.__marks = b

    def getMarks(self):
         return self.__marks

    '''
    def display(self):
        print(self.__name)
        print(self.__marks)
'''

    def display(self):
        print(self.getName())
        print(self.getMarks())

s1 = Student()
s1.setName("softlet")
s1.setMarks(50)
s1.display()

print("zzz")