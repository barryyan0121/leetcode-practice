class Solution:
    def beautifulPair(self, nums1, nums2):
        seen = {}
        points = []
        duplicate = [len(nums1), len(nums1)]
        for i, (x, y) in enumerate(zip(nums1, nums2)):
            if (x, y) in seen:
                duplicate = min(duplicate, [seen[x, y], i])
            else:
                seen[x, y] = i
            points.append((x + y, x - y, i))
        if duplicate[0] < len(nums1):
            return duplicate
        points.sort()

        def better(a, b):
            return a if a < b else b

        def solve(items):
            n = len(items)
            if n <= 3:
                best = (10**18, [n, n])
                for i in range(n):
                    for j in range(i + 1, n):
                        a, b = items[i], items[j]
                        best = better(
                            best,
                            (
                                max(abs(a[0] - b[0]), abs(a[1] - b[1])),
                                sorted((a[2], b[2])),
                            ),
                        )
                return best
            mid = n // 2
            left = solve(items[:mid])
            right = solve(items[mid:])
            best = better(left, right)
            strip = sorted(
                (x for x in items if abs(x[0] - items[mid][0]) <= best[0]),
                key=lambda x: x[1],
            )
            for i, a in enumerate(strip):
                for b in strip[i + 1 :]:
                    if b[1] - a[1] > best[0]:
                        break
                    best = better(
                        best,
                        (max(abs(a[0] - b[0]), abs(a[1] - b[1])), sorted((a[2], b[2]))),
                    )
            return best

        return solve(points)[1]


if __name__ == "__main__":
    assert Solution().beautifulPair([1, 3, 5], [2, 4, 6]) == [0, 1]
