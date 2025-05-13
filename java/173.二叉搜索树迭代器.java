import java.util.Stack;

import javax.swing.tree.TreeNode;

/*
 * @lc app=leetcode.cn id=173 lang=java
 *
 * [173] 二叉搜索树迭代器
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
class BSTIterator {

    public Stack<TreeNode> stk = new Stack<>();

    public void pushLeftBranch(TreeNode p) {
        while (p != null) {
            stk.push(p);
            p = p.left;
        }
    }

    public BSTIterator(TreeNode root) {
        pushLeftBranch(root);
    }

    public int next() {
        TreeNode p = stk.pop();
        pushLeftBranch(p.right);
        return p.val;
    }

    public boolean hasNext() {
        return !stk.isEmpty();
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */
// @lc code=end
