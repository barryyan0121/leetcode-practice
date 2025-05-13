/*
 * @lc app=leetcode.cn id=783 lang=java
 *
 * [783] 二叉搜索树节点最小距离
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
    int min = Integer.MAX_VALUE, curr = Integer.MAX_VALUE, last = -1;

    public int minDiffInBST(TreeNode root) {
        traverse(root);
        return min;
    }

    public void traverse(TreeNode root) {
        if (root == null)
            return;

        traverse(root.left);
        if (last != -1) {
            curr = Math.abs(root.val - last);
        }
        last = root.val;
        min = Math.min(curr, min);
        traverse(root.right);
    }
}
// @lc code=end
