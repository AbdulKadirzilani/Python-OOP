class Student:

    @staticmethod
    def getAge(age):

        if age<40:

             print("Old")
        else:
            print("Elder")

#No constructor define ,So parameter will not be Pass
#s2 =Student(60)

print(Student.getAge(19))

s1= Student()

print(s1.getAge(8))


