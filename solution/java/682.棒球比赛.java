import java.util.*;
/*
 * @lc app=leetcode.cn id=682 lang=java
 *
 * [682] 棒球比赛
 */

// @lc code=start
class Solution {
    public int calPoints(String[] ops) {
        int ret = 0, result = 0, n = 0;
        List<Integer> arr = new ArrayList<>();
        for (String s : ops) {
            n = arr.size();
            switch (s.charAt(0)) {
                case '+':
                    result = arr.get(n - 1) + arr.get(n - 2);
                    ret += result;
                    arr.add(result);
                    break;
                case 'D':
                    result = arr.get(n - 1) * 2;
                    ret += result;
                    arr.add(result);
                    break;
                case 'C':
                    result = arr.get(n - 1);
                    ret -= result;
                    arr.remove(n - 1);
                    break;
                default:
                    result = Integer.parseInt(s);
                    ret += result;
                    arr.add(result);
                    break;
            }
        }
        return ret;
    }
}
// @lc code=end
