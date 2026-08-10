class Solution:
    def maximizeXor(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        nums.sort()
        trie = [[-1, -1]]

        def insert(value: int) -> None:
            node = 0
            for bit in range(30, -1, -1):
                branch = (value >> bit) & 1
                if trie[node][branch] == -1:
                    trie[node][branch] = len(trie)
                    trie.append([-1, -1])
                node = trie[node][branch]

        def best(value: int) -> int:
            node = 0
            result = 0
            for bit in range(30, -1, -1):
                branch = ((value >> bit) & 1) ^ 1
                if trie[node][branch] == -1:
                    branch ^= 1
                result |= (branch ^ ((value >> bit) & 1)) << bit
                node = trie[node][branch]
            return result

        ordered = sorted(enumerate(queries), key=lambda item: item[1][1])
        answer = [-1] * len(queries)
        index = 0
        for query_index, (value, limit) in ordered:
            while index < len(nums) and nums[index] <= limit:
                insert(nums[index])
                index += 1
            if index:
                answer[query_index] = best(value)
        return answer


if __name__ == "__main__":
    test_cases = [
        (([0, 1, 2, 3, 4], [[3, 1], [1, 3], [5, 6]]), [3, 3, 7]),
        (([5, 2, 4, 6, 6, 3], [[12, 4], [8, 1], [6, 3]]), [15, -1, 5]),
    ]
    for index, (args, expected) in enumerate(test_cases):
        assert Solution().maximizeXor(*args) == expected, index
