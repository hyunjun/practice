#   http://www.careercup.com/question?id=6234634354425856


#   Wrong Answer
def print_parenthesis(n):
    def print_parenthesis_r(s, o, c):   #   s = str, o = # of open, c = # of close
        #print 'start', s, o, c
        if o == 0:
            for i in range(c):
                s += ')'
            print(s)
        if s[-1] == '(':
            if 0 < o:
                print_parenthesis_r(s + '(', o-1, c)
            if 0 < c:
                #print s + ')', o, c-1
                print_parenthesis_r(s + ')', o, c-1)
        elif s[-1] == ')':
            if 0 < o:
                #print s + '(', o-1, c
                print_parenthesis_r(s + '(', o-1, c)
    print_parenthesis_r('(', n-1, n)


def parenthesis_pairs(n):
    res = []
    def parenthesis_pairs_recur(l, o, c):   #   l = parenthesis pairs, o = # of open, c = # of close
        if o == 0:
            for i in range(c):
                l.append(')')
            res.append(''.join(l))
            for i in range(c):
                l.pop()
        elif 0 < o <= c:
            l.append('(')
            parenthesis_pairs_recur(l, o - 1, c)
            l.pop()
            l.append(')')
            parenthesis_pairs_recur(l, o, c - 1)
            l.pop()
    parenthesis_pairs_recur(['('], n - 1, n)
    return res


if __name__ == '__main__':
    #print_parenthesis(2)
    #print_parenthesis(3)
    print(parenthesis_pairs(2))
    print(parenthesis_pairs(3))
