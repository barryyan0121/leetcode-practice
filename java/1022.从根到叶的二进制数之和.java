/*
 * @lc app=leetcode.cn id=1022 lang=java
 *
 * [1022] 从根到叶的二进制数之和
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
    int path, res;

    public int sumRootToLeaf(TreeNode root) {
        traverse(root);
        return res;
    }

    void traverse(TreeNode root) {
        if (root == null)
            return;
        if (root.left == null && root.right == null) {
            res += path << 1 | root.val;
            return;
        }
        path = path << 1 | root.val;
        traverse(root.left);
        traverse(root.right);
        path >>= 1;
    }
}
// @lc code=end
