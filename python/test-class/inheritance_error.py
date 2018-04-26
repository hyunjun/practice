class Foo:
    def __init__(self):
        print('foo')


class Bar(Foo):
    def __init__(self):
        super(self.__class__, self).__init__()
        print('bar')


foo = Foo()
bar = Bar()


#   RecursionError: maximum recursion depth exceeded while calling a Python object
class Zoo(Bar):
    def __init__(self):
        super(self.__class__, self).__init__()
        print('zoo')


zoo = Zoo()
