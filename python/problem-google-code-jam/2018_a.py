import sys


#   https://blog.naver.com/ndb796/221247631646


class Solution:
    def changeOrders(self, inp, damageLimit):
        damage = 1
        accumulatedDamages, accumulatedDamage = [], 0
        csIndices = [] #   charge and shoot indices
        for i, c in enumerate(inp):
            if 'C' == c:
                damage *= 2
                accumulatedDamages.append(0)
            elif 'S' == c:
                accumulatedDamage += damage
                accumulatedDamages.append(damage)
                if 0 < i and inp[i - 1] == 'C':
                    csIndices.append(i)
        #print('accumulated damage {}, {}'.format(accumulatedDamage, csIndices))
        if 0 == accumulatedDamage or accumulatedDamage <= damageLimit:
            return 0
        numberOfChanges = 0
        idx = 1
        inps = list(inp)
        while idx < len(inps):
            if 'S' == inps[idx] and 'C' == inps[idx - 1]:
                #print('CS detected inp {}, index {}'.format(inps, idx))
                reducedDamage = accumulatedDamages[idx] / 2
                accumulatedDamages[idx - 1] = reducedDamage
                accumulatedDamage -= reducedDamage
                accumulatedDamages[idx] = 0
                numberOfChanges += 1
                #print('accumulated damage {}, {}'.format(accumulatedDamage, accumulatedDamages))
                inps[idx - 1], inps[idx] = 'S', 'C'
                if accumulatedDamage <= damageLimit:
                    return numberOfChanges
                if 0 <= idx - 2 and 'C' == inps[idx - 2] and 'S' == inps[idx - 1]:
                    idx -= 1
                else:
                    idx += 1
            else:
                idx += 1
        return -1


s = Solution()
data = [(1, 'CS', 1), (2, 'CS', 0), (1, 'SS', -1), (6, 'SCCSSC', 2), (2, 'CC', 0), (3, 'CSCSS', 5)]
for damage_limit, attack, expected_number_of_change in data:
    real = s.changeOrders(attack, damage_limit)
    print('damage limit {}, attack {}, expected {}, real {}, result {}'.format(damage_limit, attack, expected_number_of_change, real, expected_number_of_change == real))


'''
SCCSSC
1  44
SCSCSC
1 2 4
SCSSCC
1 22

CSCSS
 2 44
SCCSS
1  44
SCSCS
1 2 4
SCSSC
1 22
SSCSC
11 2
SSSCC
111
'''
