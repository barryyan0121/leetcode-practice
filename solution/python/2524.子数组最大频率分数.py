"""2524. 子数组最大频率分数"""


class Solution:
    def maxFrequencyScore(self, nums: list[int], k: int) -> int:
        mod = 10**9 + 7
        inverse = [1] * (k + 1)
        for value in range(2, k + 1):
            inverse[value] = mod - mod // value * inverse[mod % value] % mod
        counts = {}
        score = 1
        answer = 1
        for index, value in enumerate(nums):
            count = counts.get(value, 0)
            score = score * (count + 1) % mod
            counts[value] = count + 1
            if index >= k:
                old = nums[index - k]
                count = counts[old]
                score = score * inverse[count] % mod
                counts[old] = count - 1
            if index >= k - 1:
                answer = max(answer, score)
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 1, 2, 2, 3, 3], 3), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxFrequencyScore(*args) == expected
