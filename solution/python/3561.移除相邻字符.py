"""3561. 移除相邻字符"""

import heapq


class Solution:
    def resultingString(self, s: str) -> str:
        n = len(s)
        values = [ord(char) - ord("a") for char in s]
        previous = [index - 1 for index in range(n)]
        following = [index + 1 for index in range(n)]
        alive = [True] * n
        heap = []

        def removable(left, right):
            difference = abs(values[left] - values[right])
            return difference == 1 or difference == 25

        for index in range(n - 1):
            if removable(index, index + 1):
                heapq.heappush(heap, index)

        head = 0
        while heap:
            left = heapq.heappop(heap)
            if not alive[left]:
                continue
            right = following[left]
            if right == n or not alive[right] or not removable(left, right):
                continue
            before = previous[left]
            after = following[right]
            alive[left] = alive[right] = False
            if before == -1:
                head = after
            else:
                following[before] = after
            if after < n:
                previous[after] = before
            if before != -1 and after < n and removable(before, after):
                heapq.heappush(heap, before)

        answer = []
        index = head
        while index < n:
            if alive[index]:
                answer.append(s[index])
            index = following[index]
        return "".join(answer)


if __name__ == "__main__":
    test_cases = [
        (("abc",), "c"),
        (("adcb",), ""),
        (("zadb",), "db"),
    ]
    for _, ((s,), expected) in enumerate(test_cases):
        assert Solution().resultingString(s) == expected
