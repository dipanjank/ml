

class MinHeap:

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def left_child(self, i):
        """Left child of the i-th node is at index 2*i + 1"""
        return (2*i + 1, self.data[2*i + 1]) if (2*i + 1) < len(self.data) else (None, None)

    def right_child(self, i):
        """Right child of the i-th node is at index 2*i + 2"""
        return (2*i + 2, self.data[2*i + 2]) if (2*i + 2) < len(self.data) else (None, None)

    def get_parent(self, i):
        parent_index = (i - 1) // 2
        return parent_index, self.data[parent_index]

    def push(self, item):
        """Add the value at the end, increment size and the ensure that the heap property is maintained."""
        assert item is not None
        self.data.append(item)
        self.heapify_up(len(self.data)-1)

    def heapify_up(self, i):
        if i <= 0:
            return
        parent_index, parent = self.get_parent(i)
        if self.data[i] < parent:
            self.swap(parent_index, i)
            self.heapify_up(parent_index)

    def swap(self, i, j):
        """Swap the i and j-th elements."""
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def pop(self):
        """
        Return the top item (at index 0). If there are > 1 items,
        :return:
        """
        if not self.data:
            raise IndexError('Heap is empty!')

        result = self.data[0]
        self.data[0] = self.data[-1]
        del self.data[-1]
        self.heapify_down()
        return result

    def heapify_down(self, i=0):
        left_index, left = self.left_child(i)
        right_index, right = self.right_child(i)

        if left is None:
            return
        if right is None:
            min_index, min_val = left_index, left
        else:
            min_index, min_val = (left_index, left) if left < right else (right_index, right)

        if self.data[i] > min_val:
            self.swap(i, min_index)
            self.heapify_down(min_index)


if __name__ == '__main__':
    heap = MinHeap()

    for item in [2, 4, 10, 1, 5, 9]:
        heap.push(item)

    print(heap.pop(), len(heap))
    print(heap.pop(), len(heap))
    print(heap.pop(), len(heap))
    print(heap.pop(), len(heap))
    print(heap.pop(), len(heap))
    print(heap.pop(), len(heap))
