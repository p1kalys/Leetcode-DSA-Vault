class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        # Transform group definition
        group = [ g - (g==-1) * i for i, g in enumerate(group)]

        # Collect group items
        G = defaultdict(list)
        for i, g in enumerate(group):
            G[g] += [i]
        
        def toposorted(items, outEdges, inEdgeCount, transform = lambda x: [x]):
            done = set()
            sortedList = []
            while True:
                findAny = False
                for item in items:
                    if item in done:
                        continue
                    if inEdgeCount[item] == 0:
                        findAny = True
                        for outEdge in outEdges[item]:
                            inEdgeCount[outEdge] -= 1
                        sortedList += transform(item)
                        done |= set([item])
                if len(done) == len(items):
                    return sortedList
                if findAny == False:
                    return []

        # Resolve toposort for each groups
        sortedGroups = {}
        beforeGroups = defaultdict(list)
        for g, items in G.items():
            outEdges = defaultdict(list)
            inEdgeCount = defaultdict(int)
            for item in items:
                for beforeItem in beforeItems[item]:
                    if beforeItem in items:
                        outEdges[beforeItem] += [item]
                        inEdgeCount[item] += 1
                    else:
                        beforeGroups[g] += [group[beforeItem]]
            sortedList = toposorted(items, outEdges, inEdgeCount)
            if not sortedList:
                return []
            sortedGroups[g] = sortedList

        # Resolve toposort between groups
        group = frozenset(group)
        outEdges = defaultdict(list)
        inEdgeCount = defaultdict(int)
        for g in group:
            for beforeGroup in beforeGroups[g]:
                outEdges[beforeGroup] += [g]
                inEdgeCount[g] += 1
        return toposorted(group, outEdges, inEdgeCount, lambda x: sortedGroups[x])

