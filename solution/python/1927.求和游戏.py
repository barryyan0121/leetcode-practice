"""1927. 求和游戏"""


class Solution:
    def sumGame(self, num: str) -> bool:
        half = len(num) // 2
        left_sum = sum(int(char) for char in num[:half] if char != "?")
        right_sum = sum(int(char) for char in num[half:] if char != "?")
        left_unknown = num[:half].count("?")
        right_unknown = num[half:].count("?")
        difference = left_sum - right_sum
        return difference != 4.5 * (right_unknown - left_unknown)


if __name__ == "__main__":
    assert not Solution().sumGame("5023")
    assert Solution().sumGame("25??")
