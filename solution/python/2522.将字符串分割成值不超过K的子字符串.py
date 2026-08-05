"""2522. 将字符串分割成值不超过 K 的子字符串"""


class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        answer = 1
        current = 0
        for char in s:
            digit = int(char)
            if digit > k:
                return -1
            if current * 10 + digit > k:
                answer += 1
                current = digit
            else:
                current = current * 10 + digit
        return answer


if __name__ == "__main__":
    test_cases = [(("165462", 60), 4)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimumPartition(*args) == expected
