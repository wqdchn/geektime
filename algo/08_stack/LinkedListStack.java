package stack;

import linkedlist.ListNode;

/**
 * @program: algo
 * @description: 单链表实现的栈
 * @author: wqdong
 * @create: 2020-03-26 09:58
 **/
public class LinkedListStack {

  private ListNode top;
  private int size;

  public LinkedListStack() {
    top = null;
    size = 0;
  }

  // 入栈操作
  public void push(int val) {
    ListNode temp = new ListNode(val);
    if (top == null) {
      top = temp;
      size++;
    } else {
      temp.next = top; // 链表从头遍历，新入栈的结点放在头部
      top = temp;
      size++;
    }

  }

  // 出栈操作
  public int pop() {
    if (top == null) {
      System.out.println("栈空间为空！");
      return -1;
    }
    int pop = top.val;
    top = top.next;
    size--;
    return pop;
  }

  // 栈是否为空
  public boolean isEmpty() {
    return top == null;
  }

  // 栈空间当前元素个数
  public int size() {
    return size;
  }

  // 取得栈顶元素
  public int peek() {
    if (size == 0) {
      System.out.println("栈空间为空！");
      return -1;
    }

    return top.val;
  }

  // 输出栈信息
  public void printStack() {
    ListNode temp = top;
    while (temp != null) {
      System.out.print(temp.val + " ");
      temp = temp.next;
    }
    System.out.println();
  }

  public static void main(String[] args) {
    LinkedListStack linkedListStack = new LinkedListStack();

    linkedListStack.push(1);
    linkedListStack.push(2);
    linkedListStack.push(3);
    linkedListStack.push(4);
    linkedListStack.push(5);

    linkedListStack.printStack();

    System.out.println(linkedListStack.pop());
    System.out.println(linkedListStack.peek());
    System.out.println(linkedListStack.size());

    linkedListStack.printStack();

  }

}
