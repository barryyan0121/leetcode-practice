import java.util.*;
/*
 * @lc app=leetcode.cn id=257 lang=java
 *
 * [257] 二叉树的所有路径
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

    LinkedList<String> path = new LinkedList<>();
    LinkedList<String> res = new LinkedList<>();

    public List<String> binaryTreePaths(TreeNode root) {
        traverse(root);
        return res;
    }

    void traverse(TreeNode root) {
        if (root == null)
            return;
        path.addLast(root.val + "");
        if (root.left == null && root.right == null) {
            res.addLast(String.join("->", path));
            path.removeLast();
            return;
        }
        traverse(root.left);
        traverse(root.right);
        path.removeLast();
    }
}
// @lc code=end
