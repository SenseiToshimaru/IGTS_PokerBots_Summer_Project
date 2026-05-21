def solve_psne(p1_matrix, p2_matrix):
    if not p1_matrix or not p1_matrix[0]:
        return []

    rows = len(p1_matrix)
    cols = len(p1_matrix[0])

    p1_best_responses = set()
    for col in range(cols):
        max_p1_val = max(p1_matrix[row][col] for row in range(rows))
        for row in range(rows):
            if p1_matrix[row][col] == max_p1_val: #Finding the index of the max value in each col
                p1_best_responses.add((row, col))

    p2_best_responses = set()
    for row in range(rows):
        max_p2_val = max(p2_matrix[row][col] for col in range(cols))
        for col in range(cols):
            if p2_matrix[row][col] == max_p2_val:
                p2_best_responses.add((row, col))

    psne = p1_best_responses.intersection(p2_best_responses) #best of both worlds

    return sorted(list(psne))

n, m = map(int, input().split())

p1 = []
for _ in range(n):
    row = list(map(int, input().split()))
    p1.append(row)

p2 = []
for _ in range(m):
    row = list(map(int, input().split()))
    p2.append(row)

result = solve_psne(p1, p2)
print(result)