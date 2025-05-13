import java.util.HashSet;

/*
 * @lc app=leetcode.cn id=202 lang=java
 *
 * [202] 快乐数
 */

// @lc code=start
class Solution {
    public boolean isHappy(int n) {
        HashSet<Integer> set = new HashSet<>();
        while (!set.contains(n)) {
            set.add(n);
            n = square(n);
            if (n == 1) {
                return true;
            }
        }
        return false;
    }

    public int square(int n) {
        int result = 0, digit = 0;
        while (n != 0) {
            digit = n % 10;
            result += digit * digit;
            n /= 10;
        }
        return result;
    }
}
// @lc code=end
