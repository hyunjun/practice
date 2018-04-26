#   https://stackoverflow.com/questions/32831150/maximum-recursion-depth-error-in-python-when-calling-supers-init?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

class Foo:
    def __init__(self):
        print('foo')


class Bar(Foo):
    def __init__(self):
        super(Bar, self).__init__()
        print('bar')


foo = Foo()
bar = Bar()


class Zoo(Bar):
    def __init__(self):
        super(Zoo, self).__init__()
        print('zoo')


zoo = Zoo()
