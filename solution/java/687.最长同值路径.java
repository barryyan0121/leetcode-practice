/*
 * @lc app=leetcode.cn id=687 lang=java
 *
 * [687] 最长同值路径
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
    public int longestUnivaluePath(TreeNode root) {
        if (root == null)
            return 0;
        maxDepth(root, root.val);
        return res;
    }

    int res = 0;

    int maxDepth(TreeNode root, int val) {
        if (root == null)
            return 0;
        int left = maxDepth(root.left, root.val);
        int right = maxDepth(root.right, root.val);
        res = Math.max(res, left + right);
        if (root.val != val)
            return 0;
        return 1 + Math.max(left, right);
    }
}
// @lc code=end
