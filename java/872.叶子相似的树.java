import java.util.ArrayList;

/*
 * @lc app=leetcode.cn id=872 lang=java
 *
 * [872] 叶子相似的树
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
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        ArrayList<Integer> arr1 = getLeaf(root1);
        ArrayList<Integer> arr2 = getLeaf(root2);
        return arr1.equals(arr2);
    }

    ArrayList<Integer> getLeaf(TreeNode root) {
        ArrayList<Integer> arr = new ArrayList<>();
        if (root == null) {
            return arr;
        }
        if (root.left == null && root.right == null) {
            arr.add(root.val);
        }
        arr.addAll(getLeaf(root.left));
        arr.addAll(getLeaf(root.right));
        return arr;
    }
}
// @lc code=end
