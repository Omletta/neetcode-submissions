class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = {}

        for num in nums:
            if num not in seen:
                seen[num] = seen.get(num,0) + 1
            else:
                return True

        return False
        