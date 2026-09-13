class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_to_index = {}
        solutions = set()

        for first in range(len(nums)):
            if nums[first] in num_to_index.keys():
                num_to_index[nums[first]].add(first)
            else:
                num_to_index[nums[first]] = set([first])

            for second in range(first+1, len(nums)):
                complement = 0 - nums[first] - nums[second]
                if complement in num_to_index:
                    index_set = num_to_index[complement]
                    if first in index_set and second in index_set and len(index_set) == 2:
                        continue
                    elif (first in index_set or second in index_set) and len(index_set) == 1:
                        continue
                    else:
                        potential = [nums[first], nums[second], complement]
                        potential.sort()
                        potential = tuple(potential)
                        if potential not in solutions:
                            solutions.add(potential)
                            
        return [item for item in solutions]