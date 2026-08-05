"""1902. 给定二叉搜索树的插入顺序求深度"""


class Solution:
    def maxDepthBST(self, order: list[int]) -> int:
        values = sorted(order)
        rank = {value: index + 1 for index, value in enumerate(values)}
        tree = [0] * (len(order) + 1)
        depths = [0] * (len(order) + 2)

        def add(index: int) -> None:
            while index < len(tree):
                tree[index] += 1
                index += index & -index

        def prefix(index: int) -> int:
            total = 0
            while index:
                total += tree[index]
                index -= index & -index
            return total

        def kth(target: int) -> int:
            index = 0
            step = 1 << (len(tree) - 1).bit_length() - 1
            while step:
                candidate = index + step
                if candidate < len(tree) and tree[candidate] < target:
                    index = candidate
                    target -= tree[candidate]
                step >>= 1
            return index + 1

        answer = 0
        for value in order:
            current = rank[value]
            before = prefix(current - 1)
            total = prefix(len(order))
            depth = 0
            if before:
                depth = max(depth, depths[kth(before)])
            if total > before:
                depth = max(depth, depths[kth(before + 1)])
            depths[current] = depth + 1
            answer = max(answer, depths[current])
            add(current)
        return answer


if __name__ == "__main__":
    test_cases = [([2, 1, 4, 3], 3), ([1, 2, 3, 4], 4)]
    for _, (order, expected) in enumerate(test_cases):
        assert Solution().maxDepthBST(order) == expected
