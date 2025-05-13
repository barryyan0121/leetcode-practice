import java.util.ArrayList;
import java.util.List;

/*
 * @lc app=leetcode.cn id=501 lang=java
 *
 * [501] 二叉搜索树中的众数
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
    int count, base, maxCount;
    List<Integer> arr = new ArrayList<>();

    public int[] findMode(TreeNode root) {
        traverse(root);
        int[] res = new int[arr.size()];
        for (int i = 0; i < arr.size(); i++) {
            res[i] = arr.get(i);
        }
        return res;
    }

    public void update(int x) {
        if (base == x) {
            count++;
        } else {
            base = x;
            count = 1;
        }
        if (count == maxCount) {
            arr.add(base);
        }
        if (count > maxCount) {
            maxCount = count;
            arr.clear();
            arr.add(base);
        }
    }

    public void traverse(TreeNode root) {
        if (root == null) {
            return;
        }
        traverse(root.left);
        update(root.val);
        traverse(root.right);
    }
}
// @lc code=end
