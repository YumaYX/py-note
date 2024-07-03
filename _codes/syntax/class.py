class MyClass:
    def __init__(self, val):
        print("initializer")
        self.val = val

    def myclassdef(self):
        print("myclassdef")
        return 0

x = MyClass(2)

print("x.val:", x.val)
x.myclassdef()

print("type(x):", type(x))
print("type(x.myclassdef):", type(x.myclassdef))
print("type(x.myclassdef()):", type(x.myclassdef()))


print("Inherit:")
class Inherit(MyClass):
    pass

Inherit(3)
