from typing import List


class Solution:
    def findSmallestRegion(
        self, regions: List[List[str]], region1: str, region2: str
    ) -> str:
        parent = {}
        for region in regions:
            for child in region[1:]:
                parent[child] = region[0]
        ancestors = set()
        while region1:
            ancestors.add(region1)
            region1 = parent.get(region1)
        while region2 not in ancestors:
            region2 = parent[region2]
        return region2


if __name__ == "__main__":
    test_cases = [
        (
            [
                ["Earth", "North America", "South America"],
                ["North America", "United States", "Canada"],
                ["United States", "New York", "Boston"],
            ],
            "New York",
            "Canada",
            "North America",
        )
    ]
    for _, (regions, region1, region2, expected) in enumerate(test_cases):
        assert Solution().findSmallestRegion(regions, region1, region2) == expected
