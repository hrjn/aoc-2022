DAY = "07"
TYPE = "input"

MAX_DIR_SIZE= 100000
DISK_SPACE = 70000000
REQUIRED_SPACE_FOR_UPGRADE = 30000000

file_path = f"../../../data/{DAY}_{TYPE}.txt"
data = [l.strip() for l in open(file_path)]
size = {'/': 0}
cwd = []

for d in data:
    line = d.split(' ')
    if line[0] == '$':
        if line[1] == "ls":
            pass
        if line[1] == "cd":
            if line[2] == "..":
                cwd.pop()
            elif line[2] == "/":
                cwd.append('/')
            else:
                if cwd[-1] == '/':
                    cwd.append(line[2])
                else:
                    cwd.append(f"{cwd[-1]}/{line[2]}")
    elif line[0] == "dir":
        pass
    else:
        for c in cwd:
            if c not in size.keys():
                size[c] = int(line[0])
            else:
                size[c] += int(line[0])

# Part 1
sizes_filtered = sum([s for s in size.values() if s <= MAX_DIR_SIZE])
print(sizes_filtered)

# Part 2
disk_spake_taken = DISK_SPACE - size['/']
deletable_dir_sizes = [s for s in size.values() if s >= REQUIRED_SPACE_FOR_UPGRADE - disk_spake_taken]
print(min(deletable_dir_sizes))
    
