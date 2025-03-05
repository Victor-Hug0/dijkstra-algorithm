class MinHeap:
    def __init__(self):
        self.heap = []
        
    def _left_child(self, index):
        return 2 * index + 1
    
    def _right_child(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index-1) // 2
    
    def _heapify_up(self, index):
        if index == 0:
            return
        
        parent_index = self._parent(index)
        
        if self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)
            
    def _heapify_down(self, index):
        size = len(self.heap)
        left_index = self._left_child(index)
        right_index = self._right_child(index)
        
        smallest_index = index
        
        if left_index < size and self.heap[left_index] < self.heap[smallest_index]:
            smallest_index = left_index
        if right_index < size and self.heap[right_index] < self.heap[smallest_index]:
            smallest_index = right_index
            
        if smallest_index != index:
            self.heap[index], self.heap[smallest_index] = self.heap[smallest_index], self.heap[index]
            self._heapify_down(smallest_index)
            
    def show_heap(self):
        print(self.heap)
            
    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
        
    def pop_min(self):
        if len(self.heap) == 0:
            raise IndexError("Heap está vazio")
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        
        return root

