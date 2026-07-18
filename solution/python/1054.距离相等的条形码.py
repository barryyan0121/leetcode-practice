import heapq


class Solution:
    def rearrangeBarcodes(self, barcodes: list[int]) -> list[int]:
        heap = [
            (-count, value)
            for value, count in __import__("collections").Counter(barcodes).items()
        ]
        heapq.heapify(heap)
        answer = []
        previous = (0, 0)
        while heap:
            count, value = heapq.heappop(heap)
            answer.append(value)
            if previous[0] < 0:
                heapq.heappush(heap, previous)
            previous = (count + 1, value)
        return answer


if __name__ == "__main__":
    test_cases = [[1, 1, 1, 2, 2, 2]]
    for _, barcodes in enumerate(test_cases):
        answer = Solution().rearrangeBarcodes(barcodes)
        assert all(answer[i] != answer[i + 1] for i in range(len(answer) - 1))
