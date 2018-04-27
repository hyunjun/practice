#   https://stackoverflow.com/questions/32831150/maximum-recursion-depth-error-in-python-when-calling-supers-init

class Foo:
    def __init__(self):
        print('foo')


class Bar(Foo):
    def __init__(self):
        super().__init__()
        print('bar')


foo = Foo()
bar = Bar()


class Zoo(Bar):
    def __init__(self):
        super().__init__()
        print('zoo')


zoo = Zoo()
