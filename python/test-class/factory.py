#   http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html


class Shape:
    @classmethod
    def factory(cls, _type, msg):
        if 'Circle' == _type:
            return Circle(msg)
        if 'Square' == _type:
            return Square(msg)
        return None

    def __init__(self, msg):
        self.msg = msg
        print('Shape {}'.format(self.msg))
        if 'draw' == self.msg:
            self.act = self.draw
        elif 'erase' == self.msg:
            self.act = self.erase

    def act(self):
        pass


class Circle(Shape):
    def __init__(self, msg):
        super(Circle, self).__init__(msg)
        print('Circle {}'.format(self.msg))
    def draw(self):
        print('Circle.draw by {}'.format(self.msg))
    def erase(self):
        print('Circle.erase by {}'.format(self.msg))


class Square(Shape):
    def __init__(self, msg):
        super(Square, self).__init__(msg)
        print('Square {}'.format(self.msg))
    def draw(self):
        print('Square.draw by {}'.format(self.msg))
    def erase(self):
        print('Square.erase by {}'.format(self.msg))


for _type, msg in [('Circle', 'draw'), ('Square', 'erase')]:
    shape = Shape.factory(_type, msg)
    shape.act()