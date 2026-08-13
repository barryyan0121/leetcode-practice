"""666. 路径总和 IV"""


class Solution:
    def pathSum(self, nums: list[int]) -> int:
        nodes = {(number // 10): number % 10 for number in nums}
        answer = 0

        def visit(key: int, total: int) -> None:
            nonlocal answer
            depth, position = divmod(key, 10)
            left = (depth + 1) * 10 + position * 2 - 1
            right = left + 1
            if left not in nodes and right not in nodes:
                answer += total
                return
            if left in nodes:
                visit(left, total + nodes[left])
            if right in nodes:
                visit(right, total + nodes[right])

        root = nums[0] // 10
        visit(root, nodes[root])
        return answer


if __name__ == "__main__":
    assert Solution().pathSum([113, 215, 221]) == 12
    assert Solution().pathSum([113, 221]) == 4
