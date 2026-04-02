from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        
        for s in strs:
            signature = ''.join(sorted(s))
            anagram_groups[signature].append(s)
        
        return list(anagram_groups.values())