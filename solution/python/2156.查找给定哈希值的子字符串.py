"""2156. 查找给定哈希值的子字符串"""


class Solution:
    def subStrHash(
        self, s: str, power: int, modulo: int, k: int, hashValue: int
    ) -> str:
        current = 0
        power_k = pow(power, k, modulo)
        answer = 0
        for index in range(len(s) - 1, -1, -1):
            current = (current * power + ord(s[index]) - 96) % modulo
            if index + k < len(s):
                current = (current - (ord(s[index + k]) - 96) * power_k) % modulo
            if index + k <= len(s) and current == hashValue:
                answer = index
        return s[answer : answer + k]


if __name__ == "__main__":
    test_cases = [(("leetcode", 7, 20, 2, 0), "ee")]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().subStrHash(*args) == expected
