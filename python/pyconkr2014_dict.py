# -*- coding: utf8 -*-

# 만들기
print {'jan': 1, 'feb': 2, 'mar': 3}
print dict(jan=1, feb=2, mar=3)
month_names = [('jan', 1), ('feb', 2), ('mar', 3), ('apr', 4), ('may', 5), ('jun', 6)]
months = dict(month_names)
print months

print {name.title(): num for name, num in month_names}
print {name: num for name, num in month_names if num % 2 == 0}

print {v: k for k, v in months.items()}

print months['jan']
# print months['Jan']
print 'Jan' in months
print months.get('Jan')
print months.get('Jan', 1)
print months.setdefault('Jan', 1)
print months['Jan']
