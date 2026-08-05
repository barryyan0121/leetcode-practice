from collections import defaultdict


class Solution:
    def maxProfit(self, workers: list[int], tasks: list[list[int]]) -> int:
        profits = defaultdict(list)
        for skill, profit in tasks:
            profits[skill].append(profit)
        workers_by_skill = defaultdict(int)
        for worker in workers:
            workers_by_skill[worker] += 1

        answer = 0
        extra = 0
        for skill, values in profits.items():
            values.sort(reverse=True)
            used = min(workers_by_skill[skill], len(values))
            answer += sum(values[:used])
            if used < len(values):
                extra = max(extra, values[used])
        return answer + extra


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3, 4, 5], [[1, 100], [2, 400], [3, 100], [3, 400]]), 1000),
        (([10, 10000, 100000000], [[1, 100]]), 100),
        (([7], [[3, 3], [3, 3]]), 3),
    ]
    for _, ((workers, tasks), expected) in enumerate(test_cases):
        assert Solution().maxProfit(workers, tasks) == expected
