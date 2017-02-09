# https://www.pramp.com/question/AMypWAprdmUlaP2gPVLZ
import json

def flatten_recur(d):
    result = {}
    for k, v in d.items():
        if isinstance(v, dict):
            for k1, v1 in flatten_recur(v).items():
                result['{}.{}'.format(k, k1)] = v1
        else:
            result[k] = v
    return result

inp = '{"Key1": "1", "Key2": {"a" : "2", "b" : "3", "c" : {"d" : "3", "e" : "1"}}}'
d = json.loads(inp)
print flatten_recur(d)
