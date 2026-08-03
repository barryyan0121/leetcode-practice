# @lc app=leetcode.cn id=2353 lang=python3

import heapq


class FoodRatings:
    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.ratings = dict(zip(foods, ratings))
        self.cuisines = dict(zip(foods, cuisines))
        self.heaps = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.heaps.setdefault(cuisine, []).append((-rating, food))
        for heap in self.heaps.values():
            heapq.heapify(heap)

    def changeRating(self, food: str, newRating: int) -> None:
        self.ratings[food] = newRating
        heapq.heappush(self.heaps[self.cuisines[food]], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.heaps[cuisine]
        while heap:
            neg_rating, food = heap[0]
            if -neg_rating == self.ratings[food]:
                return food
            heapq.heappop(heap)
        return ""


if __name__ == "__main__":

    def run_operations(foods, cuisines, ratings, operations):
        tracker = FoodRatings(foods, cuisines, ratings)
        result = []
        for operation, args in operations:
            value = getattr(tracker, operation)(*args)
            if operation == "highestRated":
                result.append(value)
        return result

    test_cases = [
        (
            run_operations,
            (
                ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
                ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
                [9, 12, 8, 15, 14, 7],
                [
                    ("highestRated", ("korean",)),
                    ("highestRated", ("japanese",)),
                    ("changeRating", ("sushi", 16)),
                    ("highestRated", ("japanese",)),
                    ("highestRated", ("greek",)),
                ],
            ),
            ["kimchi", "ramen", "sushi", "moussaka"],
        )
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 2353 题 "设计食物评分系统" 所有测试用例通过')
