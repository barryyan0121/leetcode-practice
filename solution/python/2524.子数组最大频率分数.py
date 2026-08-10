"""2524. 子数组最大频率分数"""


class Solution:
    def maxFrequencyScore(self, nums: list[int], k: int) -> int:
        mod = 10**9 + 7
        score = 0
        answer = 0
        counts = {}
        powers = {}
        inverses = {}

        def add(value: int) -> None:
            nonlocal score
            count = counts.get(value, 0)
            old = powers.get(value, 1)
            new = old * value % mod
            score = (score + new - (old if count else 0)) % mod
            counts[value] = count + 1
            powers[value] = new

        def remove(value: int) -> None:
            nonlocal score
            old = powers[value]
            count = counts[value]
            inverse = inverses.setdefault(value, pow(value, mod - 2, mod))
            new = old * inverse % mod
            score = (score + (new if count > 1 else 0) - old) % mod
            counts[value] = count - 1
            powers[value] = new

        for index, value in enumerate(nums):
            add(value)
            if index >= k:
                remove(nums[index - k])
            if index >= k - 1:
                answer = max(answer, score)
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 1, 1, 2, 1, 2], 3), 5), (([1] * 6, 4), 1)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxFrequencyScore(*args) == expected
