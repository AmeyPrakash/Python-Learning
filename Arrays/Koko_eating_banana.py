from typing import List

class Solution:
    def hours(self, arr, n, speed): # calculated hours needed
        h = 0
        for i in range(n):
            h = h+arr[i] // speed
            if arr[i] % speed != 0:
                h = h+1
        return h

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        n = len(piles)
        low = 1
        high = max(piles)
        res = -1
        
        while low <= high:

            guess = low+(high-low) // 2
            hour = self.hours(piles, n, guess)

            if hour > h: #compare hours needed and coming back of guard

                low = guess+1
            else:
                res = guess
                high = guess - 1

        return res 
