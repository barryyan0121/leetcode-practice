"""2607. 使子数组元素和相等"""


class Solution:
    def makeSubKSumEqual(self, arr: list[int], k: int) -> int:
        from math import gcd

        step = gcd(len(arr), k)
        answer = 0
        for start in range(step):
            values = sorted(arr[start::step])
            median = values[len(values) // 2]
            answer += sum(abs(value - median) for value in values)
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 4, 1, 3], 2), 1)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().makeSubKSumEqual(*args) == expected
