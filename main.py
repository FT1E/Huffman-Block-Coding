from tree import Node
import random

SYMBOLS = ['a', 'b', 'c', 'd', 'e', 'f']
PROBABILITIES = [0.05, 0.1, 0.15, 0.18, 0.22, 0.3]

alphabet = []
for i in range(6):
    for j in range(6):
        alphabet.append(Node(symbol=SYMBOLS[i] + SYMBOLS[j], probability=PROBABILITIES[i] * PROBABILITIES[j]))


def generate_random_word(length):
    if(length % 2 != 0):
        length += 1
    
    word = ""
    for i in range(length // 2):
        word += random.choices(alphabet, weights=[node.probability for node in alphabet])[0].symbol    
    return word
