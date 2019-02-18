#   https://leetcode.com/problems/longest-palindromic-substring

#   https://leetcode.com/problems/longest-palindromic-substring/solution


data = [('babad', 'bab'),
        ('cbbd', 'bb'),
        ('babbd', 'bab'),
        ('bbbad', 'bbb'),
        ('klvxwqyzugrdoaccdafdfrvxiowkcuedfhoixzipxrkzbvpusslsgfjocvidnpsnkqdfnnzzawzsslwnvvjyoignsfbxkgrokzyusxikxumrxlzzrnbtrixxfioormoyyejashrowjqqzifacecvoruwkuessttlexvdptuvodoavsjaepvrfvbdhumtuvxufzzyowiswokioyjtzzmevttheeyjqcldllxvjraeyflthntsmipaoyjixygbtbvbnnrmlwwkeikhnnmlfspjgmcxwbjyhomfjdcnogqjviggklplpznfwjydkxzjkoskvqvnxfzdrsmooyciwulvtlmvnjbbmffureoilszlonibbcwfsjzguxqrjwypwrskhrttvnqoqisdfuifqnabzbvyzgbxfvmcomneykfmycevnrcsyqclamfxskmsxreptpxqxqidvjbuduktnwwoztvkuebfdigmjqfuolqzvjincchlmbrxpqgguwuyhrdtwqkdlqidlxzqktgzktihvlwsbysjeykiwokyqaskjjngovbagspyspeghutyoeahhgynzsyaszlirmlekpboywqdliumihwnsnwjc', 'wnsnw'),
        ('0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
            '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'),
        ]


def is_palindrome(s):
  return s == s[::-1]


#   Time Limit Exceeded
def longest_palindrome0(s):
  max_len, max_str = 1, s[0]
  for i in range(len(s)):
    for j in range(i, len(s)):
      if is_palindrome(s[i : j + 1]):
        if max_len < j + 1 - i:
          max_len = j + 1 - i
          max_str = s[i : j + 1]
  return max_str


#   32.39%
def longest_palindrome1(s):
  if is_palindrome(s):
    return s

  max_len, max_str, idx_dict = 1, s[0], {}
  for i, c in enumerate(s):
    if c in idx_dict:
      l_idx_list = idx_dict[c]
      for l_idx in l_idx_list:
        if is_palindrome(s[l_idx : i + 1]):
          if max_len < i + 1 - l_idx:
            max_len = i + 1 - l_idx
            max_str = s[l_idx : i + 1]
      l_idx_list.append(i)
      idx_dict[c] = l_idx_list
    else:
      idx_dict[c] = [i]
  return max_str


#   26.89%
def longest_palindrome(s):
    if is_palindrome(s):
        return s

    idx_list_dict = {}
    for i, c in enumerate(s):
        if c in idx_list_dict:
            idx_list_dict[c].append(i)
        else:
            idx_list_dict[c] = [i]

    max_len, max_str = 1, s[0]
    for c, idx_list in idx_list_dict.items():
        idx_list_len = len(idx_list)
        for i in range(0, idx_list_len):
            start_idx = idx_list[i]
            for j in range(idx_list_len - 1, -1, -1):
                end_idx = idx_list[j]
                cand = s[start_idx:end_idx + 1]
                if is_palindrome(cand):
                    if max_len < len(cand):
                        max_len = len(cand)
                        max_str = cand
    return max_str


for s, expected in data:
  real = longest_palindrome(s)
  print('{}, expected {}, real {}, result {}'.format(s, expected, real, expected == real))
