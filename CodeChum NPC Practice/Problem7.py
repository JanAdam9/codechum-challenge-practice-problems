# Dynamic Heat Map Analyzer

nt = input("Enter n and t: ")
nt = [int(x) for x in nt.split()]

n = nt[0]
t = nt[1]

print("Enter the grid:")

grid = []
for i in range (n):
    column = input()
    column = [int(x) for x in column.split()]
    grid.append(column)
    
heatmap = []
for i in range (n):
    a = []
    for j in range (n):
        a.append(0)
    heatmap.append(a)
    
def ZeroCheck(x):
    check = False
    for i in x:
        if i == 0:
            check = True
        return check
group = 1
for i in range (n):
    while ZeroCheck(heatmap[i]):
        
        if i == 0:
            heatmap[0][0] = 1
            for j in range (1,n):
                if abs(grid[i][j] - grid[i][j-1]) <= t:
                    heatmap[i][j] = heatmap[i][j-1]
                else:
                    group += 1
                    heatmap[i][j] = group
        elif i % 2 == 1:
            for j in range (n-1, -1, -1):
                if j == n:
                    if abs(grid[i][j] - grid[i-1][j]) <= t:
                        heatmap[i][j] = heatmap[i-1][j]
                    else:
                        group += 1
                        heatmap[i][j] = group
                else:
                    if abs(grid[i][j] - grid[i-1][j]) <= t:
                        heatmap[i][j] = heatmap[i-1][j]
                    elif abs(grid[i][j] - grid[i][j-1]) <= t:
                        heatmap[i][j] = heatmap[i][j-1]
                    else:
                        group += 1
                        heatmap[i][j] = group
        else:
            for j in range (n):
                if j == 0:
                    if abs(grid[i][j] - grid[i-1][j]) <= t:
                        heatmap[i][j] = heatmap[i-1][j]
                    else:
                        group += 1
                        heatmap[i][j] = group
                else:
                    if abs(grid[i][j] - grid[i-1][j]) <= t:
                        heatmap[i][j] = heatmap[i-1][j]
                    elif abs(grid[i][j] - grid[i][j-1]) <= t:
                        heatmap[i][j] = heatmap[i][j-1]
                    else:
                        group += 1
                        heatmap[i][j] = group

size = []
for i in range (1, group+1):
    a = 0
    for j in heatmap:
        a += j.count(i)
    size.append(a)

largestGroup = size.index(max(size))+1

for i in range (len(heatmap)):
    for j in range (len(heatmap)):
        if largestGroup == heatmap[i][j]:
            coordinates = (i,j)
            break
    else:
            continue
    break

print(f"Largest stable zone found at {coordinates} with size: {max(size)}")
