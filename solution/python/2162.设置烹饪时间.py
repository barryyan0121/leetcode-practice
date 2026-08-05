"""2162. 设置烹饪时间"""


class Solution:
    def minCostSetTime(
        self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int
    ) -> int:
        answer = float("inf")
        for minutes in range(100):
            seconds = targetSeconds - minutes * 60
            if not 0 <= seconds <= 99:
                continue
            text = f"{minutes:02d}{seconds:02d}".lstrip("0") or "0"
            cost = 0
            current = startAt
            for char in text:
                digit = int(char)
                if digit != current:
                    cost += moveCost
                    current = digit
                cost += pushCost
            answer = min(answer, cost)
        return answer


if __name__ == "__main__":
    test_cases = [((1, 2, 1, 600), 6)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minCostSetTime(*args) == expected
