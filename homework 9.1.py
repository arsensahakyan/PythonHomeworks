# Ruben

# 1
# def buildPalindrome(string):
#     if string == string[::-1]:
#         return string
#     for i in range(len(string)):
#         if string[i:] == string[len(string):i-1:-1]:
#             return string+string[i-1::-1]
#
#
# print(buildPalindrome('ababab'))

# 2
# increasing_sequences = set()
# 
# def adding_sequences(k, n, length_of_seq, sequence):
#     if length_of_seq == k:
#         increasing_sequences.add(tuple(sequence))
#         return
#
#     i = 1 if (length_of_seq == 0) else (sequence[length_of_seq - 1] + 1)
#
#     length_of_seq += 1
#     while i <= n:
#         sequence[length_of_seq - 1] = i
#         adding_sequences(k, n, length_of_seq, sequence)
#         i += 1
#
#     length_of_seq -= 1
#
#
# def all_increasing_sequences(k, n):
#     seq = [0] * k
#     length_of_seq = 0
#     adding_sequences(k, n, length_of_seq, seq)
#     return increasing_sequences
#
# print(all_increasing_sequences(3, 5))
