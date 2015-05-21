from collections import Counter

if __name__ == '__main__':
  T = int(raw_input())
  for i in range(T):
    N = int(raw_input())
    inps = [int(n) for n in raw_input().split()]

    #nums = [len([i for i in inps if i == idx]) for idx in range(len(inps))]
    #for i in range(1, len(nums)):
    #  nums[i] += nums[i - 1] - 1
    #print reduce(lambda x, y: x * y, nums, 1) % 1000000007

    nums = Counter(inps)
    res = nums[0]
    for i in range(1, len(inps)):
      nums[i] += nums[i - 1] - 1
      res *= nums[i]
    print res % 1000000007
