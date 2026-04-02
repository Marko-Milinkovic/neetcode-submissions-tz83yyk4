class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1
        
        # Step 2: Sort by frequency (descending) and take top k
        sorted_items = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        
        # Step 3: Extract just the numbers (not the counts)
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])
        
        return result