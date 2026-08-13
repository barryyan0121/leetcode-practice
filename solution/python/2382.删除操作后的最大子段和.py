"""2382. 删除操作后的最大子段和"""


class Solution:
    def maximumSegmentSum(self, nums: list[int], removeQueries: list[int]) -> list[int]:
        parent = list(range(len(nums)))
        total = [0] * len(nums)
        active = [False] * len(nums)

        def find(node: int) -> int:
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        answer = [0] * len(nums)
        best = 0
        for index in range(len(nums) - 1, -1, -1):
            node = removeQueries[index]
            active[node] = True
            total[node] = nums[node]
            for neighbor in (node - 1, node + 1):
                if 0 <= neighbor < len(nums) and active[neighbor]:
                    left, right = find(node), find(neighbor)
                    if left != right:
                        parent[right] = left
                        total[left] += total[right]
            best = max(best, total[find(node)])
            if index:
                answer[index - 1] = best
        return answer

if __name__ == "__main__":
    assert Solution().maximumSegmentSum([1,2,5,6,1], [0,3,2,4,1]) == [14,7,2,2,0]
