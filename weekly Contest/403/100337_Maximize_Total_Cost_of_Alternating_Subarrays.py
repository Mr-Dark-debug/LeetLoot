from typing import List
from functools import lru_cache

class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(ind: int, lastp: bool) -> int:
            if ind == n:
                return 0
            res = dfs(ind + 1, True) + nums[ind]
            if lastp:
                res = max(res, dfs(ind + 1, False) - nums[ind])
            return res
        
        return dfs(0, False)
