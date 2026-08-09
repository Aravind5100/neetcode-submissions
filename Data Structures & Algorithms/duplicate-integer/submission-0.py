class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Sort in-place (don't reassign to the return value)
        nums.sort()
        n = len(nums)
        i = 0
        
        # Loop through array, checking adjacent elements
        while i < n - 1:  # Stop at n-1 to avoid index out of bounds
            if nums[i] == nums[i + 1]:
                return True  # Capitalized True
            i += 1
        
        return False  # Capitalized False