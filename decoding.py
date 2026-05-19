# from encoding import coded_seq
from tree import HuffmanTree

root = HuffmanTree.root
decoded_store = []
decoded_seq = ""

def decode_seq(encoded_seq):
    global decoded_seq

    current = root

    for bit in encoded_seq:
        if bit == '0':
            current = current.left
        elif bit == '1':
            current = current.right

        if current.symbol is not None:
            decoded_seq += current.symbol
            decoded_store.append(decoded_seq)
            current = root

    return decoded_seq

# Encoded seq
# print("Encoded seq: " + coded_seq)

# Decoded seq
# print("Decoded seq: " + decode_seq())