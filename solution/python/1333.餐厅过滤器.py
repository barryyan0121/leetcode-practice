# @lc app=leetcode.cn id=1333 lang=python3

from typing import List


class Solution:
    def filterRestaurants(
        self,
        restaurants: List[List[int]],
        veganFriendly: int,
        maxPrice: int,
        maxDistance: int,
    ) -> List[int]:
        eligible = [
            restaurant
            for restaurant in restaurants
            if (not veganFriendly or restaurant[2])
            and restaurant[3] <= maxPrice
            and restaurant[4] <= maxDistance
        ]
        return [
            restaurant[0]
            for restaurant in sorted(
                eligible, key=lambda item: (item[1], item[0]), reverse=True
            )
        ]


if __name__ == "__main__":
    test_cases = [
        (
            Solution().filterRestaurants,
            (
                [
                    [1, 4, 1, 40, 10],
                    [2, 8, 0, 50, 5],
                    [3, 8, 1, 30, 4],
                    [4, 10, 1, 10, 3],
                    [5, 1, 1, 15, 1],
                ],
                1,
                50,
                10,
            ),
            [4, 3, 1, 5],
        ),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1333 题 "餐厅过滤器" 所有测试用例通过')
