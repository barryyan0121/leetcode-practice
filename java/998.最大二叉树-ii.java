/*
 * @lc app=leetcode.cn id=998 lang=java
 *
 * [998] 最大二叉树 II
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
    public TreeNode insertIntoMaxTree(TreeNode root, int val) {
        if (root == null)
            return new TreeNode(val);

        if (root.val < val) {
            TreeNode temp = root;
            root = new TreeNode(val);
            root.left = temp;
        } else {
            root.right = insertIntoMaxTree(root.right, val);
        }
        return root;
    }
}
// @lc code=end
