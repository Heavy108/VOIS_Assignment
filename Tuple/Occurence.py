t = (1, 2, 3, 2, 4, 2, 5)

visited = []

for i in t:
    if i not in visited:
        count = 0
        for j in t:
            if i == j:
                count += 1
        print(i, "->", count)
        visited.append(i)
