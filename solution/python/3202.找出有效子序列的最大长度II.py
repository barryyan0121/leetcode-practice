class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        lengths = [[0] * k for _ in range(k)]
        answer = 1
        for number in nums:
            remainder = number % k
            for previous in range(k):
                candidate = lengths[remainder][previous] + 1
                if candidate > lengths[previous][remainder]:
                    lengths[previous][remainder] = candidate
                    answer = max(answer, candidate)
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 2, 3, 4, 5], 2), 5), (([1, 4, 2, 3, 1, 4], 3), 4)]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().maximumLength(nums, k) == expected
