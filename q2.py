word = 'the quick brown fox jumps over the lazy dog.'
count = 1

for i in range(len(word)):
    if word[i] == ' ':
        count += 1

print("Total number of words =", count)
