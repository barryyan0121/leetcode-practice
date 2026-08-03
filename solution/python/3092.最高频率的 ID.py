import heapq


class Solution:
    def mostFrequentIDs(self, nums: list[int], freq: list[int]) -> list[int]:
        counts = {}
        heap = []
        answer = []
        for number, change in zip(nums, freq):
            counts[number] = counts.get(number, 0) + change
            heapq.heappush(heap, (-counts[number], number))
            while heap and -heap[0][0] != counts.get(heap[0][1], 0):
                heapq.heappop(heap)
            answer.append(-heap[0][0] if heap else 0)
        return answer


if __name__ == "__main__":
    test_cases = [
        (([2, 3, 2, 1], [3, 2, -3, 1]), [3, 3, 2, 2]),
        (([5, 5, 3], [2, -2, 1]), [2, 0, 1]),
    ]
    for _, ((nums, freq), expected) in enumerate(test_cases):
        assert Solution().mostFrequentIDs(nums, freq) == expected
