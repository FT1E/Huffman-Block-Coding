# Huffman-Block-Coding
Structure of project
- tree.py
  - class Node - which represents a single node in a Huffman Tree - has symbol, probability, encoding and left/right child.
  - class Tree - represents the Huffman Tree - has encode and decode methods
  - make_tree function - which when given a list of nodes to be used as leaves, constructs an object of type Tree
- heap.py - heap / priority queue for elements of type Node sorted by their attribute probability
- main.py - demonstrating usage of the Huffman Tree - comment out the last block of lines (72 onwards) for testing it
