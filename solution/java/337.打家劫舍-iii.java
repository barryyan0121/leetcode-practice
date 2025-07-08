import java.util.HashMap;

import javax.swing.tree.TreeNode;

/*
 * @lc app=leetcode.cn id=337 lang=java
 *
 * [337] 打家劫舍 III
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
    HashMap<TreeNode, Integer> map = new HashMap<>();

    public int rob(TreeNode root) {
        if (root == null)
            return 0;
        if (map.containsKey(root))
            return map.get(root);

        int todo = root.val + (root.left != null ? rob(root.left.left) + rob(root.left.right) : 0)
                + (root.right != null ? rob(root.right.left) + rob(root.right.right) : 0);
        int nodo = rob(root.left) + rob(root.right);
        int res = Math.max(todo, nodo);
        map.put(root, res);
        return res;

    }

}
// @lc code=end
