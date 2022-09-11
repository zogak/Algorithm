import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
order = list(map(int, input().split()))

tab = []
ans = 0
to_pull = 0
to_pull_idx = 0

for i, item in enumerate(order):
    # 꽉 찬 경우
    if len(tab) == n:
        # 이미 꽂혀 있는 경우
        if item in tab:
            continue

        # 교체해야 하는 경우
        else:
            cur_index = i
            remains = order[cur_index+1:]
            for t in tab:
                # 더이상 나오지 않는 아이템이면 그 자리를 교체할 것임
                if t not in remains:
                    to_pull = t
                    break
                # 있는 아이템 중에서 젤 마지막에 나오는 아이템의 자리로 교체할 것임
                elif remains.index(t) > to_pull_idx:
                    to_pull = t
                    to_pull_idx = remains.index(t)

            #교체
            tab[tab.index(to_pull)] = item
            ans += 1
            to_pull = 0
            to_pull_idx = 0

    # 비어 있는 경우
    else:
        tab.append(item)

print(ans)