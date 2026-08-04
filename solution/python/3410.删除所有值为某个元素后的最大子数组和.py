import heapq


class Solution:
    def maxSubarraySum(self, nums: list[int]) -> int:
        value_to_index = {value: index for index, value in enumerate(set(nums))}
        size = len(value_to_index) + 1
        raw = [0] * size
        versions = [0] * size
        heap = [(0, index, 0) for index in range(size)]
        heapq.heapify(heap)
        floor = 0
        offset = 0
        answer = max(nums)

        for value in nums:
            index = value_to_index[value]
            old_value = max(raw[index], floor) + offset
            offset += value
            floor = max(floor, -offset)
            raw[index] = old_value - offset
            versions[index] += 1
            heapq.heappush(heap, (-raw[index], index, versions[index]))
            while heap[0][2] != versions[heap[0][1]]:
                heapq.heappop(heap)
            current = max(-heap[0][0], floor) + offset
            if current > 0:
                answer = max(answer, current)
        return answer


if __name__ == "__main__":
    test_cases = [
        (([-3, 2, -2, -1, 3, -2, 3],), 7),
        (([1, 2, 3, 4],), 10),
        (([-2],), -2),
    ]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().maxSubarraySum(nums) == expected
