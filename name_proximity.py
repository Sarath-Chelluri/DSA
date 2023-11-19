def name_proximity_score(first, second):
    score = 0
    for i, j in enumerate(first):
        if j in second:
            if i == second.index(j):
                score += 2
            else:
                score += 1
    return score
print(name_proximity_score("ryaan", "najesh"))
