# 1157
from collections import Counter
word = input()
word = word.upper()
counter = Counter(word)
max_count = max(counter.values())
result = []
for w, c in counter.items():
    if c == max(counter.values()):
        result.append(w)
if len(result) != 1:
    print("?")
else:
    print(result[0])