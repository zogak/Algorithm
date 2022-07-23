'''
time out
'''
from itertools import combinations
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        combi = combinations(nums, 3)
        for c in combi:
            c = sorted(c)
            if sum(c) == 0 and c not in ans:
                ans.append(list(c))
        return ans
