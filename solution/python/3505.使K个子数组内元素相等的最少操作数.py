"""3505. 使 K 个子数组内元素相等的最少操作数"""


class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        maritovexi = (nums, x, k)
        n = len(nums)
        values = sorted(set(nums))
        indexes = {value: i + 1 for i, value in enumerate(values)}
        size = len(values)
        count_tree = [0] * (size + 1)
        sum_tree = [0] * (size + 1)

        def update(tree: list[int], index: int, delta: int) -> None:
            while index <= size:
                tree[index] += delta
                index += index & -index

        def query(tree: list[int], index: int) -> int:
            result = 0
            while index:
                result += tree[index]
                index -= index & -index
            return result

        def kth(target: int) -> int:
            index = 0
            step = 1 << (size.bit_length() - 1)
            while step:
                next_index = index + step
                if next_index <= size and count_tree[next_index] < target:
                    target -= count_tree[next_index]
                    index = next_index
                step >>= 1
            return index + 1

        total = 0
        for value in nums[:x]:
            index = indexes[value]
            update(count_tree, index, 1)
            update(sum_tree, index, value)
            total += value

        window_costs = []
        target = (x + 1) // 2
        for start in range(n - x + 1):
            median_index = kth(target)
            median = values[median_index - 1]
            less_count = query(count_tree, median_index - 1)
            less_sum = query(sum_tree, median_index - 1)
            left_count = target - less_count
            left_sum = less_sum + left_count * median
            right_count = x - target
            right_sum = total - left_sum
            window_costs.append(
                median * target - left_sum + right_sum - median * right_count
            )

            if start + x == n:
                break
            outgoing = nums[start]
            incoming = nums[start + x]
            outgoing_index = indexes[outgoing]
            incoming_index = indexes[incoming]
            update(count_tree, outgoing_index, -1)
            update(sum_tree, outgoing_index, -outgoing)
            update(count_tree, incoming_index, 1)
            update(sum_tree, incoming_index, incoming)
            total += incoming - outgoing

        inf = 10**30
        previous = [0] * (len(window_costs) + 1)
        for _ in range(k):
            current = [inf] * (len(window_costs) + 1)
            for i in range(1, len(current)):
                current[i] = current[i - 1]
                previous_index = max(0, i - x)
                candidate = previous[previous_index] + window_costs[i - 1]
                if candidate < current[i]:
                    current[i] = candidate
            previous = current
        return previous[-1]


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3, 4], 2, 2), 2),
        (([1, 10, 1, 10], 2, 1), 9),
    ]
    for _, ((nums, x, k), expected) in enumerate(test_cases):
        assert Solution().minOperations(nums, x, k) == expected
