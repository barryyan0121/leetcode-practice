/*
 * @lc app=leetcode.cn id=993 lang=java
 *
 * [993] 二叉树的堂兄弟节点
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {
    TreeNode parentX, parentY;
    int depthX, depthY;

    public boolean isCousins(TreeNode root, int x, int y) {
        depth(root, 0, null, x, y);
        if (depthX == depthY && parentX != parentY) {
            return true;
        }
        return false;
    }

    public void depth(TreeNode root, int depth, TreeNode parent, int x, int y) {
        if (root == null)
            return;
        if (root.val == x) {
            parentX = parent;
            depthX = depth;
        }
        if (root.val == y) {
            parentY = parent;
            depthY = depth;
        }
        depth(root.left, depth + 1, root, x, y);
        depth(root.right, depth + 1, root, x, y);
    }
}
// @lc code=end
