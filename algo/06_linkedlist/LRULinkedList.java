package linkedlist;

/**
 * @program: algo
 * @description: 用链表实现一个LRU算法。
 *
 * 维护一个有序的单链表，越靠近链表尾部的结点是越早之前访问的，
 *
 * 当有一个新的数据被访问时，我们从链表头部开始遍历链表。
 *
 * 这里仅实现最简单的操作。
 * @author: wqdong
 * @create: 2020-03-25 08:50
 **/
public class LRULinkedList {

  private static int capatity = 5;
  private static int length = 0;

  // LRU访问数据
  public static ListNode add(ListNode head, int val) {
    ListNode preNode = findPreListNode(head, val);
    if (preNode != null) {
      head = deleteElement(head, preNode.next);
      head = insertElementAtHead(head, val);
    } else {
      if (length >= capatity) {
        head = deleteElementAtTail(head);
      }
      head = insertElementAtHead(head, val);
    }

    return head;
  }


  // 找到指定元素值的前一个结点
  public static ListNode findPreListNode(ListNode head, int val) {
    ListNode tempHead = head;

    while (tempHead.next != null) {
      if (tempHead.next.val == val) {
        return tempHead;
      } else {
        tempHead = tempHead.next;
      }
    }

    return null;
  }


  // 删除链表中的指定结点，这里是已经确定链表中一定包含该结点
  public static ListNode deleteElement(ListNode head, ListNode node) {

    ListNode tempHead = head;
    ListNode tempNode = node;

    while (tempHead.next != null) {
      if (tempHead.next.val == node.val) {
        tempHead.next = tempHead.next.next;
      } else {
        tempHead = tempHead.next;
      }
    }

    length--;
    return head;
  }

  // 删除链表的尾部结点
  public static ListNode deleteElementAtTail(ListNode head) {
    ListNode fast = head.next;
    ListNode slow = head;
    while (fast.next != null) {
      fast = fast.next;
      slow = slow.next;
    }

    slow.next = null;

    length--;
    return head;
  }

  // 在链表头部插入指定元素值
  public static ListNode insertElementAtHead(ListNode head, int val) {
    ListNode tempHead = head;
    head = new ListNode(val);
    head.next = tempHead;

    length++;
    return head;
  }

  // 打印链表信息
  public static void printListNode(ListNode head) {
    while (head != null) {
      System.out.print(head.val + " ");
      head = head.next;
    }
  }

  public static void main(String[] args) {
    ListNode head = new ListNode(1);
    head.next = new ListNode(2);
    head.next.next = new ListNode(3);
    head.next.next.next = new ListNode(4);
    head.next.next.next.next = new ListNode(5);
    length = 5;

    head = add(head, 5);
    printListNode(head);

    System.out.println();
    head = add(head, 4);
    printListNode(head);

    System.out.println();
    head = add(head, 0);
    printListNode(head);

    System.out.println();
    head = add(head, 3);
    printListNode(head);

    System.out.println();
    head = add(head, 4);
    printListNode(head);

  }

}
