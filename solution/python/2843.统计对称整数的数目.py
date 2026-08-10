"""2843. 统计对称整数的数目"""


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        answer = 0
        for number in range(low, high + 1):
            digits = str(number)
            half = len(digits) // 2
            if len(digits) % 2 == 0 and sum(map(int, digits[:half])) == sum(
                map(int, digits[half:])
            ):
                answer += 1
        return answer


if __name__ == "__main__":
    assert Solution().countSymmetricIntegers(1, 100) == 9
