package stack;

/**
 * @program: algo
 * @description: 数组实现的顺序栈
 * @author: wqdong
 * @create: 2020-03-26 09:02
 **/
public class ArrayStack {

  private int capacity = 5;
  private int length = 0;

  private int[] data = null;

  // 初始化操作
  public ArrayStack() {
    this.data = new int[capacity];
    this.capacity = capacity;
    this.length = 0;
  }

  // 入栈操作
  public void push(int val) {
    if (capacity == length) {
      System.out.println("栈空间已满！不能入栈！");
      return;
    }

    data[length] = val;
    length++;
  }

  // 出栈操作
  public int pop() {
    if (length == 0) {
      System.out.println("栈空间为空！");
      return -1;
    }

    int pop = data[length - 1];
    length--;
    return pop;
  }

  // 栈是否为空
  public boolean isEmpty() {
    return length == 0;
  }

  // 栈空间当前元素个数
  public int size(){
    return length;
  }

  // 取得栈顶元素
  public int peek() {
    if (length == 0) {
      System.out.println("栈空间为空！");
      return -1;
    }

    int top = data[length - 1];
    return top;
  }

  // 输出栈信息
  public void printStack(){
    for (int i = 0; i < length; i++){
      System.out.print(data[i] + " ");
    }
    System.out.println();
  }

  public static void main(String[] args){
    ArrayStack arrayStack = new ArrayStack();

    arrayStack.push(1);
    arrayStack.push(2);
    arrayStack.push(3);
    arrayStack.push(4);
    arrayStack.push(5);

    arrayStack.printStack();

    System.out.println(arrayStack.pop());
    System.out.println(arrayStack.peek());
    System.out.println(arrayStack.size());

    arrayStack.printStack();

  }
}
