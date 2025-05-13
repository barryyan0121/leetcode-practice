import java.util.HashMap;

/*
 * @lc app=leetcode.cn id=437 lang=java
 *
 * [437] 路径总和 III
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

    HashMap<Integer, Integer> map = new HashMap<>();
    int pathSum = 0, targetSum, res = 0;

    public int pathSum(TreeNode root, int targetSum) {
        this.targetSum = targetSum;
        map.put(0, 1);
        traverse(root);
        return res;
    }

    void traverse(TreeNode root) {
        if (root == null)
            return;

        pathSum += root.val;

        res += map.getOrDefault(pathSum - targetSum, 0);
        map.put(pathSum, map.getOrDefault(pathSum, 0) + 1);
        traverse(root.left);
        traverse(root.right);
        map.put(pathSum, map.get(pathSum) - 1);
        pathSum -= root.val;
    }
}
// @lc code=end
