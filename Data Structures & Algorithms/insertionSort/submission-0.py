# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        output = []
        for i in range(len(pairs)):
            if i == 0:
                output.append(pairs[:])
                continue
            j = i-1
            while j >= 0 and pairs[i].key < pairs[j].key:
                j -= 1
            if j < 0 and pairs[i].key >= pairs[j+1].key:
                continue
            temp = pairs[i]
            sorted_part = pairs[:j+1]+[temp]+pairs[j+1:i]
            pairs = sorted_part + pairs[i+1:]
            output.append(pairs[:])
        return output
        