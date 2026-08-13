"""3228. 将 1 移动到末尾的最大操作次数"""


class Solution:
    def maxOperations(self, s: str) -> int:
        ones = answer = 0
        for index, char in enumerate(s):
            if char == "0" and index + 1 < len(s) and s[index + 1] == "1":
                answer += ones
            elif char == "1":
                ones += 1
        return answer


if __name__ == "__main__":
    test_cases = [
        ("1001101", 4),
        ("00111", 0),
    ]
    for index, (s, expected) in enumerate(test_cases):
        assert Solution().maxOperations(s) == expected, index
