import sys


FNV_64_INIT = 0xFFFFFFFFFFFFFFFF & 0xcbf29ce484222325
FNV_64_PRIME = 0xFFFFFFFFFFFFFFFF & 0x100000001b3;


def hash_fnv1a_64(key):
  hash = 0xFFFFFFFF & FNV_64_INIT

  for x in key:
    val = 0xFFFFFFFF & ord(x)
    hash ^= val
    hash *= 0xFFFFFFFF & FNV_64_PRIME

  return 0xFFFFFFFF & hash


for line in sys.stdin.readlines():
  line = line.strip()
  hashed_val = hash_fnv1a_64(line)
  print('{}\t{}\t{}'.format(line, hashed_val, hashed_val % 10))
