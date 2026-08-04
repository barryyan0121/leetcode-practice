import heapq


class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        heap = [(value, index) for index, value in enumerate(nums)]
        heapq.heapify(heap)
        for _ in range(k):
            value, index = heapq.heappop(heap)
            value *= multiplier
            nums[index] = value
            heapq.heappush(heap, (value, index))
        return nums


if __name__ == "__main__":
    test_cases = [
        (([2, 1, 3, 5, 6], 5, 2), [8, 4, 6, 5, 6]),
        (([1, 2], 3, 4), [16, 8]),
    ]
    for _, ((nums, k, multiplier), expected) in enumerate(test_cases):
        assert Solution().getFinalState(nums, k, multiplier) == expected
