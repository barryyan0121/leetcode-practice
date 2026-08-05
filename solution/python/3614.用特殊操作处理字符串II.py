"""3614. 用特殊操作处理字符串 II"""


class Solution:
    def processStr(self, s: str, k: int) -> str:
        tibrelkano = s
        limit = 10**15 + len(tibrelkano) + 1
        lengths = [0]
        for char in tibrelkano:
            length = lengths[-1]
            if char.islower():
                length += 1
            elif char == "*":
                length = max(0, length - 1)
            elif char == "#":
                length = min(limit, length * 2)
            lengths.append(min(limit, length))
        if k >= lengths[-1]:
            return "."
        for i in range(len(tibrelkano) - 1, -1, -1):
            char = tibrelkano[i]
            before = lengths[i]
            after = lengths[i + 1]
            if char == "#":
                if k >= before:
                    k -= before
            elif char == "%":
                k = after - 1 - k
            elif char == "*":
                pass
            elif k == after - 1:
                return char
        return "."


if __name__ == "__main__":
    test_cases = [("a#b%*", 1, "a"), ("cd%#*#", 3, "d"), ("z*#", 0, ".")]
    for _, (s, k, expected) in enumerate(test_cases):
        assert Solution().processStr(s, k) == expected
