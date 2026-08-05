"""1912. 设计电影租借系统"""

import heapq


class MovieRentingSystem:
    def __init__(self, n: int, entries: list[list[int]]):
        self.price = {}
        self.available = set()
        self.rented = set()
        self.version = {}
        self.available_version = {}
        self.search_heap = {}
        self.rented_heap = []
        for shop, movie, price in entries:
            key = (shop, movie)
            self.price[key] = price
            self.available.add(key)
            self.available_version[key] = 0
            self.search_heap.setdefault(movie, []).append((price, shop, 0))
        for heap in self.search_heap.values():
            heapq.heapify(heap)

    def search(self, movie: int) -> list[int]:
        heap = self.search_heap.get(movie, [])
        result = []
        stale = []
        while heap and len(result) < 5:
            price, shop, version = heapq.heappop(heap)
            if (shop, movie) in self.available and self.available_version[
                (shop, movie)
            ] == version:
                result.append(shop)
                stale.append((price, shop, version))
        for item in stale:
            heapq.heappush(heap, item)
        return result

    def rent(self, shop: int, movie: int) -> None:
        key = (shop, movie)
        self.available.remove(key)
        self.rented.add(key)
        self.version[key] = self.version.get(key, 0) + 1
        heapq.heappush(
            self.rented_heap,
            (self.price[key], shop, movie, self.version[key]),
        )

    def drop(self, shop: int, movie: int) -> None:
        key = (shop, movie)
        self.rented.remove(key)
        self.available.add(key)
        self.available_version[key] += 1
        heapq.heappush(
            self.search_heap[movie],
            (self.price[key], shop, self.available_version[key]),
        )

    def report(self) -> list[list[int]]:
        result = []
        stale = []
        while self.rented_heap and len(result) < 5:
            price, shop, movie, version = heapq.heappop(self.rented_heap)
            if (shop, movie) in self.rented and self.version[(shop, movie)] == version:
                result.append([shop, movie])
                stale.append((price, shop, movie, version))
        for item in stale:
            heapq.heappush(self.rented_heap, item)
        return result


if __name__ == "__main__":
    test_cases = [((), True)]
    for _, (args, expected) in enumerate(test_cases):
        system = MovieRentingSystem(3, [[0, 1, 5], [0, 2, 6], [1, 1, 4], [2, 1, 7]])
        assert system.search(1) == [1, 0, 2]
        system.rent(1, 1)
        assert system.report() == [[1, 1]]
        system.drop(1, 1)
        assert system.search(1) == [1, 0, 2]
