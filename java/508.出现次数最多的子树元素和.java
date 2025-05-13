import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

/*
 * @lc app=leetcode.cn id=508 lang=java
 *
 * [508] 出现次数最多的子树元素和
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

    public int[] findFrequentTreeSum(TreeNode root) {
        sum(root);
        int maxCount = 0;
        for (int count : map.values()) {
            maxCount = Math.max(maxCount, count);
        }
        List<Integer> res = new ArrayList<>();
        for (int i : map.keySet()) {
            if (map.get(i) == maxCount) {
                res.add(i);
            }
        }
        int[] arr = new int[res.size()];
        for (int i = 0; i < res.size(); i++) {
            arr[i] = res.get(i);
        }
        return arr;
    }

    private int sum(TreeNode root) {
        if (root == null)
            return 0;
        int leftSum = sum(root.left);
        int rightSum = sum(root.right);
        int res = root.val + leftSum + rightSum;
        map.put(res, map.getOrDefault(res, 0) + 1);
        return res;
    }
}
// @lc code=end
