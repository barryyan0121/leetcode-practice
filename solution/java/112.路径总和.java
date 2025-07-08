/*
 * @lc app=leetcode.cn id=112 lang=java
 *
 * [112] 路径总和
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
    int target;
    boolean hasFound = false;

    public boolean hasPathSum(TreeNode root, int targetSum) {
        traverse(root, targetSum);
        return hasFound;
    }

    void traverse(TreeNode root, int targetSum) {
        if (root == null)
            return;

        target += root.val;
        if (root.left == null && root.right == null) {
            if (target == targetSum) {
                hasFound = true;
            }
        }
        traverse(root.left, targetSum);
        traverse(root.right, targetSum);
        target -= root.val;
    }
}
// @lc code=end
