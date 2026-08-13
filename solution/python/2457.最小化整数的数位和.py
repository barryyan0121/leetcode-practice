"""2457. 最小化整数的数位和"""


class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        answer = 0
        place = 1
        while sum(map(int, str(n))) > target:
            digit = n // place % 10
            addition = (10 - digit) * place
            n += addition
            answer += addition
            place *= 10
        return answer


if __name__ == "__main__":
    assert Solution().makeIntegerBeautiful(16, 6) == 4
