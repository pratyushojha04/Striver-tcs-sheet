mp = {}
print(x, mp[x])
for i in range(n):
    if arr[i] in mp:
        mp[arr[i]] += 1
    else:
        mp[arr[i]] = 1
for x in mp:
    print(x,mp[x])






visited = [False] * n
    for i in range(n):
        if (visited[i] == True):
            continue
        count = 1
        for j in range(i + 1, n):
            if (arr[i] == arr[j]):
                visited[j] = True
                count += 1
        print(arr[i], count)