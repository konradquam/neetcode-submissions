class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        output = []
        for num in nums:
            freq[num] += 1
        sorted_list = sorted(freq.items(), key = lambda i: i[1], reverse=True)
        for item, frequency in sorted_list[:k]:
            output.append(item)

        return output
        