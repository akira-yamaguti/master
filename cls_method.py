class Foo:
    clsvar = 0

    def __init__(self, name=""):
        Foo.clsvar += 1
        self.name = name

    def instance_method(self):
        print('in instance_method')
        print('cls ver:',self.clsvar)
        print('instance var:',self.name)

    @classmethod
    def cls_method(cls):
        print('in cls_method')
        print('cls var:',cls.clsvar)

    @staricmethod
    def static_method(self):
        print('in static_method')
        print('cls var:',Foo.clsvar)

f=Foo('foo')
f.instance_method()
f.cls_method()
Foo.cls_method()
Foo.static_method()
print()
b=Foo('bar')
b.instance_method()
print('Foo.clsvar:',b.clsvar)
b.clsvar += 1
print('b.clsbar:',b.clsvar)
print('Foo.clsbar:',Foo.clsvar)
