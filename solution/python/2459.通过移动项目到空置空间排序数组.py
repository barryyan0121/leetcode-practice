"""2459. 通过移动项目到空置空间排序数组"""


class Solution:
    def sortArray(self, nums: list[int]) -> int:
        def cost(mapping: list[int], empty_target: int) -> int:
            visited = [False] * len(mapping)
            zero_cycle = 1
            other = 0
            for start in range(len(mapping)):
                if visited[start]:
                    continue
                cycle = []
                node = start
                while not visited[node]:
                    visited[node] = True
                    cycle.append(node)
                    node = mapping[node]
                if len(cycle) == 1:
                    continue
                if empty_target in cycle:
                    zero_cycle = len(cycle)
                else:
                    other += len(cycle) + 1
            return zero_cycle - 1 + other

        rotated = [value - 1 if value else len(nums) - 1 for value in nums]
        return min(cost(nums, 0), cost(rotated, len(nums) - 1))

if __name__ == "__main__":
    assert Solution().sortArray([1,0,2,3]) == 1
