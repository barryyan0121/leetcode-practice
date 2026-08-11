class Solution:
    def findMinimumTime(self, strength: list[int]) -> int:
        n = len(strength)
        cost = [[(strength[row] + slot) // (slot + 1) for slot in range(n)] for row in range(n)]
        u = [0] * (n + 1)
        v = [0] * (n + 1)
        p = [0] * (n + 1)
        way = [0] * (n + 1)
        for row in range(1, n + 1):
            p[0] = row
            column = 0
            minimum = [float("inf")] * (n + 1)
            used = [False] * (n + 1)
            while True:
                used[column] = True
                current = p[column]
                delta = float("inf")
                next_column = 0
                for candidate in range(1, n + 1):
                    if not used[candidate]:
                        value = cost[current - 1][candidate - 1] - u[current] - v[candidate]
                        if value < minimum[candidate]:
                            minimum[candidate], way[candidate] = value, column
                        if minimum[candidate] < delta:
                            delta, next_column = minimum[candidate], candidate
                for candidate in range(n + 1):
                    if used[candidate]:
                        u[p[candidate]] += delta
                        v[candidate] -= delta
                    else:
                        minimum[candidate] -= delta
                column = next_column
                if p[column] == 0:
                    break
            while column:
                p[column] = p[way[column]]
                column = way[column]
        return -v[0]


if __name__ == "__main__":
    test_cases = [(([3, 4, 1],), 4), (([2, 5, 4],), 6)]
    for _, ((strength,), expected) in enumerate(test_cases):
        assert Solution().findMinimumTime(strength) == expected
