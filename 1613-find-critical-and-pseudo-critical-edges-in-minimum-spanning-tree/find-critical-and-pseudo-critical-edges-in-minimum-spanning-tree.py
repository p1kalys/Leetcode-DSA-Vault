class Solution:
    def find_mst(self,num_vertices, graph, init = None, exl = None):
        def visit(u):
            k[u] = True
            for v, w in graph.get(u, []):
                if exl and u in exl and v in exl:
                    continue
                if not k[v]:
                    heappush(tmp, (w, u, v))
        res = 0
        k = [False] * num_vertices
        tmp = []
        if init:
            u, v, w = init
            res += w
            k[u] = k[v] = True
            visit(u) or visit(v)
        else:
            visit(0)

        while tmp:
            w, u, v = heappop(tmp)
            if k[u] and k[v]: continue
            res += w
            if not k[u]:
                visit(u)
            if not k[v]:
                visit(v)
        
        return res if all(k) else inf
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = dict()
        for u, v, w in edges:
            graph.setdefault(u, []).append((v, w))
            graph.setdefault(v, []).append((u, w))
        temp = self.find_mst(n, graph)
        c_edge, p_edge = [], []
        for i in range(len(edges)):
            if self.find_mst(n, graph, exl = edges[i][:2]) > temp:
                c_edge.append(i)
            elif self.find_mst(n, graph, init = edges[i]) == temp:
                p_edge.append(i)
        return [c_edge, p_edge]
