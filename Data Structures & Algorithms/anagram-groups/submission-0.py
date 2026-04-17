class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anas = []
        groups = []
        
        for word in strs:
            if sorted(word) not in anas:
                anas.append(sorted(word))
        
        for i in range(len(anas)):
            group = []
            for word in strs:
                if sorted(word) == anas[i]:
                    group.append(word)
            groups.append(group)
        
        return groups




        