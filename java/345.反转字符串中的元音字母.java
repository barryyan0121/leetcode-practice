import java.util.HashSet;
import java.util.Set;

/*
 * @lc app=leetcode.cn id=345 lang=java
 *
 * [345] 反转字符串中的元音字母
 */

// @lc code=start
class Solution {
    public String reverseVowels(String s) {
        int i = 0, n = s.length(), j = n - 1;
        char[] c = s.toCharArray();
        while (i < j) {
            if (isVowel(c[i]) && isVowel(c[j])) {
                char temp = c[i];
                c[i] = c[j];
                c[j] = temp;
                i++;
                j--;
            } else {
                while (i < n && !isVowel(c[i])) {
                    i++;
                }
                while (j >= 0 && !isVowel(c[j])) {
                    j--;
                }
            }
        }
        return new String(c);
    }

    public boolean isVowel(char ch) {
        return "aeiouAEIOU".indexOf(ch) >= 0;
    }
}
// @lc code=end
