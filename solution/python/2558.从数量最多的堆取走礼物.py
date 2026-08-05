"""2558. 从数量最多的堆取走礼物"""


class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        import heapq

        heap = [-gift for gift in gifts]
        heapq.heapify(heap)
        for _ in range(k):
            heapq.heapreplace(heap, -int((-heap[0]) ** 0.5))
        return -sum(heap)


if __name__ == "__main__":
    test_cases = [(([25, 64, 9, 4, 100], 4), 29)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().pickGifts(*args) == expected
