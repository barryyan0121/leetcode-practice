"""2269. 找到一个数字的 K 美丽值"""


class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        text = str(num)
        return sum(
            value and num % value == 0
            for i in range(len(text) - k + 1)
            if (value := int(text[i : i + k]))
        )

if __name__ == "__main__":
    assert Solution().divisorSubstrings(240, 2) == 2
