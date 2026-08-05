"""2548. 填满背包的最大价格"""


class Solution:
    def maxPrice(self, items: list[list[int]], capacity: int) -> float:
        items.sort(key=lambda item: item[0] / item[1], reverse=True)
        answer = 0.0
        for price, weight in items:
            taken = min(capacity, weight)
            answer += price * taken / weight
            capacity -= taken
            if capacity == 0:
                return answer
        return -1.0


if __name__ == "__main__":
    test_cases = [(([[50, 1], [10, 8]], 5), 55.0)]
    for _, (args, expected) in enumerate(test_cases):
        assert abs(Solution().maxPrice(*args) - expected) < 1e-9
