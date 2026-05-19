
# todo - making the huffman tree (using heap - bcs it's easier)
# todo - encoding function - dictionary with direct access to leaves
# todo - decoding function - traversing from the root of the tree to a leaf and then repeat until all symbols are consumed

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

    # traverse the tree and assign encodings to the leaves
    def assign_encodings(self, node=None, encoding=""):
        if node is None:
            node = self.root

        if node.symbol is not None:
            node.encoding = encoding
            return
        
        self.assign_encodings(node.left, encoding + "0")
        self.assign_encodings(node.right, encoding + "1")



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


SYMBOLS = ['a', 'b', 'c', 'd', 'e', 'f']
PROBABILITIES = [0.05, 0.1, 0.15, 0.18, 0.22, 0.3]

alphabet = []
for i in range(6):
    for j in range(6):
        alphabet.append(Node(symbol=SYMBOLS[i] + SYMBOLS[j], probability=PROBABILITIES[i] * PROBABILITIES[j]))


HuffmanTree = make_tree(alphabet)
HuffmanTree.assign_encodings()
Leaves = {}
for a in alphabet:
    Leaves[a.symbol] = a.encoding
    # print(f"Symbol: {a.symbol}\tEncoding: {a.encoding}")