"""2557. 从一个范围内选择最多整数 II"""


class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        answer = 0
        total = 0
        previous = 0
        for value in sorted(set(x for x in banned if x <= n) | {n + 1}):
            count = value - previous - 1
            low, high = 0, count
            while low < high:
                take_mid = (low + high + 1) // 2
                cost = (2 * (previous + 1) + take_mid - 1) * take_mid // 2
                if cost <= maxSum - total:
                    low = take_mid
                else:
                    high = take_mid - 1
            take = low
            answer += take
            total += (2 * (previous + 1) + take - 1) * take // 2
            if total >= maxSum:
                break
            previous = value
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 6, 5], 5, 6), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxCount(*args) == expected
