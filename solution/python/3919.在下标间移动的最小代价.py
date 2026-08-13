"""3919. 在下标间移动的最小代价"""


class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        lomviretas = nums
        n = len(lomviretas)
        closest = [0] * n
        closest[0] = 1
        closest[-1] = n - 2
        for index in range(1, n - 1):
            left_gap = lomviretas[index] - lomviretas[index - 1]
            right_gap = lomviretas[index + 1] - lomviretas[index]
            closest[index] = index - 1 if left_gap <= right_gap else index + 1

        forward = [0] * n
        for index in range(n - 1):
            forward[index + 1] = forward[index] + (
                1
                if closest[index] == index + 1
                else lomviretas[index + 1] - lomviretas[index]
            )

        backward = [0] * n
        for index in range(n - 1, 0, -1):
            backward[index - 1] = backward[index] + (
                1
                if closest[index] == index - 1
                else lomviretas[index] - lomviretas[index - 1]
            )

        answer = []
        for left, right in queries:
            if left <= right:
                answer.append(forward[right] - forward[left])
            else:
                answer.append(backward[right] - backward[left])
        return answer


if __name__ == "__main__":
    test_cases = [
        (((-5, -2, 3), [[0, 2], [2, 0], [1, 2]]), [6, 2, 5]),
        (((0, 2, 3, 9), [[3, 0], [1, 2], [2, 0]]), [4, 1, 3]),
        (((1, 4), [[0, 1], [1, 0], [0, 0]]), [1, 1, 0]),
    ]
    for _, (args, expected) in enumerate(test_cases):
        nums_arg, queries_arg = args
        assert Solution().minCost(list(nums_arg), queries_arg) == expected
