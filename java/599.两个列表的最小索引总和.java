import java.util.ArrayList;
import java.util.HashMap;

/*
 * @lc app=leetcode.cn id=599 lang=java
 *
 * [599] 两个列表的最小索引总和
 */

// @lc code=start
class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        HashMap<String, Integer> map = new HashMap<>();
        ArrayList<String> mins = new ArrayList<>();
        int currMin = Integer.MAX_VALUE, min = Integer.MAX_VALUE;
        for (int i = 0; i < list1.length; i++) {
            map.put(list1[i], i);
        }
        for (int i = 0; i < list2.length; i++) {
            if (map.containsKey(list2[i])) {
                currMin = map.get(list2[i]) + i;
                if (currMin < min) {
                    min = currMin;
                    mins.clear();
                    mins.add(list2[i]);
                } else if (currMin == min) {
                    mins.add(list2[i]);
                }
            }
        }
        return mins.toArray(new String[mins.size()]);
    }
}
// @lc code=end
