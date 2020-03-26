package queue;

import linkedlist.ListNode;
import stack.LinkedListStack;

/**
 * @program: algo
 * @description: 链表实现的队列
 * @author: wqdong
 * @create: 2020-03-26 14:03
 **/
public class LinkedListQueue {

  private ListNode head = null;
  private ListNode tail = null;
  private int length = 0;

  // 入队操作
  public void push(int val) {
    if (tail == null) {
      ListNode node = new ListNode(val);
      head = node;
      tail = node;
      length++;
    } else {
      tail.next = new ListNode(val);
      tail = tail.next;
      length++;
    }
  }

  // 出队操作
  public int poll() {

    if (head == null) {
      System.out.println("队列为空！");
      return -1;
    }

    int poll = head.val;
    head = head.next;

    if (head == null) {
      tail = null;
    }

    length--;

    return poll;
  }

  // 获取队列头部元素
  public int peek() {
    if (head == null) {
      System.out.println("队列为空！");
      return -1;
    }

    int peek = head.val;
    return peek;
  }

  // 输出队列信息
  public void printQueue() {
    ListNode temp = head;
    while (temp != null) {
      System.out.print(temp.val + " ");
      temp = temp.next;
    }
    System.out.println();
  }

  // 队列长度
  public int getLength() {
    return length;
  }


  public static void main(String[] args) {
    LinkedListQueue linkedListQueue = new LinkedListQueue();

    linkedListQueue.push(1);
    linkedListQueue.push(2);
    linkedListQueue.push(3);
    linkedListQueue.push(4);
    linkedListQueue.push(5);

    linkedListQueue.printQueue();

    linkedListQueue.poll();
    linkedListQueue.poll();

    linkedListQueue.push(6);
    linkedListQueue.push(7);
    linkedListQueue.push(8);

    linkedListQueue.printQueue();

    System.out.println(linkedListQueue.peek());
    System.out.println(linkedListQueue.getLength());
  }

}
