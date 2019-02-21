#   https://leetcode.com/problems/time-based-key-value-store

#   https://leetcode.com/problems/time-based-key-value-store/solution


from collections import defaultdict

#   runtime; 848ms, 14.35%
#   memory; 61.4MB, 92.45%
class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        values = self.d[key]
        if 0 == len(values):
            values.append((timestamp, value))
        else:
            l, r = 0, len(values) - 1
            while l < r:
                m = (l + r) // 2
                if values[m][0] == timestamp:
                    break
                elif values[m][0] < timestamp:
                    l = m + 1
                else:
                    r = m - 1
            pos = (l + r) // 2
            if values[pos][0] == timestamp:
                values[pos] = (timestamp, value)
            elif values[pos][0] < timestamp:
                values.insert(pos + 1, (timestamp, value))
            else:
                values.insert(pos - 1, (timestamp, value))
        self.d[key] = values

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        values = self.d[key]
        if 0 == len(values):
            return ''
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][0] <= timestamp and (m == len(values) - 1 or timestamp < values[m + 1][0]):
                return values[m][1]
            elif values[m + 1][0] <= timestamp:
                l = m + 1
            else:
                r = m - 1
        return ''


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set('foo', 'bar', 1)
obj.set('foo', 'bar2', 4)
for key, timestamp, expected in [('foo', 1, 'bar'), ('foo', 3, 'bar'), ('foo', 4, 'bar2'), ('foo', 5, 'bar2')]:
    real = obj.get(key, timestamp)
    print('key {} timestamp {} -> expected {}, real {}, result {}'.format(key, timestamp, expected, real, expected == real))
'''
foo 1   4
love    10  20
'''

obj.set('love', 'high', 10)
obj.set('love', 'low', 20)
for key, timestamp, expected in [('love', 5, ''), ('love', 10, 'high'), ('love', 15, 'high'), ('love', 20, 'low'), ('love', 25, 'low')]:
    real = obj.get(key, timestamp)
    print('key {} timestamp {} -> expected {}, real {}, result {}'.format(key, timestamp, expected, real, expected == real))
