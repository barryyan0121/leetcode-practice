import java.util.HashMap;
import java.util.LinkedList;

/*
 * @lc app=leetcode.cn id=652 lang=java
 *
 * [652] 寻找重复的子树
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
    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        traverse(root);
        return res;
    }

    List<TreeNode> res = new LinkedList<>();
    HashMap<String, Integer> memo = new HashMap<>();

    String traverse(TreeNode root) {
        if (root == null)
            return " ";

        String left = traverse(root.left);
        String right = traverse(root.right);
        String subtree = left + "," + right + "," + root.val;
        int freq = memo.getOrDefault(subtree, 0);
        if (freq == 1) {
            res.add(root);
        }

        memo.put(subtree, freq + 1);
        return subtree;
    }
}
// @lc code=end
