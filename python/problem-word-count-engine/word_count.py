# https://www.pramp.com/question/W5EJq2Jld3t2ny9jyZXG

# first idea
# split string by whitespace & punctuation O(N)
# put it into the Counter dictionary to check the word count O(N)
# sort Counter by its count O(NlogN)
# then return sorted Counter

# wire-frame ==> BETTER: wireframe
# "Practice makes perfect. Get perfect by practice. Just practice!"


# if there is only whitespaces it's easy, split()
# if there are many punctuations, special chars !@$#%@#.'
# to clean up the string, using regular expression
# re.sub(pattern, '', str) , then use split()

from collections import Counter
import re

PATTERN = re.compile('[^ a-zA-Z]')

def word_count(s):
   if s is None or 0 == len(s):
      return None
   
   # remove all the punctuations
   cleaned_s = re.sub(PATTERN, '', s.lower())
   
   # split by whitespace
   splited_s = cleaned_s.split()
   
   # Counter
   counter_s = Counter(splited_s)
   
   # sort
   sorted_counter_s = sorted(counter_s.items(), key=lambda t: t[1], reverse=True)
   
   return sorted_counter_s

print word_count("practice makes perfect. get perfect by practice. just practice!")
# { practice: 3, perfect: 2,  makes: 1, get: 1, by: 1, just: 1 }
# let M be the number of UNIQUE words
# time = O(n + mlogm)
