# @lc app=leetcode.cn id=1418 lang=python3


class Solution:
    def displayTable(self, orders: list[list[str]]) -> list[list[str]]:
        dishes = sorted({order[2] for order in orders})
        tables = sorted({int(order[1]) for order in orders})
        counts = {(table, dish): 0 for table in tables for dish in dishes}
        for _, table, dish in orders:
            counts[(int(table), dish)] += 1
        result = [["Table", *dishes]]
        for table in tables:
            result.append(
                [str(table), *(str(counts[(table, dish)]) for dish in dishes)]
            )
        return result


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.displayTable,
            (
                [
                    ["David", "3", "Ceviche"],
                    ["Corina", "10", "Beef Burrito"],
                    ["David", "3", "Fried Chicken"],
                    ["Carla", "5", "Water"],
                    ["Carla", "5", "Ceviche"],
                    ["Rous", "3", "Ceviche"],
                ],
            ),
            [
                ["Table", "Beef Burrito", "Ceviche", "Fried Chicken", "Water"],
                ["3", "0", "2", "1", "0"],
                ["5", "0", "1", "0", "1"],
                ["10", "1", "0", "0", "0"],
            ],
        )
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1418 题 "点菜展示表" 所有测试用例通过')
