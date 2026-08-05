"""3929. 最小分割分数 II"""


class Solution:
    def minPartitionScore(self, nums: list[int], k: int) -> int:
        pelunaxori = nums
        prefix = [0]
        for value in pelunaxori:
            prefix.append(prefix[-1] + value)

        def evaluate(penalty: int) -> tuple[int, int]:
            # Work with twice the score to keep every value integral.
            hull = [(0, 0, 0)]  # slope, intercept, number of parts
            head = 0
            dp = 0
            parts = 0
            for index in range(1, len(prefix)):
                total = prefix[index]
                while head + 1 < len(hull):
                    current = hull[head]
                    following = hull[head + 1]
                    current_value = current[0] * total + current[1]
                    following_value = following[0] * total + following[1]
                    if following_value < current_value or (
                        following_value == current_value and following[2] > current[2]
                    ):
                        head += 1
                    else:
                        break
                slope, intercept, previous_parts = hull[head]
                dp = total * total + total + slope * total + intercept + 2 * penalty
                parts = previous_parts + 1

                line = (-2 * total, dp + total * total - total, parts)
                while len(hull) >= head + 2:
                    first = hull[-2]
                    second = hull[-1]
                    if (second[1] - first[1]) * (second[0] - line[0]) >= (
                        line[1] - second[1]
                    ) * (first[0] - second[0]):
                        hull.pop()
                    else:
                        break
                hull.append(line)
            return dp, parts

        low, high = 0, (prefix[-1] * (prefix[-1] + 1)) // 2
        while low < high:
            penalty = (low + high + 1) // 2
            _, parts = evaluate(penalty)
            if parts >= k:
                low = penalty
            else:
                high = penalty - 1
        score_twice, _ = evaluate(low)
        return (score_twice - 2 * low * k) // 2


if __name__ == "__main__":
    test_cases = [
        (([5, 1, 2, 1], 2), 25),
        (([1, 2, 3, 4], 1), 55),
        (([1, 1, 1], 3), 3),
        (([5, 6, 5, 6], 3), 102),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minPartitionScore(*args) == expected
