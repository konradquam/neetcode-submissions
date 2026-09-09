class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first = 0
        second = 1

        while first < len(nums) - 1:
            while second < len(nums):
                if nums[first] + nums[second] != target:
                    second += 1
                else:
                    return [first, second]
            first += 1
            second = first + 1
        return