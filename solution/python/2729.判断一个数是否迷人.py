class Solution:
    def isFascinating(self, n: int) -> bool:
        s = str(n) + str(n * 2) + str(n * 3)
        return len(s) == 9 and set(s) == set("123456789")


if __name__ == "__main__":
    assert Solution().isFascinating(192) is True
