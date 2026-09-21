class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        min_speed = right

        while left <= right:
            r = (left + right) // 2

            hours = 0

            for pile in piles:
                hours += (pile + r - 1) // r

            if hours <= h:
                min_speed = r
                right = r - 1
            else:
                left = r + 1

        return min_speed