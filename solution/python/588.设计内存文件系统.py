#
# @lc app=leetcode.cn id=588 lang=python3
#
# [588] 设计内存文件系统
#


# @lc code=start
class FileSystem:
    def __init__(self):
        self.root = {"children": {}, "content": None}

    def _get(self, path, create=False):
        node = self.root
        for name in filter(None, path.split("/")):
            if create:
                node = node["children"].setdefault(
                    name, {"children": {}, "content": None}
                )
            else:
                node = node["children"][name]
        return node

    def ls(self, path: str):
        node = self._get(path)
        if node["content"] is not None:
            return [path.rsplit("/", 1)[-1]]
        return sorted(node["children"])

    def mkdir(self, path: str) -> None:
        self._get(path, True)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self._get(filePath, True)
        node["content"] = (node["content"] or "") + content

    def readContentFromFile(self, filePath: str) -> str:
        return self._get(filePath)["content"]


# @lc code=end


if __name__ == "__main__":
    fs = FileSystem()
    assert fs.ls("/") == []
    fs.mkdir("/a/b/c")
    fs.addContentToFile("/a/b/c/d", "hello")
    assert fs.ls("/") == ["a"]
    assert fs.readContentFromFile("/a/b/c/d") == "hello"
