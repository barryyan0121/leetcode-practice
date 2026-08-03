class Solution:
    def minimumValueSum(self, nums: list[int], andValues: list[int]) -> int:
        infinity = 10**18
        previous = [infinity] * (len(nums) + 1)
        previous[0] = 0

        for target in andValues:
            current = [infinity] * (len(nums) + 1)
            groups = []
            for end in range(1, len(nums) + 1):
                candidates = [(value & nums[end - 1], cost) for value, cost in groups]
                if previous[end - 1] < infinity:
                    candidates.append((nums[end - 1], previous[end - 1]))

                merged = []
                for value, cost in candidates:
                    if merged and merged[-1][0] == value:
                        merged[-1] = (value, min(merged[-1][1], cost))
                    else:
                        merged.append((value, cost))
                groups = merged
                for value, cost in groups:
                    if value == target:
                        current[end] = cost + nums[end - 1]
                        break
            previous = current

        answer = previous[-1]
        return -1 if answer == infinity else answer


if __name__ == "__main__":
    test_cases = [
        ([1, 4, 3, 3, 2], [0, 3, 3, 2], 12),
        ([2, 3, 5, 7, 7, 7, 5], [0, 7, 5], 17),
        ([1, 2, 3, 4], [2], -1),
    ]
    for _, (nums, and_values, expected) in enumerate(test_cases):
        assert Solution().minimumValueSum(nums, and_values) == expected
