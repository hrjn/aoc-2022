INPUT = "data.txt"

data = [l.strip() for l in open(INPUT)]
acc = 0
s = []

for x in data:
    if x:
        acc += int(x)
    else:
        s.append(acc)
        acc = 0
if acc != 0:
    s.append(acc)

s.sort(reverse=True)
print(s[0])
print(sum(s[:3]))



