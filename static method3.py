class Student:
    a ="Telusko"

    def __init__(self,m1,m2):
        self.m1 =m1
        self.m2 =m2

    def avg(self):
        return (self.m1*self.m2)/2
    @classmethod
    def info(cls):
        return cls.a

    @staticmethod
    def info2(a):
        return a
    #
    # @staticmethod
    # def info2():
    #     return "This is Static method"

Student.a=50
s1= Student(4,5)
print(s1.avg())
print(Student.info())
print(Student.info2(4))