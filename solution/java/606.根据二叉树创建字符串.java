/*
 * @lc app=leetcode.cn id=606 lang=java
 *
 * [606] 根据二叉树创建字符串
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

    public String tree2str(TreeNode root) {
        StringBuilder s = new StringBuilder("");
        if (root == null) {
            return s.toString();
        }
        s.append(root.val);
        if (root.left != null || root.right != null) {
            s.append("(");
            s.append(tree2str(root.left));
            s.append(")");
        }
        if (root.right != null) {
            s.append("(");
            s.append(tree2str(root.right));
            s.append(")");
        }

        return s.toString();
    }
}
// @lc code=end
