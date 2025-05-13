import java.util.*;

/*
* @lc app=leetcode.cn id=113 lang=java
*
* [113] 路径总和 II
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
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {

        traverse(root, targetSum);
        return res;
    }

    List<List<Integer>> res = new LinkedList<>();
    LinkedList<Integer> path = new LinkedList<>();

    void traverse(TreeNode root, int sum) {
        if (root == null)
            return;
        int remain = sum - root.val;
        if (root.left == null && root.right == null) {
            if (remain == 0) {
                path.addLast(root.val);
                res.add(new LinkedList<>(path));
                path.removeLast();
            }
            return;
        }
        path.addLast(root.val);
        traverse(root.left, remain);
        traverse(root.right, remain);
        path.removeLast();
    }
}
// @lc code=end
