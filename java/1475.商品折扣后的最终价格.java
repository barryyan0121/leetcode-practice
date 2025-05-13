import java.util.Stack;

/*
 * @lc app=leetcode.cn id=1475 lang=java
 *
 * [1475] 商品折扣后的最终价格
 */

// @lc code=start
class Solution {
    public int[] finalPrices(int[] prices) {
        return nextSmallerOrEqualElement(prices);
    }

    public int[] nextSmallerOrEqualElement(int[] num) {
        Stack<Integer> stack = new Stack<>();
        int[] res = new int[num.length];
        for (int i = num.length - 1; i >= 0; i--) {
            while (!stack.empty() && stack.peek() > num[i]) {
                stack.pop();
            }
            res[i] = stack.empty() ? num[i] : num[i] - stack.peek();
            stack.push(num[i]);
        }
        return res;
    }
}
// @lc code=end
