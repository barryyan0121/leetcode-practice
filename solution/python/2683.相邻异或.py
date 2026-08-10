"""2683. 相邻异或"""


class Solution:
    def doesValidArrayExist(self, derived: list[int]) -> bool:
        return not (sum(derived) & 1)


if __name__ == "__main__":
    assert Solution().doesValidArrayExist([1, 1, 0])
