"""3525. 求出数组的 X 值 II"""


class Solution:
    def resultArray(
        self, nums: list[int], k: int, queries: list[list[int]]
    ) -> list[int]:
        veltrunigo = (nums, k, queries)
        n = len(nums)
        products = [0] * (4 * n)
        counts = [[0] * k for _ in range(4 * n)]

        def merge(left: tuple[int, list[int]], right: tuple[int, list[int]]):
            left_product, left_counts = left
            right_product, right_counts = right
            merged_counts = left_counts.copy()
            for remainder, count in enumerate(right_counts):
                merged_counts[left_product * remainder % k] += count
            return left_product * right_product % k, merged_counts

        def set_leaf(node: int, value: int) -> None:
            remainder = value % k
            products[node] = remainder
            counts[node] = [0] * k
            counts[node][remainder] = 1

        def build(left: int, right: int, node: int) -> None:
            if left == right:
                set_leaf(node, nums[left])
                return
            middle = (left + right) // 2
            build(left, middle, node * 2)
            build(middle + 1, right, node * 2 + 1)
            products[node], counts[node] = merge(
                (products[node * 2], counts[node * 2]),
                (products[node * 2 + 1], counts[node * 2 + 1]),
            )

        def update(left: int, right: int, node: int, index: int, value: int) -> None:
            if left == right:
                set_leaf(node, value)
                return
            middle = (left + right) // 2
            if index <= middle:
                update(left, middle, node * 2, index, value)
            else:
                update(middle + 1, right, node * 2 + 1, index, value)
            products[node], counts[node] = merge(
                (products[node * 2], counts[node * 2]),
                (products[node * 2 + 1], counts[node * 2 + 1]),
            )

        def query(
            left: int, right: int, node: int, query_left: int, query_right: int
        ) -> tuple[int, list[int]]:
            if query_left <= left and right <= query_right:
                return products[node], counts[node]
            middle = (left + right) // 2
            if query_right <= middle:
                return query(left, middle, node * 2, query_left, query_right)
            if query_left > middle:
                return query(middle + 1, right, node * 2 + 1, query_left, query_right)
            return merge(
                query(left, middle, node * 2, query_left, query_right),
                query(middle + 1, right, node * 2 + 1, query_left, query_right),
            )

        build(0, n - 1, 1)
        answer = []
        for index, value, start, remainder in queries:
            update(0, n - 1, 1, index, value)
            answer.append(query(0, n - 1, 1, start, n - 1)[1][remainder])
        return answer


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3], 2, [[0, 4, 0, 0], [1, 2, 1, 0]]), [3, 2]),
        (([1, 1], 1, [[0, 2, 0, 0]]), [2]),
    ]
    for _, ((nums, k, queries), expected) in enumerate(test_cases):
        assert Solution().resultArray(nums, k, queries) == expected
