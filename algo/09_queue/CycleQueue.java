package queue;

/**
 * @program: algo
 * @description: 数组实现的循环队列
 * @author: wqdong
 * @create: 2020-03-26 14:30
 **/
public class CycleQueue {

  private int capacity = 11;
  private int head = 0;
  private int tail = 0;

  private int[] data = null;

  public CycleQueue() {
    this.capacity = capacity;
    this.data = new int[capacity];
  }

  // 入队操作
  public void push(int val) {
    if ((tail + 1) % capacity == head) {
      System.out.println("队列空间已满！不能入队！");
      return;
    } else {
      data[tail] = val;
      tail = (tail + 1) % capacity;
    }

  }

  // 出队操作
  public int poll() {
    if (head == tail) {
      System.out.println("队列为空！");
      return -1;
    }
    int poll = data[head];
    head = (head + 1) % capacity;
    return poll;
  }

  // 获取队列头部元素
  public int peek() {
    if (head == tail) {
      System.out.println("队列为空！");
      return -1;
    }
    int peek = data[head];
    return peek;
  }

  // 获取队列长度
  public int getLength() {
    return tail > head ? tail - head : capacity + tail - head;
  }

  // 输出队列信息
  public void printQueue() {

    for (int i = head; i % capacity != tail; i = (i + 1) % capacity) {
      System.out.print(data[i] + " ");
    }
    System.out.println();
  }

  public static void main(String[] args) {
    CycleQueue cycleQueue = new CycleQueue();

    cycleQueue.push(1);
    cycleQueue.push(2);
    cycleQueue.push(3);
    cycleQueue.push(4);
    cycleQueue.push(5);
    cycleQueue.push(1);
    cycleQueue.push(2);
    cycleQueue.push(3);
    cycleQueue.push(4);
    cycleQueue.push(5);

    cycleQueue.printQueue();

    cycleQueue.poll();
    cycleQueue.poll();

    cycleQueue.printQueue();

    cycleQueue.push(6);

    cycleQueue.printQueue();

    System.out.println(cycleQueue.peek());
    System.out.println(cycleQueue.getLength());

  }


}
