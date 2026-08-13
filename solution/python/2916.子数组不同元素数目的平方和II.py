class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        sums = [0] * (4 * n)
        squares = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, left, right, value):
            length = right - left + 1
            squares[node] = (
                squares[node] + 2 * value * sums[node] + value * value * length
            ) % mod
            sums[node] = (sums[node] + value * length) % mod
            lazy[node] += value

        def push(node, left, right):
            if lazy[node] and left != right:
                middle = (left + right) // 2
                apply(node * 2, left, middle, lazy[node])
                apply(node * 2 + 1, middle + 1, right, lazy[node])
                lazy[node] = 0

        def update(node, left, right, start, end):
            if start <= left and right <= end:
                apply(node, left, right, 1)
                return
            push(node, left, right)
            middle = (left + right) // 2
            if start <= middle:
                update(node * 2, left, middle, start, end)
            if end > middle:
                update(node * 2 + 1, middle + 1, right, start, end)
            sums[node] = (sums[node * 2] + sums[node * 2 + 1]) % mod
            squares[node] = (squares[node * 2] + squares[node * 2 + 1]) % mod

        last = {}
        answer = 0
        for right, value in enumerate(nums):
            update(1, 0, n - 1, last.get(value, -1) + 1, right)
            last[value] = right
            answer = (answer + squares[1]) % mod
        return answer


if __name__ == "__main__":
    assert Solution().sumCounts([1, 2, 1]) == 15
