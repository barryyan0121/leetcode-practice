/*
 * @lc app=leetcode.cn id=21 lang=java
 *
 * [21] 合并两个有序链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
import java.util.*;
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode p = new ListNode(-1), ret = p;
        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                p.next = list1;
                p = p.next;
                list1 = list1.next;
            } else {
                p.next =list2;
                p = p.next;
                list2 = list2.next;
            }
        }
        if (list1 != null) {
            p.next = list1;
        } else {
            p.next = list2;
        }
        return ret.next;
    }
}
// @lc code=end

