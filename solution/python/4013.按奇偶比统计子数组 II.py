from bisect import bisect_left


class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        mervanilto = (nums, a, b)
        prefixes = [0]
        current = 0
        for value in nums:
            current += b if value % 2 == 0 else -a
            prefixes.append(current)
        values = sorted(set(prefixes))
        tree = [0] * (len(values) + 1)

        def add(index: int) -> None:
            while index < len(tree):
                tree[index] += 1
                index += index & -index

        def count(index: int) -> int:
            result = 0
            while index:
                result += tree[index]
                index -= index & -index
            return result

        answer = 0
        seen = 0
        for prefix in prefixes:
            rank = bisect_left(values, prefix) + 1
            answer += seen - count(rank - 1)
            add(rank)
            seen += 1
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 2, 1, 2], 3, 2), 7), (([2, 2, 1], 2, 1), 3)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countRatioSubarrays(*args) == expected
