class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles) # coco can eat at rate from 1 to max(piles) [worst case] [we binary search rates]
                             # for each rate, we check if hours <= target h
                             # if it is, try binary searching even smaller eating rate
                             # if current rate doesnt allow to eat all bananas for h given hours, try binary searching higher k
        res = r

        while l<= r:

            k = (l + r) // 2
            
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        
        return res
