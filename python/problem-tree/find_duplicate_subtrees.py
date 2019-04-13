#   https://leetcode.com/problems/find-duplicate-subtrees


from TreeNode import TreeNode
from collections import defaultdict

class Solution:
    #   Time Limit Exceeded
    def findDuplicateSubtrees0(self, root):
        if root is None:
            return []

        #   1. traverse, and construct dict[node.val] = [node]
        q, d = [root], defaultdict(list)
        while q:
            node = q.pop(0)
            d[node.val].append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        #   2. if dict 1 < len(value): check duplication, res.append(node) if it's true
        #def isDuplicated(n1, n2):
        #    if n1 is None and n2 is None:
        #        return True
        #    if n1 is None or n2 is None or n1.val != n2.val:
        #        return False
        #    return isDuplicated(n1.left, n2.left) and isDuplicated(n1.right, n2.right)

        def traverseStr(n):
            res, q = [], [n]
            while q:
                node = q.pop(0)
                if node:
                    res.append(str(node.val))
                    if node.left or node.right:
                        q.append(node.left)
                        q.append(node.right)
                else:
                    res.append('x')
            return ','.join(res)

        resDict = defaultdict(list)
        for val, nodes in d.items():
            if len(nodes) < 2:
                continue
            for i, node in enumerate(nodes):
                iStr = traverseStr(node)
                for j in range(i + 1, len(nodes)):
                    jStr = traverseStr(nodes[j])
                    #if isDuplicated(node, nodes[j]):
                    #    resDict[node.val].append(node)
                    #    break
                    if iStr == jStr:
                        resDict[iStr].append(node)
                        break
        #print(resDict)
        return [values[0] for _, values in resDict.items()]

    #   Wrong Answer
    def findDuplicateSubtrees1(self, root):
        if root is None:
            return []

        def nodes(n):
            if n is None:
                return []
            q, d = [n], []
            while q:
                node = q.pop(0)
                d.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            return d

        def isDuplicated(n1, n2):
            if n1 is None and n2 is None:
                return True
            if n1 is None or n2 is None or n1.val != n2.val:
                return False
            return isDuplicated(n1.left, n2.left) and isDuplicated(n1.right, n2.right)

        def traverseStr(n):
            res, q = [], [n]
            while q:
                node = q.pop(0)
                if node:
                    res.append(str(node.val))
                    if node.left or node.right:
                        q.append(node.left)
                        q.append(node.right)
                else:
                    res.append('x')
            return ','.join(res)

        lefts, rights, res = nodes(root.left), nodes(root.right), []
        resDict = defaultdict(list)
        for left in lefts:
            lStr = traverseStr(left)
            for right in rights:
                rStr = traverseStr(right)
                if lStr == rStr:
                    resDict[lStr].append(left)
                #if isDuplicated(left, right):
                #    res.append(left)
                    break

        #print(res)
        #return res
        print(resDict)
        return [values[0] for _, values in resDict.items()]

    #   Wrong Answer
    def findDuplicateSubtrees2(self, root):
        if root is None:
            return []

        top = root
        while not (top.left and top.right):
            if top.left is None:
                top = top.right
            elif top.right is None:
                top = top.left
            if top is None:
                return []

        q, valNodeDict = [top], defaultdict(list)
        while q:
            n = q.pop(0)
            valNodeDict[n.val].append(n)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

        def isSameTree(n0, n1):
            if n0 is None and n1 is None:
                return True
            if n0 is None or n1 is None or n0.val != n1.val:
                return False
            return isSameTree(n0.left, n1.left) and isSameTree(n0.right, n1.right)

        def isLeaf(n):
            if n.left is None and n.right is None:
                return True
            return False

        def traverseStr(n):
            res, q = [], [n]
            while q:
                node = q.pop(0)
                if node:
                    res.append(str(node.val))
                    if node.left or node.right:
                        q.append(node.left)
                        q.append(node.right)
                else:
                    res.append('x')
            return ','.join(res)

        ret = []
        for val, nodes in valNodeDict.items():
            if 1 == len(nodes):
                continue
            visited, hasSameTree = set(), False
            for i, node in enumerate(nodes):
                if hasSameTree and traverseStr(node) in visited:
                #if node in visited or (isLeaf(node) and node.val in visitedLeaf):
                    continue
                for j in range(i + 1, len(nodes)):
                    if hasSameTree and traverseStr(nodes[j]) in visited:
                    #if nodes[j] in visited or (isLeaf(nodes[j]) and node.val in visitedLeaf):
                        continue
                    if isSameTree(node, nodes[j]):
                        ret.append(node)
                        visited.add(traverseStr(node))
                        hasSameTree = True
                        #visited.add(node)
                        #visited.add(nodes[j])
                        #if node.left is None and node.right is None:
                        #    visitedLeaf.add(node.val)
                        break
        return ret

    #   runtime; 172ms, 8.70%
    #   memory; 14.5MB, 100.00%
    def findDuplicateSubtrees(self, root):
        if root is None:
            return []

        top = root
        while not (top.left and top.right):
            if top.left is None:
                top = top.right
            elif top.right is None:
                top = top.left
            if top is None:
                return []

        q, valNodeDict = [top], defaultdict(list)
        while q:
            n = q.pop(0)
            valNodeDict[n.val].append(n)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

        def traverseStr(n):
            lVal, rVal = 'x', 'x'
            if n.left is None and n.right is None:
                lVal, rVal = '', ''
            if n.left:
                lVal = traverseStr(n.left)
            if n.right:
                rVal = traverseStr(n.right)
            return '({} {} {})'.format(lVal, n.val, rVal)

        ret, visited = [], defaultdict(int)
        for val, nodes in valNodeDict.items():
            if 1 == len(nodes):
                continue
            for i, node in enumerate(nodes):
                treeStr = traverseStr(node)
                visited[treeStr] += 1
                if 2 < visited[treeStr]:
                    continue
                if 2 == visited[treeStr]:
                    ret.append(node)
        return ret

s = Solution()
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.right.left = TreeNode(2)
root1.right.right = TreeNode(4)
root1.right.left.left = TreeNode(4)
root2 = TreeNode(0)
root2.left = TreeNode(0)
root2.right = TreeNode(0)
root2.left.left = TreeNode(0)
root2.right.right = TreeNode(0)
root2.right.right.left = TreeNode(0)
root3 = TreeNode(0)
root3.left = TreeNode(0)
root3.right = TreeNode(0)
root3.left.left = TreeNode(0)
root3.right.right = TreeNode(0)
root3.left.left.left = TreeNode(0)
root3.left.left.right = TreeNode(0)
root3.right.right.left = TreeNode(0)
root3.right.right.right = TreeNode(0)
for root in [root1, root2, root3]:
    print(root)
    for duplicated in s.findDuplicateSubtrees(root):
        print(duplicated)
