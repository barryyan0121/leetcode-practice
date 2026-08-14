"""3237. Alt 和 Tab 模拟"""


class Solution:
    def simulationResult(self, windows: list[int], queries: list[int]) -> list[int]:
        seen = set()
        answer = []
        for window in reversed(queries):
            if window not in seen:
                seen.add(window)
                answer.append(window)
        answer.extend(window for window in windows if window not in seen)
        return answer


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3], [3, 3, 2]), [2, 3, 1]),
        (([1, 4, 2, 3], [4, 1, 3]), [3, 1, 4, 2]),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().simulationResult(*args) == expected
