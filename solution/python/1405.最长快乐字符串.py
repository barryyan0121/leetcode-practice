# @lc app=leetcode.cn id=1405 lang=python3
import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [
            (-count, char) for count, char in ((a, "a"), (b, "b"), (c, "c")) if count
        ]
        heapq.heapify(heap)
        result = []
        while heap:
            count, char = heapq.heappop(heap)
            if len(result) >= 2 and result[-1] == result[-2] == char:
                if not heap:
                    break
                other_count, other = heapq.heappop(heap)
                result.append(other)
                other_count += 1
                if other_count:
                    heapq.heappush(heap, (other_count, other))
                heapq.heappush(heap, (count, char))
            else:
                result.append(char)
                count += 1
                if count:
                    heapq.heappush(heap, (count, char))
        return "".join(result)


if __name__ == "__main__":
    test_cases = [
        (Solution().longestDiverseString, (1, 1, 7), "ccaccbcc"),
        (Solution().longestDiverseString, (7, 1, 0), "aabaa"),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1405 题 "最长快乐字符串" 所有测试用例通过')
