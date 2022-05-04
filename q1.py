words = ["PHP", "pyhon", "zekelabs"]
max_length = 0

for i in range(len(words)):
    length = len(words[i])
    if length > max_length:
        max_length = length
        max_word = words[i]

print("Longest Word Length =", max_length, "\nLongest Length Word =", max_word)
