class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # [1,4][4,6][7,8][10,10]
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        last_time = 0 # holds the arrival time of the slowest fleet (the fleet currently in front of everything behind it)
        

        for pos, spd in cars:

            time = (target - pos) / spd

            if time > last_time:
                fleets += 1
                last_time = time
            
        return fleets