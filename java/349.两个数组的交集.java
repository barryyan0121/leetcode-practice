import java.util.ArrayList;

/*
 * @lc app=leetcode.cn id=349 lang=java
 *
 * [349] 两个数组的交集
 */

// @lc code=start
class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        int n1 = nums1.length, n2 = nums2.length;
        ArrayList<Integer> result = new ArrayList<>();
        int i = 0, j = 0;
        int prev = -1;
        while (i < n1 && j < n2) {
            if (nums1[i] == nums2[j] && prev != nums1[i]) {
                result.add(nums1[i]);
                prev = nums1[i];
                i++;
                j++;
            } else if (nums1[i] < nums2[j]) {
                i++;
            } else {
                j++;
            }
        }
        int[] ret = new int[result.size()];
        for (int id = 0; id < result.size(); id++) {
            ret[id] = result.get(id);
        }
        return ret;
    }
}
// @lc code=end
