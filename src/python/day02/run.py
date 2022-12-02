DAY = "02"
TYPE = "input"

file_path = f"../../../data/{DAY}_{TYPE}.txt"
data = [l.strip() for l in open(file_path)]

total_score = 0
shape_pts = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
outcome_pts = {'d': 3, 'w': 6, 'l': 0}
rules = {"A X": "d",
         "A Y": "w",
         "A Z": "l",
         "B X": "l",
         "B Y": "d",
         "B Z": "w",
         "C X": "w",
         "C Y": "l",
         "C Z": "d"}

for d in data:
    total_score += (outcome_pts[rules[d]] + shape_pts[d[-1]])

print(total_score)

rules_p2 = {"A X": "A Z",
            "A Y": "A X",
            "A Z": "A Y",
            "B X": "B X",
            "B Y": "B Y",
            "B Z": "B Z",
            "C X": "C Y",
            "C Y": "C Z",
            "C Z": "C X"}

total_score_p2 = 0
for d in data:
    d2 = rules_p2[d]
    score = shape_pts[d2[-1]] + outcome_pts[rules[d2]]
    print(f"{d} -> {d2} ({score})")
    total_score_p2 += score

print(total_score_p2)


