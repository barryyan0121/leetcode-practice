import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;

/*
 * @lc app=leetcode.cn id=380 lang=java
 *
 * [380] O(1) 时间插入、删除和获取随机元素
 */

// @lc code=start
class RandomizedSet {

    List<Integer> nums;
    Map<Integer, Integer> indices;
    Random rand;

    public RandomizedSet() {
        nums = new ArrayList<>();
        indices = new HashMap<>();
        rand = new Random();
    }

    public boolean insert(int val) {
        if (indices.containsKey(val)) {
            return false;
        }
        int length = nums.size();
        indices.put(val, length);
        nums.add(val);
        return true;
    }

    public boolean remove(int val) {
        if (!indices.containsKey(val)) {
            return false;
        }
        int index = indices.get(val);
        int last = nums.get(nums.size() - 1);
        indices.put(last, index);
        nums.set(index, last);
        nums.remove(nums.size() - 1);
        indices.remove(val);
        return true;

    }

    public int getRandom() {
        int randInt = rand.nextInt(nums.size());
        return nums.get(randInt);
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
// @lc code=end
