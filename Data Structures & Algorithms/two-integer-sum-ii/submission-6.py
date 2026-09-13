class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        solution = []
        
        for first in range(len(numbers)):
            if numbers[first] == 0 and numbers[first+1] == 0 and target != 0:
                continue
            for second in range(first+1, len(numbers)):
                if numbers[first] + numbers[second] > target:
                    break
                if numbers[first] + numbers[second] == target:
                    solution.append(first+1)
                    solution.append(second+1)
                    return solution

        return solution