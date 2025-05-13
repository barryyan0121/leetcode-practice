/*
 * @lc app=leetcode.cn id=671 lang=java
 *
 * [671] 二叉树中第二小的节点
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
    public int findSecondMinimumValue(TreeNode root) {
        if (root == null || root.left == null && root.right == null)
            return -1;
        int left = root.left.val, right = root.right.val;
        if (root.val == left) {
            left = findSecondMinimumValue(root.left);
        }
        if (root.val == right) {
            right = findSecondMinimumValue(root.right);
        }
        if (left == -1) {
            return right;
        }
        if (right == -1) {
            return left;
        }
        return Math.min(left, right);

    }
}
// @lc code=end
