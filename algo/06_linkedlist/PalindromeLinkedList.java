package linkedlist;


import java.util.Stack;

/**
 * @program: algo
 * @description: 回文字符串，字符串用链表存储，为了简便起见，使用整型数字来代替字符串
 * @author: wqdong
 * @create: 2020-03-24 20:18
 **/
public class PalindromeLinkedList {

  // Runtime: 3 ms, faster than 25.61% of Java online submissions for Palindrome Linked List.
  public boolean isPalindrome(ListNode head) {

    if (head == null || head.next == null) {
      return true;
    }

    Stack<Integer> stack = new Stack<Integer>();
    ListNode temp = head;

    while (temp != null) {
      stack.push(temp.val);
      temp = temp.next;
    }

    while (head != null) {
      if (stack.pop() != head.val) {
        return false;
      }
      head = head.next;
    }

    return true;

  }

  // Runtime: 1 ms, faster than 94.70% of Java online submissions for Palindrome Linked List.
  public boolean isPalindrome2(ListNode head) {
    if (head == null || head.next == null) {
      return true;
    }

    ListNode fast = head;
    ListNode slow = head;

    while (fast != null && fast.next != null) {
      fast = fast.next.next;
      slow = slow.next;
    }

    if (fast != null) {
      slow = slow.next;
    }

    slow = reverse(slow);
    fast = head;

    while (slow != null) {
      if (fast.val != slow.val) {
        return false;
      }
      fast = fast.next;
      slow = slow.next;
    }

    return true;
  }

  private ListNode reverse(ListNode head) {
    ListNode prev = null;
    while (head != null) {
      ListNode next = head.next;
      head.next = prev;
      prev = head;
      head = next;
    }
    return prev;
  }
}
