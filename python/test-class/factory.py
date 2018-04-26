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


class Circle(Shape):
    def __init__(self, msg):
        super(Circle, self).__init__(msg)
        print('Circle {}'.format(self.msg))
    def draw(self):
        print('Circle.draw')
    def erase(self):
        print('Circle.erase')


class Square(Shape):
    def __init__(self, msg):
        super(Square, self).__init__(msg)
        print('Square {}'.format(self.msg))
    def draw(self):
        print('Square.draw')
    def erase(self):
        print('Square.erase')


for _type in ['Circle', 'Square']:
    shape = Shape.factory(_type, 'msg: {}'.format(_type.lower()))
    shape.draw()
    shape.erase()
