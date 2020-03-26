package queue;

/**
 * @program: algo
 * @description: 数组实现的队列
 * @author: wqdong
 * @create: 2020-03-26 12:38
 **/
public class ArrayQueue {

  private int capacity = 5;

  private int[] data = null;
  private int head = 0;
  private int tail = 0;

  public ArrayQueue() {
    this.data = new int[capacity];
    this.capacity = capacity;
  }

  // 入队操作
  public void push(int val) {
    if (tail == capacity) {
      if (head == 0) { // 此时队列空间已满
        System.out.println("队列空间已满！不能入队！");
        return;
      } else { // 此时队列空间未满，元素往前挪动，腾出空间
        for (int i = head; i < tail; i++) {
          data[i - head] = data[i];
        }
        tail -= head;
        head = 0;
      }
    }
    data[tail] = val;
    tail++;
  }


  // 出队操作
  public int poll() {
    if (head == tail) {
      System.out.println("队列为空！");
      return -1;
    }
    int poll = data[head];
    head++;
    return poll;
  }

  // 获取队列头部元素
  public int peek() {
    if (head == tail) {
      return -1;
    }
    int peek = data[head];
    return peek;
  }

  // 队列元素个数
  public int getLength() {
    return tail - head;
  }

  // 输出队列信息
  public void printQueue() {
    for (int i = head; i < tail; i++) {
      System.out.print(data[i] + " ");
    }
    System.out.println();
  }

  public static void main(String[] args) {
    ArrayQueue arrayQueue = new ArrayQueue();
    arrayQueue.push(1);
    arrayQueue.push(2);
    arrayQueue.push(3);
    arrayQueue.push(4);
    arrayQueue.push(5);

    arrayQueue.printQueue();

    arrayQueue.poll();
    arrayQueue.poll();

    arrayQueue.printQueue();

    arrayQueue.push(6);
    arrayQueue.printQueue();

    System.out.println(arrayQueue.poll());
    System.out.println("队列头部元素 = "+ arrayQueue.peek());
    System.out.println("队列长度 = " + arrayQueue.getLength());

    arrayQueue.printQueue();
  }

}
