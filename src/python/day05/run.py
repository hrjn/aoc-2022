
import re
DAY = "05"
TYPE = "input"
PSTEP = 3

class CargoCrane(object):
    def __init__(self, file_path):
        header = []
        moves = []
        in_header = True
        with open(file_path, 'r') as f:
            for row in (f.readlines()):
                if len(row) == 1:
                    in_header = False
                    continue
                row.replace('\n', '')
                if in_header:
                    header.append(row)
                else:
                    moves.append(row.rstrip())
        header.reverse()
        # Stack index parsing
        stack_indexes = header[0].strip().replace(' ', '')
        self.state = {k: [] for k in stack_indexes}
        # Initial state creation
        for x in header[1:]:
            row = [' ' for _ in range(len(self.state))]
            row_cpt = 0
            i = 0
            while(i<len(x)):
                if x[i] == '[': # ]
                    row[row_cpt] = x[i:i+PSTEP]
                row_cpt += 1
                i += PSTEP+1
            for i, c in enumerate(row):
                if c != " ":
                    self.state[str(i+1)].append(c)
        
        # Now for the moves
        self.move_sequence = []
        for m in moves:
            m_parsed = []
            for w in m.split(" "):
                if w.isdigit():
                    m_parsed.append(w)
            cnt = int(m_parsed[0])
            while cnt > 0:
                cnt -= 1
                self.move_sequence.append([x for x in m_parsed[1:]])

        
        self.move_sequence_part2 = []
        for m in moves:
            m_parsed = []
            for w in m.split(" "):
                if w.isdigit():
                    m_parsed.append(w)
            self.move_sequence_part2.append(m_parsed)


    def get_stack_top(self):
        return {i: stack[-1] for (i, stack) in self.state.items()}


    def rearrange(self):
        for m in self.move_sequence:
            item = self.state[m[0]].pop()
            self.state[m[1]].append(item)
        return self

    def rearrange_part2(self):
        for m in self.move_sequence_part2:
            batch = self.state[m[1]][-(int(m[0])):]
            self.state[m[2]] += batch
            for _ in range(len(batch)):
                self.state[m[1]].pop()




file_path = f"../../../data/{DAY}_{TYPE}.txt"
cargo = CargoCrane(file_path)
cargo.rearrange_part2()
cargo.get_stack_top()
print(cargo.state)
