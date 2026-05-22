
# * making the huffman tree (using heap - bcs it's easier)
# * encoding function - dictionary with direct access to encodings
# * decoding function - traversing from the root of the tree to a leaf and then repeat until all symbols are read

from heap import Heap

class Node:
    def __init__(self, symbol=None, probability=None, left=None, right=None):
        self.symbol = symbol
        self.probability = probability
        self.left = left
        self.right = right
        self.encoding = None

    

class Tree:
    def __init__(self, root=None):
        self.root = root
        self.encoding = dict()          # for getting the encoding of a symbol directly

    # traverse the tree and assign encodings to the leaves
    def assign_encodings(self, node=None, encoding=""):
        if node is None:
            node = self.root

        if node.symbol is not None:
            self.encoding[node.symbol] = encoding
            node.encoding = encoding
            return
        
        self.assign_encodings(node.left, encoding + "0")
        self.assign_encodings(node.right, encoding + "1")

    # encode a sequence using this huffman tree
    def encode(self, seq):
        block_len = 2       # how many letters to take at a time
        block_count = 0     # how many letters are there currently collected in the block
        block = ""          # values in the block
        code = ""           # encoded version of seq
        for letter in seq:
            if (block_count < block_len):    
                block_count += 1 
                block += letter
            elif(block_count == block_len):
                block_count = 1 
                code += self.encoding[block]
                block = letter   
                
        code += self.encoding[block]
        return code       
    
    
    # not implementing error handling if sequence contains something other than 1 or 0
    def decode(self, encoded_seq):
        current = self.root
        decoded_seq = ""
        
        for bit in encoded_seq:
            if bit == '0':
                current = current.left
            elif bit == '1':
                current = current.right

            if current.symbol is not None:
                decoded_seq += current.symbol
                current = self.root

        return decoded_seq

def make_tree(nodes):
    heap = Heap()
    for node in nodes:
        heap.insert(node)

    while len(heap.heap) > 1:
        right = heap.extract_min()
        left = heap.extract_min()

        new_node = Node(symbol=None, probability=left.probability + right.probability, left=left, right=right)
        heap.insert(new_node)
    
    tree = Tree(root=heap.extract_min())
    tree.assign_encodings()
    return tree
