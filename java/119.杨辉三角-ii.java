import java.util.*;

/*
 * @lc app=leetcode.cn id=119 lang=java
 *
 * [119] 杨辉三角 II
 */

// @lc code=start
class Solution {
    public List<Integer> getRow(int rowIndex) {
        ArrayList<Integer> ret = new ArrayList<>();
        ret.add(1);
        if (rowIndex == 0) {
            return ret;
        }
        List<Integer> pre = getRow(rowIndex - 1);
        for (int i = 0; i < pre.size() - 1; i++) {
            ret.add(pre.get(i) + pre.get(i + 1));
        }
        ret.add(1);
        return ret;

    }
}
// @lc code=end

