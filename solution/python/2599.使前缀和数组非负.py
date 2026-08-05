"""2599. 使前缀和数组非负"""


class Solution:
    def makePrefSumNonNegative(self, nums: list[int]) -> int:
        import heapq

        heap = []
        answer = 0
        total = 0
        for value in nums:
            total += value
            heapq.heappush(heap, value)
            if total < 0:
                total -= heapq.heappop(heap)
                answer += 1
        return answer


if __name__ == "__main__":
    test_cases = [(([-4, -3, 2],), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().makePrefSumNonNegative(*args) == expected
