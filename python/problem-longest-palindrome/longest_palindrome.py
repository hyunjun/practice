# https://leetcode.com/problems/longest-palindromic-substring

data = ['babad',
        'cbbd',
        'babbd',
        'bbbad',
        'klvxwqyzugrdoaccdafdfrvxiowkcuedfhoixzipxrkzbvpusslsgfjocvidnpsnkqdfnnzzawzsslwnvvjyoignsfbxkgrokzyusxikxumrxlzzrnbtrixxfioormoyyejashrowjqqzifacecvoruwkuessttlexvdptuvodoavsjaepvrfvbdhumtuvxufzzyowiswokioyjtzzmevttheeyjqcldllxvjraeyflthntsmipaoyjixygbtbvbnnrmlwwkeikhnnmlfspjgmcxwbjyhomfjdcnogqjviggklplpznfwjydkxzjkoskvqvnxfzdrsmooyciwulvtlmvnjbbmffureoilszlonibbcwfsjzguxqrjwypwrskhrttvnqoqisdfuifqnabzbvyzgbxfvmcomneykfmycevnrcsyqclamfxskmsxreptpxqxqidvjbuduktnwwoztvkuebfdigmjqfuolqzvjincchlmbrxpqgguwuyhrdtwqkdlqidlxzqktgzktihvlwsbysjeykiwokyqaskjjngovbagspyspeghutyoeahhgynzsyaszlirmlekpboywqdliumihwnsnwjc',
        '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000']


def is_palindrome(s):
  return s == s[::-1]


def longest_palindrome(s):
  max_len, max_str = 1, s[0]
  for i in range(len(s)):
    for j in range(i, len(s)):
      if is_palindrome(s[i : j + 1]):
        if max_len < j + 1 - i:
          max_len = j + 1 - i
          max_str = s[i : j + 1]
  return max_str


def longest_palindrome2(s):
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


for s in data:
  print(s, longest_palindrome2(s))

