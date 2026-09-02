class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_list = []

        for s in strs:
            sorted_list.append(''.join(sorted(s)))
        
        
        seen_ana = {}

        for i, s in enumerate(sorted_list):
            if s in seen_ana:
                seen_ana[s] = seen_ana[s] + [i]
            else:
                seen_ana[s] = [i]

        ans = []
        for k, v in seen_ana.items():
            temp = []
            for i in v:
                temp.append(strs[i])
            ans.append(temp)

        return ans