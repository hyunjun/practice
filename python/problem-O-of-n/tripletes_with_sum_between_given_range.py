#   https://www.interviewbit.com/problems/triplets-with-sum-between-given-range


'''
discussion에 올라온 흥미로운 풀이법
prshntsingh
1 .Convert string array(A) to array of double numbers(v).
2. Sort this array.
3. Use three pointer left(l), middle(m) and right®.
4. Initialize l=0, m=1, r = n-1;

See following code:

while(r>m &&r>l)
    {
        if(v[l]+v[m]+v[r]>1 && v[l]+v[m]+v[r]<2)
        {
            f=1;  //flag
            r--;
            r++;
            l++;
        }
        else if(v[l]+v[m]+v[r]>=2)
        {
            r--;
        }
        else if(v[l]+v[m]+v[r]<=1)
        {
            l++;
            m++;

        }
    }
'''


from typing import List


class Solution:
    #   Wrong Answer
    def tripletSum0(self, arr: List[int]) -> int:
        if arr is None or 0 == len(arr):
            return 0
        arr = sorted(float(a) for a in arr if float(a) < 2.0)
        print(arr)
        for i, a in enumerate(arr):
            _min, _max, l, r = 1 - a, 2 - a, i + 1, len(arr) - 1
            if _min <= 0 or _max <= 0:
                break
            print(_min, _max, l, r)
            while l < r:
                print(l, r)
                _sum = arr[l] + arr[r]
                if _min < _sum < _max:
                    return 1
                if _sum <= _min:
                    print('{}; min case {}->{}, {} -> {} < {}'.format(a, l, arr[l], r, arr[r], _min))
                    prev_l = l
                    l = (l + r) // 2
                    if l == prev_l:
                        break
                elif _max <= _sum:
                    print('{}; max case {} < {}->{}, {} -> {}'.format(a, _max, l, arr[l], r, arr[r]))
                    prev_r = r
                    r = (l + r) // 2
                    if r == prev_r:
                        break
        return 0

    #   Time Limit Exceeded
    def tripletSum1(self, arr: List[int]) -> int:
        if arr is None or 0 == len(arr):
            return 0
        arr = sorted(float(a) for a in arr)
        for i, a in enumerate(arr):
            for j in range(i + 1, len(arr)):
                _min, _max, l, r = 1 - a - arr[j], 2 - a - arr[j], j + 1, len(arr) - 1
                if _min < 0:
                    _min = 0
                while l <= r:
                    m = (l + r) // 2
                    if _min < arr[m] < _max:
                        return 1
                    if arr[m] < _min:
                        l = m + 1
                    else:
                        r = m - 1
        return 0

    def tripletSum(self, arr: List[int]) -> int:
        if arr is None or 0 == len(arr):
            return 0
        arr, A, B, C, D = [float(a) for a in arr if float(a) < 2], [], [], [], []
        #print(boundaries)
        for a in arr:
            if 0 < a <= 1 / 3:
                A.append(a)
            elif 1 / 3 < a < 2 / 3:
                B.append(a)
            elif 2 / 3 <= a < 1:
                C.append(a)
            elif 1 <= a < 2:
                D.append(a)
        #print(f'A {A}, B {B}, C {C}, D {D}')
        lenA, lenB, lenC, lenD = len(A), len(B), len(C), len(D)
        if 3 <= lenB or (1 <= lenA and 1 <= lenB and 1 <= lenC):
            return 1
        rA, rB, rC = sorted(A, reverse=True), sorted(B, reverse=True), sorted(C, reverse=True)
        if 2 <= lenA and 1 <= lenB and 1 < sum(rA[0:2], rB[0]) < 2:
            return 1
        if 2 <= lenA and 1 <= lenC and 1 < sum(rA[0:2], rC[0]) < 2:
            return 1
        if 1 <= lenA and 2 <= lenB and 1 < sum(rB[0:2], rA[0]) < 2:
            return 1
        A, B, C, D = sorted(A), sorted(B), sorted(C), sorted(D)
        if 2 <= lenA and 1 <= lenD and 1 < sum(A[0:2], D[0]) < 2:
            return 1
        if 2 <= lenB and 1 <= lenC and 1 < sum(B[0:2], C[0]) < 2:
            return 1
        if 2 <= lenB and 1 <= lenD and 1 < sum(B[0:2], D[0]) < 2:
            return 1
        if 1 <= lenA and 2 <= lenC and 1 < sum(C[0:2], A[0]) < 2:
            return 1
        if 1 <= lenB and 2 <= lenC and 1 < sum(C[0:2], B[0]) < 2:
            return 1
        if 1 <= lenA and 1 <= lenB and 1 <= lenD and 1 < A[0] + B[0] + D[0] < 2:
            return 1
        if 1 <= lenA and 1 <= lenC and 1 <= lenD and 1 < A[0] + C[0] + D[0] < 2:
            return 1
        return 0


s = Solution()
data = [(['0.6', '0.7', '0.8', '1.2', '0.4'], 1),
        (['2.673662', '2.419159', '0.573816', '2.454376', '0.403605', '2.503658', '0.806191' ], 1),
        (['0.297657', '0.420048', '0.053365', '0.437979', '0.375614', '0.264731', '0.060393', '0.197118', '0.203301', '0.128168'], 1),
        (['0.503094', '0.648924', '0.999298'], 0),
        (['0.366507', '0.234601', '2.126313', '1.372403', '2.022170', '0.308558', '2.120754', '1.561462'], 1),
        (['2.445610', '0.129967', '2.376455', '1.910948', '0.917844', '0.815911', '1.743973'], 1),
        (['2.012771', '2.058788', '1.930395', '1.256333', '0.487474', '2.424690', '1.215940', '0.107228'], 1),
        ]
for arr, expected in data:
    real = s.tripletSum(arr)
    print(f'{arr}, expected {expected}, real {real}, result {expected == real}')
