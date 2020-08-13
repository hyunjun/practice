#   https://leetcode.com/problems/iterator-for-combination

#   https://leetcode.com/problems/iterator-for-combination/discuss/452186/Python-generator-yield-and-Python-built-in-cheat


#   runtime; 48ms, 76.75%
#   memory; 15.1MB, 100.00%
class CombinationIterator0:

    def __init__(self, characters: str, combinationLength: int):
        self.combis, self.idx = [], 0
        def combi(acc, s, n):
            if n == 1:
                for c in s:
                    self.combis.append(acc + c)
            else:
                for i, c in enumerate(s):
                    combi(acc + c, s[i + 1:], n - 1)

        combi('', characters, combinationLength)

    def next(self) -> str:
        ret = self.combis[self.idx]
        self.idx += 1
        return ret

    def hasNext(self) -> bool:
        return self.idx < len(self.combis)

#   https://leetcode.com/explore/featured/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3422
#   runtime; 52ms, 86.77%
#   memory; 15.9MB, 58.70%
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations, self.hasMore = self.combi(set(), combinationLength, characters), True
        self.nextVal = next(self.combinations)

    def combi(self, used, left, s):
        if left == 1:
            for c in s:
                if c in used:
                    continue
                yield c
        else:
            for i, c in enumerate(s):
                if c in used:
                    continue
                used.add(c)
                for n in self.combi(used, left - 1, s[i + 1:]):
                    yield c + n
                used.remove(c)
                
    def next(self) -> str:
        ret = None
        try:
            ret = self.nextVal
            self.nextVal = next(self.combinations)
        except StopIteration:
            self.nextVal, self.hasMore = None, False
        return ret

    def hasNext(self) -> bool:
        return self.hasMore        


# Your CombinationIterator object will be instantiated and called as such:
obj = CombinationIterator('abc', 2)
print(obj.next() == 'ab')
print(obj.hasNext() == True)
print(obj.next() == 'ac')
print(obj.hasNext() == True)
print(obj.next() == 'bc')
print(obj.hasNext() == False)
