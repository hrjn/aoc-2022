from collections import Counter

DAY = "06"
TYPE = "input"
# WSIZE = 4 # part 1
WSIZE = 14

def has_only_unique_chars(s: str) -> bool:
    freq = Counter(s)
    if len(freq) == len(s):
        return True
    else:
        return False

file_path = f"../../../data/{DAY}_{TYPE}.txt"
with open(file_path, 'r') as f:
    data = f.readline()
ptr = 0
while ptr < len(data):
    w = data[ptr:ptr+WSIZE]
    is_marker = has_only_unique_chars(w)
    if is_marker:
        print(ptr+WSIZE)
        break
    ptr += 1
