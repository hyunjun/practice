#   https://leetcode.com/problems/iterator-for-combination

#   https://leetcode.com/problems/iterator-for-combination/discuss/452186/Python-generator-yield-and-Python-built-in-cheat


#   runtime; 48ms, 76.75%
#   memory; 15.1MB, 100.00%
class CombinationIterator:

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
        


# Your CombinationIterator object will be instantiated and called as such:
obj = CombinationIterator('abc', 2)
print(obj.next() == 'ab')
print(obj.hasNext() == True)
print(obj.next() == 'ac')
print(obj.hasNext() == True)
print(obj.next() == 'bc')
print(obj.hasNext() == False)
