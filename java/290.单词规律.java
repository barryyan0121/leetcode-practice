import java.util.Map;

/*
 * @lc app=leetcode.cn id=290 lang=java
 *
 * [290] 单词规律
 */

// @lc code=start
class Solution {
    public boolean wordPattern(String pattern, String s) {
        Map<String, Character> str2ch = new HashMap<String, Character>();
        Map<Character, String> ch2str = new HashMap<Character, String>();

        String[] str = s.split(" ");
        char[] pat = pattern.toCharArray();
        int n = str.length;
        if (n != pat.length) {
            return false;
        }
        for (int i = 0; i < n; i++) {
            if (str2ch.containsKey(str[i]) && !str2ch.get(str[i]).equals(pat[i])) {
                return false;
            }
            if (ch2str.containsKey(pat[i]) && !ch2str.get(pat[i]).equals(str[i])) {
                return false;
            }
            str2ch.put(str[i], pat[i]);
            ch2str.put(pat[i], str[i]);
        }
        return true;
    }
}
// @lc code=end
