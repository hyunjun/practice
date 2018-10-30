#   https://leetcode.com/problems/unique-email-addresses


class Solution:
    def numUniqueEmails(self, emails):
        res = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.', '')
            local = local[:local.index('+')]
            res.add('{}@{}'.format(local, domain))
        print(res)
        return len(res)


s = Solution()
data = [(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"], 2), #   "testemail@leetcode.com", "testemail@lee.tcode.com"
        ]
for emails, expected in data:
    real = s.numUniqueEmails(emails)
    print('{}, expected {}, real {}, result {}'.format(emails, expected, real, expected == real))
