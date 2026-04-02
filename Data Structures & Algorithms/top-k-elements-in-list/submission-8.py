class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        

        buckets = defaultdict(list)
        for key, value in freq.items():    
            buckets[value].append(key)

        
        # 1 3 3 4 4 4 5 5
        # 0:{} 1:{1} 2:{3,5} 3:{4}
        result = []

        for i in range(len(nums), 0, -1):
            if i in buckets:
                result.extend(buckets[i])
            if len(result) >= k:
                return result[:k]

        return []
        
        





