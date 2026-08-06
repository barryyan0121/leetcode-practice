# @lc app=leetcode.cn id=2234 lang=python3

from bisect import bisect_left


class Solution:
    def maximumBeauty(
        self, flowers: list[int], newFlowers: int, target: int, full: int, partial: int
    ) -> int:
        flowers = sorted(min(value, target) for value in flowers)
        full_count = sum(value == target for value in flowers)
        flowers = flowers[: len(flowers) - full_count]
        prefix = [0]
        for value in flowers:
            prefix.append(prefix[-1] + value)
        answer = full_count * full
        count = len(flowers)
        for completed in range(count + 1):
            cost = completed * target - (prefix[count] - prefix[count - completed])
            if cost > newFlowers:
                continue
            remaining = newFlowers - cost
            incomplete = count - completed
            if incomplete == 0:
                answer = max(answer, full_count * full + completed * full)
                continue
            low, high = 0, target - 1
            while low <= high:
                level = (low + high) // 2
                index = bisect_left(flowers, level, 0, incomplete)
                needed = level * index - prefix[index]
                if needed <= remaining:
                    low = level + 1
                else:
                    high = level - 1
            answer = max(
                answer,
                (full_count + completed) * full + high * partial,
            )
        return answer


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.maximumBeauty, ([1, 2, 3], 3, 5, 5, 2), 9),
        (solution.maximumBeauty, ([5, 5], 0, 5, 10, 1), 20),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 2234 题 "花园的最大总美丽值" 所有测试用例通过')
