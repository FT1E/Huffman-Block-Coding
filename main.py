from tree import Node, Leaves
import random
import math

from encoding import encode_seq
from decoding import decode_seq

SYMBOLS = ['a', 'b', 'c', 'd', 'e', 'f']
PROBABILITIES = [0.05, 0.1, 0.15, 0.18, 0.22, 0.3]

alphabet = []
for i in range(6):
    for j in range(6):
        alphabet.append(Node(symbol=SYMBOLS[i] + SYMBOLS[j], probability=PROBABILITIES[i] * PROBABILITIES[j]))


non_compressed_code = {}
non_compressed_code_length = math.ceil(math.log2(len(alphabet)))
bits = [0 for _ in range(non_compressed_code_length)]
for node in alphabet:
    
    non_compressed_code[node.symbol] = "".join([str(x) for x in bits])
    for i in range(non_compressed_code_length-1,0, -1):
        bits[i] = (bits[i] + 1) % 2
        if bits[i] == 1:
            break   # * no carry, so stop
    
# print(non_compressed_code)

def generate_random_word(length):
    if(length % 2 != 0):
        length += 1
    
    word = ""
    for i in range(length // 2):
        word += random.choices(alphabet, weights=[node.probability for node in alphabet])[0].symbol    
    return word


expected_code_length = 0
for node in alphabet:
    expected_code_length += node.probability * len(Leaves[node.symbol])
    # print(f"Probability: {round(node.probability, 4)}\t\t Encoding length: {len(Leaves[node.symbol])} \t\t Symbol: {node.symbol} \t\t Encoding: {Leaves[node.symbol]}")

print(f"Expected code length: {expected_code_length}")
non_compressed_expected_codelength = non_compressed_code_length
print(f"Non-compressed: {non_compressed_expected_codelength}")

alt_alphabet = []
print(PROBABILITIES)
PROBABILITIES[0], PROBABILITIES[5] = PROBABILITIES[5], PROBABILITIES[0]
print(PROBABILITIES)
for i in range(6):
    for j in range(6):
        alt_alphabet.append(Node(symbol=SYMBOLS[i] + SYMBOLS[j], probability=PROBABILITIES[i] * PROBABILITIES[j]))

alt_expected_code_length = 0
for node in alt_alphabet:
    alt_expected_code_length += node.probability * len(Leaves[node.symbol]) 

print(f"Expected length assuming the input has flipped probabilities: {alt_expected_code_length}")

# seq = generate_random_word(20)
# encoded = encode_seq(seq)
# decoded = decode_seq(encoded)

# print(f"Original Sequence:\t {seq}")
# print(f"Encoding of sequence:\t {encoded}")
# print(f"Decoding of encoding:\t {decoded}")

# print(f"Decoding of encoding == original: {seq == decoded}")