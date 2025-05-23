/*
 * @lc app=leetcode.cn id=116 lang=java
 *
 * [116] 填充每个节点的下一个右侧节点指针
 */

// @lc code=start
/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        if (root == null)
            return null;
        traverse(root.left, root.right);
        return root;
    }

    void traverse(Node root1, Node root2) {
        if (root1 == null || root2 == null)
            return;

        root1.next = root2;

        traverse(root1.left, root1.right);
        traverse(root2.left, root2.right);
        traverse(root1.right, root2.left);
    }
}
// @lc code=end
