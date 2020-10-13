#   https://medium.com/swlh/monads-in-python-e3c9592285d6

class Failure():
    def __init__(self, value, failed=False):
        self.value = value
        self.failed = failed
    def get(self):
        return self.value
    def is_failed(self):
        return self.failed
    def __str__(self):
        return ' '.join([str(self.value), str(self.failed)])
    def bind(self, f):
        if self.failed:
            return self
        try:
            x = f(self.get())
            return Failure(x)
        except:
            return Failure(None, True)
    def __or__(self, f):
        return self.bind(f)


x = '1'
y = Failure(x).bind(int)
print(y)

from operator import neg
x = '1'
y = Failure(x).bind(int).bind(neg).bind(str)
print(y)

x = 'XYZ'
y = Failure(x).bind(int).bind(neg).bind(str)
print(y)

x = '1'
y = Failure(x) | int | neg | str
print(y)
