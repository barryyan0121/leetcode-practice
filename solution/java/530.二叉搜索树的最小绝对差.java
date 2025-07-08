/*
 * @lc app=leetcode.cn id=530 lang=java
 *
 * [530] 二叉搜索树的最小绝对差
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
    int lastNode = -1, minimum = Integer.MAX_VALUE;

    public int getMinimumDifference(TreeNode root) {
        traverse(root);
        return minimum;
    }

    void traverse(TreeNode root) {
        if (root == null)
            return;
        traverse(root.left);
        if (lastNode == -1) {
            lastNode = root.val;
        } else {
            int currMin = Math.abs(root.val - lastNode);
            lastNode = root.val;
            minimum = Math.min(minimum, currMin);
        }
        traverse(root.right);

    }
}
// @lc code=end
