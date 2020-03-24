package array;

/**
 * @program: algo
 * @description: 实现一个支持动态扩容的数组
 * @author: wqdong
 * @create: 2020-03-24 07:18
 **/
public class GenericArray<T> {

  private T[] data;
  private int size;


  // 根据传入的容量capacity构造一个数组
  public GenericArray(int capacity) {
    data = (T[]) new Object[capacity];
    size = 0;
  }

  // 无参构造方法，并设置默认数组容量
  public GenericArray() {
    this(10);
  }

  // 获取数组容量
  public int getCapacity() {
    return data.length;
  }

  // 获取数组当前元素个数
  public int getSize() {
    return size;
  }

  // 判断数组是否为空
  public boolean isEmpty() {
    return size == 0;
  }

  // 根据传入的索引值index和元素值value，修改对应位置上的值
  public void set(int index, T value) {
    if (index < 0 || index >= size) {
      throw new IllegalArgumentException("index有越界风险！");
    }
    data[index] = value;
  }

  // 根据传入的索引值index，获取对应位置上的元素值
  public T get(int index) {
    if (index < 0 || index >= size) {
      throw new IllegalArgumentException("index有越界风险！");
    }
    return data[index];
  }

  // 根据传入的元素值value，查看数组是否包含该元素
  public boolean contains(T value) {
    for (T e : data) {
      if (e.equals(value)) {
        return true;
      }
    }
    return false;
  }

  // 根据传入的元素值value，查找数组中对应的下标索引值，若无则返回-1
  public int find(T value) {
    for (int i = 0; i < size; i++) {
      if (data[i].equals(value)) {
        return i;
      }
    }
    return -1;
  }

  // 根据传入的索引index值和元素值value，进行插入操作
  public void insert(int index, T value) {
    if (index < 0 || index > size) {
      throw new IllegalArgumentException("index有越界风险！");
    }

    // 先检查当前元素个数与数组容量关系
    if (size == data.length) {
      resize(2 * data.length);
    }

    for (int i = size - 1; i >= index; i--) {
      data[i + 1] = data[i];
    }

    data[index] = value;
    size++;
  }

  // 数组扩容方法
  public void resize(int capacity) {
    T[] nData = (T[]) new Object[capacity];

    for (int i = 0; i < size; i++) {
      nData[i] = data[i];
    }

    data = nData;
  }

  // 向数组头部插入元素
  public void addFirst(T value) {
    insert(0, value);
  }

  // 向数组尾部插入元素
  public void addLast(T value) {
    insert(size, value);
  }

  // 根据传入的索引值index，删除对应位置上的元素
  public T remove(int index) {
    if (index < 0 || index >= size) {
      throw new IllegalArgumentException("index有越界风险！");
    }

    T rm = data[index];

    for (int i = index + 1; i < size; i++) {
      data[i - 1] = data[i];
    }

    size--;
    data[size] = null;

    // 缩容
    if (size == data.length / 4 && data.length / 2 != 0) {
      resize(data.length / 2);
    }

    return rm;
  }

  // 删除数组头部元素
  public T removeFirst() {
    return remove(0);
  }

  // 删除数组尾部元素
  public T removeLast() {
    return remove(size - 1);
  }

  // 根据传入的元素值value，删除数组中的该元素
  public void removeElement(T value) {
    int index = find(value);
    if (index != -1) {
      remove(index);
    }
  }

  // 输出数组信息
  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append(String.format(
        "数组容量为 %d, 当前元素个数为 %d", data.length, size
    ));

    sb.append(" [");
    for (int i = 0; i < size; i++) {
      sb.append(data[i]);
      if (i != size - 1) {
        sb.append(",");
      }
    }
    sb.append("]");
    return sb.toString();
  }
}
