import heapq


class Solution:
    def unmarkedSumArray(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        marked = [False] * len(nums)
        heap = [(value, index) for index, value in enumerate(nums)]
        heapq.heapify(heap)
        remaining = sum(nums)
        answer = []
        for index, count in queries:
            if not marked[index]:
                marked[index] = True
                remaining -= nums[index]
            for _ in range(count):
                while heap and marked[heap[0][1]]:
                    heapq.heappop(heap)
                if not heap:
                    break
                _, smallest_index = heapq.heappop(heap)
                marked[smallest_index] = True
                remaining -= nums[smallest_index]
            answer.append(remaining)
        return answer


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 2, 1, 2, 3, 1], [[1, 2], [3, 3], [4, 2]]), [8, 3, 0]),
        (([1, 4, 2, 3], [[0, 1]]), [7]),
    ]
    for _, ((nums, queries), expected) in enumerate(test_cases):
        assert Solution().unmarkedSumArray(nums, queries) == expected
