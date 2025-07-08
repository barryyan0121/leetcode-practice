import java.util.*;
/*
 * @lc app=leetcode.cn id=106 lang=java
 *
 * [106] 从中序与后序遍历序列构造二叉树
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

    HashMap<Integer, Integer> valToIndex = new HashMap<>();

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        for (int i = 0; i < inorder.length; i++) {
            valToIndex.put(inorder[i], i);
        }
        return build(postorder, 0, postorder.length - 1, inorder, 0, inorder.length - 1);
    }

    TreeNode build(int[] postorder, int postStart, int postEnd,
            int[] inorder, int inStart, int inEnd) {
        if (postStart > postEnd) {
            return null;
        }
        int rootval = postorder[postEnd];
        int index = valToIndex.get(rootval);
        int leftsize = index - inStart;
        TreeNode root = new TreeNode(rootval);
        root.left = build(postorder, postStart, postStart + leftsize - 1,
                inorder, inStart, index - 1);
        root.right = build(postorder, postStart + leftsize, postEnd - 1,
                inorder, index + 1, inEnd);
        return root;
    }
}
// @lc code=end
