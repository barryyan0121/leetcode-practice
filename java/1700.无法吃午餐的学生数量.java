import java.util.LinkedList;
import java.util.*;

/*
 * @lc app=leetcode.cn id=1700 lang=java
 *
 * [1700] 无法吃午餐的学生数量
 */

// @lc code=start
class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        int[] studentCount = new int[2];
        for (int type : students) {
            studentCount[type]++;
        }

        for (int type : sandwiches) {
            if (studentCount[type] == 0) {
                return studentCount[0] + studentCount[1];
            }
            studentCount[type]--;
        }
        return 0;
    }
}
// @lc code=end
