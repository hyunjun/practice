#   https://leetcode.com/problems/employee-importance

#   https://leetcode.com/problems/employee-importance/solution


class Solution:
    #   37.96%
    def getImportance(self, employees, id):
        if employees is None or 0 == len(employees):
            return 0
        impDict, parentDict = {}, {}
        '''
        #   submit할 때는 문제의 class 구조에 맞춰 이렇게 사용
        for employee in employees:
            impDict[employee.id] = employee.importance
            for subId in employee.subordinates:
                parentDict[subId] = employee.id
        '''
        for _id, impVal, subList in employees:
            impDict[_id] = impVal
            for subId in subList:
                parentDict[subId] = _id
        if id not in impDict:
            return 0
        visited, _sum = set(), 0
        for _id, parent in parentDict.items():
            if parent == id:
                if _id not in visited:
                    _sum += impDict[_id]
                    visited.add(_id)
            else:
                while parent in parentDict:
                    parent = parentDict[parent]
                    if parent == id:
                        if _id not in visited:
                            _sum += impDict[_id]
                            visited.add(_id)
                        break
        if id not in visited:
            _sum += impDict[id]
        return _sum


s = Solution()
data = [([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1, 11),
        ([[1, 15, [2]], [2, 10, [3]], [3, 5, []]], 1, 30),
        ]
for employees, _id, expected in data:
    real = s.getImportance(employees, _id)
    print('{}, {}, expected {}, real {}, result {}'.format(employees, _id, expected, real, expected == real))
