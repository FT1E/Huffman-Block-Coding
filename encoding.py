from main import generate_random_word
from tree import Leaves

#Variables
word_len = 10
block = ""
code = ""
block_len = 2
block_store = []
block_count = 0
coded_seq = ""

#Getting the entire seq
seq = generate_random_word(word_len)

def iterate_seq(my_seq):

    global block_count, block, block_store, code

    for letter in my_seq:

        if (block_count < block_len):    
            block_count += 1 
            block += letter
        elif(block_count == block_len):
            block_count = 1
            block_store.append(block) 
            code += Leaves[block]
            block = letter   
            
    block_store.append(block)        
    code += Leaves[block]
    print(block_store)
    return code       

#Seq of the alphabet
#print(seq)
#coded seq
coded_seq = iterate_seq(seq)
#print(coded_seq)