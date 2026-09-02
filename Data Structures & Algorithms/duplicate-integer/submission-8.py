class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       from collections import Counter

       dict_c = Counter(nums)
       for k,v in dict_c.items():
            if v > 1:
                return True

       return False