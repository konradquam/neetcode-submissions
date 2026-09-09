class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        #build the graph as ajacency lists
        graph = {}
        for start, end, weight in edges:
            if start not in graph.keys():
                graph[start] = [(end, weight)]
            else:
                graph[start].append((end, weight))
        min_heap = []
        distances = {i: math.inf for i in range(n)}

        #initialize src distance
        distances[src] = 0

        heapq.heappush(min_heap, (distances[src], src))

        while min_heap:
            dist, node = heapq.heappop(min_heap)

            if node not in graph.keys():
                continue
            for next_node, next_dist in graph[node]:
                if dist + next_dist < distances[next_node]:
                    distances[next_node] = dist + next_dist
                    heapq.heappush(min_heap, (dist+next_dist, next_node))
        
        for node, weight in distances.items():
            if weight == math.inf:
                distances[node] = -1
        return distances

