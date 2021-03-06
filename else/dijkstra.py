graph = [defaultdict(int) for _ in range(n)]
for x,y,w in edgeList:
    graph[x].setdefault(y, w)
    if graph[x][y] > w:
        graph[x][y] = w
    graph[y].setdefault(x, w)
    if graph[y][x] > w:
        graph[y][x] = w            


def dijkstra(start):
    alr = set()
    dis = [float('inf') for _ in range(n)]
    dis[start] = 0
    heap = [(0,start)]
    while heap:
        _, cur = heapq.heappop(heap)
        alr.add(cur)
        for x, w in graph[cur].items():
            if x not in alr:
                dis[x] = min(dis[x], dis[cur] + w)
                heapq.heappush(heap, (dis[x],x))
        
        while heap and heap[0][1] in alr:
            heapq.heappop(heap)
    return dis
