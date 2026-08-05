class Solution:
    def numberOfCategories(self, n: int, H: "CategoryHandler") -> int:
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for i in range(n):
            for j in range(i + 1, n):
                a, b = find(i), find(j)
                if H.haveSameCategory(i, j) and a != b:
                    parent[a] = b
        return len({find(i) for i in range(n)})


if __name__ == "__main__":
    print("交互题，跳过本地模拟")
