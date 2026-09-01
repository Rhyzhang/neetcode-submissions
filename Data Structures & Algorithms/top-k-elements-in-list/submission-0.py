class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        dict_c = Counter(nums)
        arr = dict_c.most_common(k)
        ans = [k for k,v in arr]
        return ans
                
        