# heap with custom elements for making the huffman tree


class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, node):
        self.heap.append(node)
        current = len(self.heap) - 1

        while current >= 0:
            parent = self.get_parent_index(current)

            # if current node has probability smaller than parent
            if self.heap[current].probability < self.heap[parent].probability:
                self.heap[current], self.heap[parent] = self.heap[parent], self.heap[current]
                current = parent
            else:
                break

    def get_min(self):
        return self.heap[0]
    
    def remove_min(self):
        current = 0
        while True:
            left = self.get_left_child_index(current)
            right = self.get_right_child_index(current)

            if left >= len(self.heap):
                self.heap[current], self.heap[-1] = self.heap[-1], self.heap[current]
                self.heap.pop()
                break
            elif right >= len(self.heap):
                self.heap[current], self.heap[left] = self.heap[left], self.heap[current]
                self.heap.pop()
                break
            else:
                if self.heap[left].probability < self.heap[right].probability:
                    self.heap[current], self.heap[left] = self.heap[left], self.heap[current]
                    current = left
                else:
                    self.heap[current], self.heap[right] = self.heap[right], self.heap[current]
                    current = right
            

    def extract_min(self):
        min = self.get_min()
        self.remove_min()
        return min
    
    def get_parent_index(self, index):
        return (index - 1) // 2
    
    def get_left_child_index(self, index):
        return 2 * index + 1
    
    def get_right_child_index(self, index):
        return 2 * index + 2