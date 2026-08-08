#
# @lc app=leetcode.cn id=1166 lang=python3
#
# [1166] 设计文件系统
#


# @lc code=start
class FileSystem:
    def __init__(self):
        self.values = {"/": -1}

    def createPath(self, path, value):
        parent = path[: path.rfind("/")] or "/"
        if path in self.values or parent not in self.values:
            return False
        self.values[path] = value
        return True

    def get(self, path):
        return self.values.get(path, -1)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
# @lc code=end


if __name__ == "__main__":
    test_cases = [("/a", 1, True), ("/a/b", 2, True), ("/c/d", 1, False)]
    file_system = FileSystem()
    for index, (path, value, expected) in enumerate(test_cases):
        assert file_system.createPath(path, value) == expected, index
    assert file_system.get("/a/b") == 2
