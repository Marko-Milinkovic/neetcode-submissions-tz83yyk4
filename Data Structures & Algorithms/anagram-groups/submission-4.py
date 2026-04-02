class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dictionary = defaultdict(list)

        for s in strs:
            temp = ''.join(sorted(s))

            dictionary[temp].append(s)
        
        return list(dictionary.values())

