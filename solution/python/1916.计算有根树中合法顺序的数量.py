"""1916. 计算有根树中合法顺序的数量"""


class Solution:
    def waysToBuildRooms(self, prevRoom: list[int]) -> int:
        modulo = 10**9 + 7
        size = len(prevRoom)
        children = [[] for _ in range(size)]
        for room in range(1, size):
            children[prevRoom[room]].append(room)
        factorial = [1] * (size + 1)
        for value in range(1, size + 1):
            factorial[value] = factorial[value - 1] * value % modulo
        inverse_factorial = [1] * (size + 1)
        inverse_factorial[size] = pow(factorial[size], modulo - 2, modulo)
        for value in range(size, 0, -1):
            inverse_factorial[value - 1] = inverse_factorial[value] * value % modulo

        order = [0]
        for node in order:
            order.extend(children[node])
        subtree_size = [1] * size
        ways = [1] * size
        for node in reversed(order):
            total = 0
            for child in children[node]:
                child_size = subtree_size[child]
                ways[node] = (
                    ways[node]
                    * ways[child]
                    * factorial[total + child_size]
                    * inverse_factorial[total]
                    * inverse_factorial[child_size]
                ) % modulo
                total += child_size
            subtree_size[node] = total + 1
        return ways[0]


if __name__ == "__main__":
    assert Solution().waysToBuildRooms([-1, 0, 1]) == 1
    assert Solution().waysToBuildRooms([-1, 0, 0, 1, 2]) == 6
