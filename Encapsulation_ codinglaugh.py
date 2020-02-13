class Vehical:

    def __init__(self, name):

        self.name = name # public
        self._name = name   #protected
        self.__name = name #private

v = Vehical("Solimuddin")

print(v.name)
print(v._name)


# The turials was wrong
print(v._Vehical__name)