"""2440. 创建价值相同的连通块"""


class Solution:
    def componentValue(self, nums: list[int], edges: list[list[int]]) -> int:
        total = sum(nums)
        children = [[] for _ in nums]
        for left, right in edges:
            children[left].append(right)
            children[right].append(left)
        order = [0]
        parent = [-1] * len(nums)
        for node in order:
            for neighbor in children[node]:
                if neighbor != parent[node]:
                    parent[neighbor] = node
                    order.append(neighbor)
        for parts in range(len(nums), 0, -1):
            if total % parts:
                continue
            target = total // parts
            sums = nums[:]
            valid = True
            for node in reversed(order[1:]):
                if sums[node] > target:
                    valid = False
                    break
                if sums[node] == target:
                    sums[node] = 0
                sums[parent[node]] += sums[node]
            if valid and sums[0] == target:
                return parts - 1
        return 0
