from typing import Tuple

DAY = "03"
TYPE = "input"

SIZE_GROUP = 3

def get_prio(c: str) -> int:
    c_enc = ord(c)
    if c.islower():
        prio = c_enc - 96
    else:
        prio = c_enc - 38
    return prio

def get_common_char(s: Tuple[str,str]) -> str:
    return ''.join(set(s[0]).intersection(s[1]))

def get_cptms(r: str) -> Tuple[str,str]:
    size_cptm = int(len(d)/2)
    return (r[:size_cptm], r[size_cptm:])

file_path = f"../../../data/{DAY}_{TYPE}.txt"
data = [l.strip() for l in open(file_path)]

sum_prio = 0
cpt = 0
acc = []
for d in data:
    # Part 1
    # sum_prio += get_prio(get_common_char(get_cptms(d)))

    # Part 2
    cpt +=1
    acc.append(d)
    if cpt == 3:
        sum_prio += get_prio(get_common_char((get_common_char((acc[0], acc[1])),acc[2])))
        acc = []
        cpt = 0

print(sum_prio)
    




