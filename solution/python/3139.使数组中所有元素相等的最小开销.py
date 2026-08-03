class Solution:
    def minCostToEqualizeArray(self, nums: list[int], cost1: int, cost2: int) -> int:
        mod = 10**9 + 7
        minimum = min(nums)
        maximum = max(nums)
        total_sum = sum(nums)
        if cost2 >= 2 * cost1:
            return (maximum * len(nums) - total_sum) * cost1 % mod

        balance = (total_sum - 2 * minimum + len(nums) - 3) // (len(nums) - 2)
        start = max(maximum, balance)
        answer = float("inf")
        for target in {maximum, start, start + 1}:
            total = target * len(nums) - total_sum
            largest = target - minimum
            other = total - largest
            if largest > other:
                value = other * cost2 + (largest - other) * cost1
            else:
                value = (total // 2) * cost2 + (total % 2) * cost1
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
