/*
 * @lc app=leetcode.cn id=513 lang=java
 *
 * [513] 找树左下角的值
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
    // 记录二叉树的最大深度
    int maxDepth = 0;
    // 记录 traverse 递归遍历到的深度
    int depth = 0;
    TreeNode res = null;

    public int findBottomLeftValue(TreeNode root) {
        traverse(root);
        return res.val;
    }

    void traverse(TreeNode root) {
        if (root == null) {
            return;
        }
        // 前序遍历位置
        depth++;
        if (depth > maxDepth) {
            // 到最大深度时第一次遇到的节点就是左下角的节点
            maxDepth = depth;
            res = root;
        }
        traverse(root.left);
        traverse(root.right);
        // 后序遍历位置
        depth--;
    }
}
// @lc code=end
