"""1849. 将字符串拆分为递减的连续值"""


class Solution:
    def splitString(self, s: str) -> bool:
        length = len(s)

        def search(position: int, previous: int, parts: int) -> bool:
            if position == length:
                return parts >= 2
            for end in range(position + 1, length + 1):
                piece = s[position:end]
                value = int(piece)
                if not parts or value == previous - 1:
                    if search(end, value, parts + 1):
                        return True
            return False

        return search(0, 0, 0)


if __name__ == "__main__":
    test_cases = [("1234", False), ("050043", True), ("9080701", False)]
    for _, (s, expected) in enumerate(test_cases):
        assert Solution().splitString(s) == expected
