import java.util.ArrayList;
import java.util.List;

/*
 * @lc app=leetcode.cn id=500 lang=java
 *
 * [500] 键盘行
 */

// @lc code=start
class Solution {
    static String[] ss = new String[] { "qwertyuiop", "asdfghjkl", "zxcvbnm" };
    static int[] hash = new int[26];
    static {
        for (int i = 0; i < ss.length; i++) {
            for (char c : ss[i].toCharArray())
                hash[c - 'a'] = i;
        }
    }

    public String[] findWords(String[] words) {
        List<String> list = new ArrayList<>();
        for (String w : words) {
            int t = -1;
            char arr[] = w.toCharArray();
            for (int i = 0; i < arr.length; i++) {
                char c = arr[i];
                c = Character.toLowerCase(c);
                if (t == -1)
                    t = hash[c - 'a'];
                else if (t != hash[c - 'a'])
                    break;
                if (i == w.length() - 1) {
                    list.add(w);
                }
            }

        }
        return list.toArray(new String[list.size()]);
    }
}
// @lc code=end
