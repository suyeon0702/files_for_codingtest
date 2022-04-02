import sys

n, m = map(int, input().split())
x, y, d = map(int, input().split())
R = [list(map(int, input().split())) for _ in range(n)]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

visited = [[0 for _ in range(m)] for _ in range(n)]

def InRange(x, y):
    return 0 <= x and x < n and 0 <= y and y < m
        
def CanGo(x, y):
    return InRange(x, y) and R[x][y] == 0 and visited[x][y] == 0

def Go(x, y, d):
    d_cnt = 0
    for i in range(1, 5):
        dx = dy = (4-i)%4 # turn left
        new_x, new_y = x + dxs[dx], y + dys[dy]

        if CanGo(new_x, new_y):
            visited[new_x][new_y] = 1
            x, y = new_x, new_y
            Go(x, y, dx)
        else:
            d_cnt += 1
    
    if d_cnt == 4:
        Back(x, y, d)

def Back(x, y, d):
    back_x, back_y = x - dxs[d], y - dys[d]

    if not InRange(back_x, back_y) or R[back_x][back_y]:
        return
    else:
        x, y = back_x, back_y
        Go(x, y, d)
    

if CanGo(x, y):
    visited[x][y] = 1

Go(x, y, d)

acre = 0

for i in range(n):
    acre += sum(visited[i])

print(acre)

