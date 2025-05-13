import java.util.*;

/*
 * @lc app=leetcode.cn id=118 lang=java
 *
 * [118] 杨辉三角
 */

// @lc code=start
class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ret = new ArrayList<>();
        for (int i = 0; i < numRows; i++) {
            List<Integer> row = new ArrayList<>();
            row.add(1);
            if (i == 0) {
                ret.add(row);
                continue;
            }
            for (int j = 1; j < i; j++) {
                int res = ret.get(i - 1).get(j - 1) + ret.get(i - 1).get(j);
                row.add(res);
            }
            row.add(1);
            ret.add(row);
        }
        return ret;
    }
}
// @lc code=end
