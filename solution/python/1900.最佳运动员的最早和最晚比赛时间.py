"""1900. 最佳运动员的最早和最晚比赛时间"""

from functools import cache


class Solution:
    def earliestAndLatest(
        self, n: int, firstPlayer: int, secondPlayer: int
    ) -> list[int]:
        @cache
        def dfs(left: int, right: int, count: int) -> tuple[int, int]:
            if left + right == count - 1:
                return 1, 1
            earliest, latest = 10**9, -(10**9)
            half = count >> 1
            for mask in range(1 << half):
                winners = [False] * count
                for index in range(half):
                    if mask >> index & 1:
                        winners[index] = True
                    else:
                        winners[count - 1 - index] = True
                if count & 1:
                    winners[half] = True
                winners[count - 1 - left] = winners[count - 1 - right] = False
                winners[left] = winners[right] = True
                new_left = new_right = new_count = 0
                for index in range(count):
                    if index == left:
                        new_left = new_count
                    if index == right:
                        new_right = new_count
                    if winners[index]:
                        new_count += 1
                next_earliest, next_latest = dfs(new_left, new_right, new_count)
                earliest = min(earliest, next_earliest + 1)
                latest = max(latest, next_latest + 1)
            return earliest, latest

        return list(dfs(firstPlayer - 1, secondPlayer - 1, n))


if __name__ == "__main__":
    test_cases = [((11, 2, 4), [3, 4]), ((5, 1, 5), [1, 1])]
    for args, expected in test_cases:
        assert Solution().earliestAndLatest(*args) == expected
