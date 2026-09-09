class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        def binary_search(l, r):
            mid = (l + r) // 2
            if mid == l:
                if nums[l] < nums[r]:
                    return nums[l]
                else:
                    return nums[r]
            if nums[mid] > nums[r]:
                return binary_search(mid, r)
            else:
                return binary_search(l, mid)
        return binary_search(l, r)
            

        