from heapq import heappush, heappop
 
def solve():
    n = int(input())
    balls_dict = {}
    for _ in range(n):
        l, r = map(int, input().split())
        if l not in balls_dict:
            balls_dict[l] = []
        balls_dict[l].append(r)
 
    balls_key_list = [key for key in balls_dict]
    balls_key_list.sort()
 
    nxt = 1
    queue = []
    key_cnt = len(balls_key_list)
    balls_key_list.append(10**10)
    for i in range(key_cnt):
        l = balls_key_list[i]
        nxt_l = balls_key_list[i+1]
        nxt = max(nxt, l)
        for r in balls_dict[l]:
            heappush(queue, r)
 
        while nxt < nxt_l and len(queue) > 0:
            r = heappop(queue)
            if nxt > r:
                print("No")
                return
            nxt += 1
    print("Yes")
    return
 
t = int(input())
 
for _ in range(t):
    solve()