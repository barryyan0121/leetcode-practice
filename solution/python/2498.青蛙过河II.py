"""2498. 青蛙过河 II"""


class Solution:
    def maxJump(self, stones: list[int]) -> int:
        if len(stones) == 2:
            return stones[1] - stones[0]
        return max(
            stones[index + 2] - stones[index] for index in range(len(stones) - 2)
        )


if __name__ == "__main__":
    assert Solution().maxJump([0, 2, 5, 6, 7]) == 5
