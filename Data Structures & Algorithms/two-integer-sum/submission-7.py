class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for i,n in enumerate(nums):
            hashmap[n] = i
        
        for i,n in enumerate(nums):
            comp = target - n
            if comp in hashmap and hashmap[comp] != i:
                return [i, hashmap[comp]]
        return []