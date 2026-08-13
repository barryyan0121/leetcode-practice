"""3861. 容量最小的箱子"""


class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        answer = -1
        for index, value in enumerate(capacity):
            if value < itemSize:
                continue
            if answer == -1 or value < capacity[answer]:
                answer = index
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 5, 3, 7], 3), 2), (([3, 5, 4, 3], 2), 0), (([4], 5), -1)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimumIndex(*args) == expected
