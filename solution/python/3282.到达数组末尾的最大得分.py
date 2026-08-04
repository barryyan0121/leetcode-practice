class Solution:
    def findMaximumScore(self, nums: list[int]) -> int:
        n = len(nums)
        lines = [None] * (4 * n)

        def value(line: tuple[int, int], x: int) -> int:
            return line[0] * x + line[1]

        def add(line: tuple[int, int], node: int, left: int, right: int) -> None:
            if lines[node] is None:
                lines[node] = line
                return
            middle = (left + right) // 2
            current = lines[node]
            if value(line, middle) > value(current, middle):
                lines[node], line = line, current
                current = lines[node]
            if left == right:
                return
            if (value(line, left) > value(current, left)) != (
                value(line, middle) > value(current, middle)
            ):
                add(line, node * 2, left, middle)
            else:
                add(line, node * 2 + 1, middle + 1, right)

        def query(x: int, node: int, left: int, right: int) -> int:
            result = value(lines[node], x) if lines[node] is not None else -(10**30)
            if left == right:
                return result
            middle = (left + right) // 2
            if x <= middle:
                return max(result, query(x, node * 2, left, middle))
            return max(result, query(x, node * 2 + 1, middle + 1, right))

        add((nums[0], 0), 1, 0, n - 1)
        for index in range(1, n):
            score = query(index, 1, 0, n - 1)
            add((nums[index], score - index * nums[index]), 1, 0, n - 1)
        return query(n - 1, 1, 0, n - 1)


if __name__ == "__main__":
    test_cases = [([1, 3, 1, 5], 7), ([4, 3, 1, 3, 2], 16)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().findMaximumScore(nums) == expected
