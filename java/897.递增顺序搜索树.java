/*
 * @lc app=leetcode.cn id=897 lang=java
 *
 * [897] 递增顺序搜索树
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
    TreeNode ret = new TreeNode(-1);

    public TreeNode increasingBST(TreeNode root) {
        TreeNode ans = ret;
        traverse(root);
        return ans.right;
    }

    public void traverse(TreeNode root) {
        if (root == null)
            return;

        traverse(root.left);
        ret.right = root;
        root.left = null;
        ret = ret.right;
        traverse(root.right);
    }
}
// @lc code=end
