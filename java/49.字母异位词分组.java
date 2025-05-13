import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;

/*
 * @lc app=leetcode.cn id=49 lang=java
 *
 * [49] 字母异位词分组
 */

// @lc code=start
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();
        for (String s : strs) {
            String code = encode(s);
            map.putIfAbsent(code, new LinkedList<>());
            map.get(code).add(s);
        }
        List<List<String>> res = new LinkedList<>();
        for (List<String> str : map.values()) {
            res.add(str);
        }
        return res;
    }

    public String encode(String s) {
        char[] code = new char[26];
        for (char c : s.toCharArray()) {
            code[c - 'a']++;
        }
        return new String(code);
    }
}
// @lc code=end
