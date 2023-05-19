# Project 4: Task 3 - Huffman Coding
# Variable sized encoding

from heapq import heappush, heappop, heapify
from collections import defaultdict
# to utilize the bitarray functionality one shall install a c++ version 14 and higher from
# https://visualstudio.microsoft.com/visual-cpp-build-tools/

from bitarray import bitarray


text = input("Input string: ")
string = text
freq_lib = defaultdict(int)  # generate a default library
for ch in text:              # count each letter and record into the frequency library
    freq_lib[ch] += 1

print(f"Frequency table:\n      ${freq_lib}")

heap = [[fq, [sym, ""]] for sym, fq in freq_lib.items()]  # '' is for entering the huffman code later

heapify(heap)  # transform the list into a heap tree structure

while len(heap) > 1:
    right = heappop(heap)  # heappop - Pop and return the smallest item from the heap
    left = heappop(heap)

    for pair in right[1:]:
        pair[1] = '0' + pair[1]  # add zero to all the right note
    for pair in left[1:]:
        pair[1] = '1' + pair[1]  # add one to all the left note
    heappush(heap, [right[0] + left[0]] + right[1:] + left[1:])

huffman_list = right[1:] + left[1:]
print("Huffman Code:\n     ",huffman_list)
huffman_dict = {a[0]: bitarray(str(a[1])) for a in huffman_list}

# Encoding
encoded_text = bitarray()
encoded_text.encode(huffman_dict, text)
print(f"The encoded text is:\n      {encoded_text}")

padding = 8 - (len(encoded_text) % 8)

with open('compressed_file.bin', 'wb') as w:
    encoded_text.tofile(w)

# Decoding
decoded_text = bitarray()

with open('compressed_file.bin', 'rb') as r:
    decoded_text.fromfile(r)

decoded_text = decoded_text[:-padding]  # remove padding

decoded_text = decoded_text.decode(huffman_dict)
decoded_text = ''.join(decoded_text)

print(f"The decoded text is:\n      {decoded_text}")

with open('uncompress.bin', 'w') as w:
    w.write(text)