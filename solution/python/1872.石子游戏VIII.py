"""1872. 石子游戏 VIII"""


class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        prefix = []
        total = 0
        for value in stones:
            total += value
            prefix.append(total)
        answer = prefix[-1]
        for index in range(len(stones) - 2, 0, -1):
            answer = max(answer, prefix[index] - answer)
        return answer


if __name__ == "__main__":
    test_cases = [([-1, 2, -3, 4, -5], 5), ([7, -6, 5, 10, 5, -2, -6], 13)]
    for _, (stones, expected) in enumerate(test_cases):
        assert Solution().stoneGameVIII(stones) == expected
