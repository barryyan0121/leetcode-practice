import java.util.Arrays;

/*
 * @lc app=leetcode.cn id=204 lang=java
 *
 * [204] 计数质数
 */

// @lc code=start
class Solution {
    public int countPrimes(int n) {
        boolean[] isPrime = new boolean[n];
        int count = 0;
        Arrays.fill(isPrime, true);
        for (int i = 2; i < n; i++) {
            if (isPrime[i]) {
                count++;
                if ((long) i * i < n) {
                    for (int j = i * i; j < n; j += i) {
                        isPrime[j] = false;
                    }
                }
            }
        }

        return count;
    }

    // 0 1 2 3 4 5 6 7 8 9
    // 1 1 1 1 0 1 0 1 0 0
}
// @lc code=end
