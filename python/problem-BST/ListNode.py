class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        '''
        res = '({})->'.format(self.val)
        if self.next:
            res += str(self.next)
        else:
            res += 'None'
        return res
        '''
        if self.next:
            return '({})->{}'.format(self.val, self.next)
        return '({})->x'.format(self.val)
