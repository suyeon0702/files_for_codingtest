#조삼모사

n = int(input())
P = [list(map(int, input().split())) for _ in range(n)]


M = []
gap = []

# P 조합
def work_pair(curr_work, cnt_m):
    if cnt_m == n//2:
        E = []
        
        for i in range(1, n+1):
            if i not in M:
                E.append(i)
    
        d = tot_press(M) - tot_press(E)

        if d >= 0:
            gap.append(d)
        else:
            gap.append(-d)

                
        return
    
    if curr_work == n+1:
 
        return

    M.append(curr_work)
    work_pair(curr_work + 1, cnt_m + 1)
    M.pop()

    work_pair(curr_work + 1, cnt_m)

def tot_press(works):
    tot = 0
    for i in works:
        for j in works:
            if j != i:
                tot += P[i-1][j-1]
    return tot
    

work_pair(1, 0)
print(min(gap))



