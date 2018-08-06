#   https://leetcode.com/problems/subdomain-visit-count

#   https://leetcode.com/problems/subdomain-visit-count/solution


class Solution:
    #   97.64%
    def subdomainVisits(self, cpdomains):
        cntDict = {}
        for cpdomain in cpdomains:
            cnt, domain = cpdomain.split(' ')
            cnt = int(cnt)
            if domain in cntDict:
                cntDict[domain] += cnt
            else:
                cntDict[domain] = cnt
            for i, d in enumerate(domain):
                if '.' == d:
                    sub = domain[i + 1:]
                    if sub in cntDict:
                        cntDict[sub] += cnt
                    else:
                        cntDict[sub] = cnt
        return ['{} {}'.format(v, k) for k, v in cntDict.items()]


s = Solution()
data = [(["9001 discuss.leetcode.com"], ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]),
        (["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"], ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]),
        ]
for cpdomains, expected in data:
    real = s.subdomainVisits(cpdomains)
    print('{}, expected {}, real {}, result {}'.format(cpdomains, expected, real, sorted(expected) == sorted(real)))
