class Solution:
    def minCostToEqualizeArray(self, nums: list[int], cost1: int, cost2: int) -> int:
        mod = 10**9 + 7
        if len(nums) == 1:
            return 0
        minimum = min(nums)
        maximum = max(nums)
        total_sum = sum(nums)
        if cost2 >= 2 * cost1 or len(nums) < 3:
            return (maximum * len(nums) - total_sum) * cost1 % mod
        answer = float("inf")
        for target in range(maximum, 2 * maximum):
            total = target * len(nums) - total_sum
            largest = target - minimum
            pairs = min(total // 2, total - largest)
            value = (total - 2 * pairs) * cost1 + pairs * cost2
            answer = min(answer, value)
        return answer % mod


if __name__ == "__main__":
    test_cases = [
        ([4, 1], 5, 10, 15),
        ([2, 3, 3, 3, 5], 2, 1, 6),
        ([3, 5, 3], 1, 3, 4),
        ([1, 14, 14, 15], 2, 1, 20),
    ]
    for _, (nums, cost1, cost2, expected) in enumerate(test_cases):
        assert Solution().minCostToEqualizeArray(nums, cost1, cost2) == expected
