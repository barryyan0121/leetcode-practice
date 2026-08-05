"""3747. 统计移除零后不同整数的数目"""


class Solution:
    def countDistinct(self, n: int) -> int:
        digits = str(n)
        answer = sum(9**length for length in range(1, len(digits)))
        for index, digit in enumerate(digits):
            value = int(digit)
            if value == 0:
                break
            answer += (value - 1) * 9 ** (len(digits) - index - 1)
            if index == len(digits) - 1:
                answer += 1
        return answer


if __name__ == "__main__":
    test_cases = [((10,), 9), ((3,), 3)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countDistinct(*args) == expected
