"""2602. 使数组元素全部相等的最少操作次数"""

from bisect import bisect_left, bisect_right


class Solution:
    def minOperations(self, nums: list[int], queries: list[int]) -> list[int]:
        nums.sort()
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)
        total = prefix[-1]
        answer = []
        for query in queries:
            left = bisect_left(nums, query)
            right = bisect_right(nums, query)
            answer.append(
                query * left
                - prefix[left]
                + total
                - prefix[right]
                - query * (len(nums) - right)
            )
        return answer


if __name__ == "__main__":
    test_cases = [(([3, 1, 6, 8], [1, 5]), [14, 10])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minOperations(*args) == expected
