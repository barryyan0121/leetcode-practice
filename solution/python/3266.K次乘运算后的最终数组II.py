import heapq


class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        modulo = 10**9 + 7
        if multiplier == 1:
            return [value % modulo for value in nums]

        maximum = max(nums)
        heap = [(value, index) for index, value in enumerate(nums)]
        heapq.heapify(heap)
        while k and heap[0][0] * multiplier <= maximum:
            value, index = heapq.heappop(heap)
            heapq.heappush(heap, (value * multiplier, index))
            k -= 1

        heap.sort()
        full_cycles, extra = divmod(k, len(nums))
        for position, (value, index) in enumerate(heap):
            exponent = full_cycles + (position < extra)
            nums[index] = value % modulo * pow(multiplier, exponent, modulo) % modulo
        return nums


if __name__ == "__main__":
    test_cases = [
        (([2, 1, 3, 5, 6], 5, 2), [8, 4, 6, 5, 6]),
        (([100000, 2000], 2, 1000000), [999999307, 999999993]),
        (([1, 2], 3, 4), [16, 8]),
    ]
    for _, ((nums, k, multiplier), expected) in enumerate(test_cases):
        assert Solution().getFinalState(nums, k, multiplier) == expected
