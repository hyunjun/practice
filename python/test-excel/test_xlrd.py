#   https://stackoverflow.com/questions/53940031/python-converting-excel-file-to-json-format

#   python3 -m virtualenv .venv
#   pip install xlrd


import xlrd
import json

wb = xlrd.open_workbook('test.xlsx')
sh = wb.sheet_by_index(0)
keys = sh.row_values(0)
dialogs = []
for r in range(1, sh.nrows):
    d, row = {}, sh.row_values(r)
    d['questions'] = {keys[0]: row[0], keys[1]: row[1]}
    d['answers'] = {keys[2]: row[2], keys[3]: row[3]}
    d['id'] = int(row[4])
    dialogs.append(d)
print(json.dumps(dialogs))
