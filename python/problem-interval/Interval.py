class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '[{},{}]'.format(self.start, self.end)


intervalStrings=lambda intervals: ' '.join([interval.__str__() for interval in intervals])
