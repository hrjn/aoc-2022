from typing import List, Dict

DAY = "04"
TYPE = "input"

SIZE_BINVEC_SAMPLE = 9
SIZE_BINVEC_INPUT = 99

file_path = f"../../../data/{DAY}_{TYPE}.txt"
data = [l.strip() for l in open(file_path)]

def has_overlap(s: str, size_binvec: int, part: str) -> bool:
    asgns = [x.split('-') for x in s.split(',')]
    bin_vecs = []
    sizes = []
    for a in asgns:
        bnd = [int(x)-1 for x in a]
        sizes.append(len(range(bnd[0], bnd[1]))+1)
        vec = ''
        for i in range(size_binvec):
            if i in range(bnd[0], bnd[1]+1):
                vec += '1'
            else:
                vec += '0'
        bin_vecs.append(int(vec, base=2))
    overlap = format(bin_vecs[0] & bin_vecs[1], 'b').replace('0', '')
    if overlap:
        if part == '1':
            if len(overlap) == min(sizes):
                return True
            else:
                return False
        return True
    return False

s = 0
for d in data:
    if has_overlap(d, SIZE_BINVEC_INPUT, part='1'):
        s += 1
print(s)


