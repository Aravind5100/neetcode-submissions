class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hsmp = {}

        for i,n in enumerate(nums):
            hsmp[n]=i

        for i,n in enumerate(nums):
            difference = target-n
            if difference in hsmp:
                if hsmp[difference]!=i:
                    return [i,hsmp[difference]]
        return []
            