# https://www.pramp.com/question/AMypWAprdmUlaP2gPVLZ
import json


def flatten_stack(d):
    result = {}
    stack = [('', d)]
    while stack:
        prefix, target = stack.pop()
        if isinstance(target, dict):
            for k, v in target.items():
                stack.append(('{}.{}'.format(prefix, k), v))
        else:
            result[prefix[1:]] = target
    return result


inp = '{"Key1": "1", "Key2": {"a" : "2", "b" : "3", "c" : {"d" : "3", "e" : "1"}}}'
d = json.loads(inp)
print(flatten_stack(d))
