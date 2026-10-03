class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        reverse_list = sorted(nums,reverse= True)

        return reverse_list[k-1]        