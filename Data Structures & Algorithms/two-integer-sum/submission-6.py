class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        # Example 1:
        # Input: 
        # nums = [3,4,5,6], target = 7
        # Output: [0,1]
        # Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

        hashmap = {}
        for i, n in enumerate(nums):
            hashmap[n] = i
        
        print(hashmap)
        for i, n in enumerate(nums):
            complement = target - n
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        return []
            