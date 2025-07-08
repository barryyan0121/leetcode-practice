import java.util.ArrayList;
import java.util.List;

/*
 * @lc app=leetcode.cn id=144 lang=java
 *
 * [144] 二叉树的前序遍历
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
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> arr = new ArrayList<>();
        if (root == null) {
            return arr;
        }
        arr.add(root.val);
        arr.addAll(preorderTraversal(root.left));
        arr.addAll(preorderTraversal(root.right));
        return arr;
    }
}
// @lc code=end
