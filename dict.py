words = ["hello", "bye", "ballon", "cat", "man"]
# by_letter = {}
from collections import defaultdict


by_letter = defaultdict(list)
print(by_letter)
for word in words:

    by_letter[word[0]].append(word)

print(by_letter)
