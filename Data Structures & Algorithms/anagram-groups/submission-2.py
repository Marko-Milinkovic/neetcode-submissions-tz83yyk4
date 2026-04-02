from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        log = defaultdict(list)

        for s in strs:
            temp = ''.join(sorted(s))
            log[temp].append(s)
        
        return list(log.values())
