from tree import *
import random
import math

SYMBOLS = ['a', 'b', 'c', 'd', 'e', 'f']
PROBABILITIES = [0.05, 0.1, 0.15, 0.18, 0.22, 0.3]

alphabet = []
for i in range(6):
    for j in range(6):
        alphabet.append(Node(symbol=SYMBOLS[i] + SYMBOLS[j], probability=PROBABILITIES[i] * PROBABILITIES[j]))



# generates a random word using the given probabilites
def generate_random_word(length):
    if(length % 2 != 0):
        length += 1
    
    word = ""
    for i in range(length // 2):
        word += random.choices(alphabet, weights=[node.probability for node in alphabet])[0].symbol    
    return word


def calculate_expected_length(probabilities, lenghts):
    res = 0    
    for i in range(len(probabilities)):
        res += probabilities[i] * lenghts[i]
    return res


huffman_tree = make_tree(alphabet)


non_compressed_expected_length = math.ceil(math.log2(len(alphabet)))
huffman_expected_length = calculate_expected_length([x.probability for x in alphabet], [len(x.encoding) for x in alphabet])

# expected length with flipped probabilites
ALT_PROBABILITIES = list(PROBABILITIES)     # get a copy - so original isn't modified

# swap probabilities
ALT_PROBABILITIES[0], ALT_PROBABILITIES[5] = ALT_PROBABILITIES[5], ALT_PROBABILITIES[0]
print(ALT_PROBABILITIES)
alt_alphabet = []
for i in range(len(SYMBOLS)):
    for j in range(len(SYMBOLS)):
        alt_alphabet.append(Node(symbol=SYMBOLS[i] + SYMBOLS[j], probability=ALT_PROBABILITIES[i] * ALT_PROBABILITIES[j]))


flipped_expected_length = calculate_expected_length([x.probability for x in alt_alphabet], [len(x.encoding) for x in alphabet])

# print(f"Non-compressed expected codeword length: {non_compressed_expected_length}")
# print(f"Compressed with Huffman expected codeword length: {huffman_expected_length}")
# print(f"With flipped probabilities: {flipped_expected_length}")


compression_ratio = non_compressed_expected_length / huffman_expected_length

# compression ratio if probabilities are flipped for 'a' and 'f'
alt_compression_ratio = non_compressed_expected_length / flipped_expected_length

print(f"Compression ratio with original probabilities:\t{compression_ratio}")
print(f"Compression ratio with flipped probabilities:\t{alt_compression_ratio}")



# You can uncomment below for generating a random word with original probabilities, encode it, decode the encoding

# seq = generate_random_word(1000)        # replace 1000 with any positive number
# encoded = huffman_tree.encode(seq)
# decoded = huffman_tree.decode(encoded)

# print(f"Original Sequence:\t {seq}")
# print(f"Encoding of sequence:\t {encoded}")
# print(f"Decoding of encoding:\t {decoded}")
# print(f"Decoding of encoding == original: {seq == decoded}")