"""2115. 从给定原料中找到所有可以做出的菜"""

from collections import defaultdict, deque


class Solution:
    def findAllRecipes(
        self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]
    ) -> list[str]:
        need = defaultdict(list)
        degree = {recipe: len(items) for recipe, items in zip(recipes, ingredients)}
        for recipe, items in zip(recipes, ingredients):
            for item in items:
                need[item].append(recipe)
        queue = deque(supplies)
        answer = []
        while queue:
            item = queue.popleft()
            for recipe in need[item]:
                degree[recipe] -= 1
                if degree[recipe] == 0:
                    answer.append(recipe)
                    queue.append(recipe)
        return answer


if __name__ == "__main__":
    test_cases = [((["bread"], [["yeast", "flour"]], ["yeast", "flour"]), ["bread"])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().findAllRecipes(*args) == expected
