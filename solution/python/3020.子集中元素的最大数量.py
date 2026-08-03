from collections import Counter


class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        counts = Counter(nums)
        answer = counts[1] if counts[1] % 2 else max(0, counts[1] - 1)
        for value, count in counts.items():
            if value == 1 or count < 2:
                continue
            length = 1
            while True:
                squared = value * value
                if squared not in counts:
                    break
                length += 1
                value = squared
                if counts[value] < 2:
                    break
            answer = max(answer, 2 * length - 1)
        return max(answer, 1)


if __name__ == "__main__":
    test_cases = [([5, 4, 1, 2, 2], 3), ([1, 3, 2, 4], 1)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().maximumLength(nums) == expected
