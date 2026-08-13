"""3845. 最大子数组异或值"""

from collections import deque


class TrieNode:
    __slots__ = ("child", "count")

    def __init__(self) -> None:
        self.child = [-1, -1]
        self.count = 0


class BinaryTrie:
    def __init__(self) -> None:
        self.nodes = [TrieNode()]

    def add(self, value: int, delta: int) -> None:
        node = 0
        self.nodes[node].count += delta
        for bit in range(14, -1, -1):
            current = (value >> bit) & 1
            nxt = self.nodes[node].child[current]
            if nxt == -1:
                nxt = len(self.nodes)
                self.nodes[node].child[current] = nxt
                self.nodes.append(TrieNode())
            node = nxt
            self.nodes[node].count += delta

    def best_xor(self, value: int) -> int:
        node = 0
        answer = 0
        for bit in range(14, -1, -1):
            current = (value >> bit) & 1
            target = current ^ 1
            nxt = self.nodes[node].child[target]
            if nxt != -1 and self.nodes[nxt].count:
                answer |= 1 << bit
                node = nxt
            else:
                node = self.nodes[node].child[current]
        return answer


class Solution:
    def maxXor(self, nums: list[int], k: int) -> int:
        trie = BinaryTrie()
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] ^ value)

        maximum = deque()
        minimum = deque()
        left = 0
        answer = 0
        trie.add(0, 1)

        for right, value in enumerate(nums):
            while maximum and nums[maximum[-1]] <= value:
                maximum.pop()
            maximum.append(right)
            while minimum and nums[minimum[-1]] >= value:
                minimum.pop()
            minimum.append(right)

            while nums[maximum[0]] - nums[minimum[0]] > k:
                trie.add(prefix[left], -1)
                if maximum[0] == left:
                    maximum.popleft()
                if minimum[0] == left:
                    minimum.popleft()
                left += 1

            answer = max(answer, trie.best_xor(prefix[right + 1]))
            trie.add(prefix[right + 1], 1)
        return answer


if __name__ == "__main__":
    test_cases = [(([5, 4, 5, 6], 2), 7), (([5, 4, 5, 6], 1), 6)]
    for args, expected in test_cases:
        assert Solution().maxXor(*args) == expected
