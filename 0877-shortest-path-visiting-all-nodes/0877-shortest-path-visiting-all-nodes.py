class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:

        # n = total node count = height of adjacency matrix
        n = len(graph)

        # Initialize traversal queue
        # parameter of tuple: (node idx, state mask, visiting path length)
        traversal_queue = deque( [(node_idx, 1 << node_idx , 0) for node_idx in range(n) ] )


        visited = { (node_idx, 1 << node_idx ) for node_idx in range(n) }

        # Mask of all node visited
        all_node_visited = (1 << n) - 1

        # Launch BFS traversal from each node in graph G as source
        while traversal_queue:

            cur_node, cur_state, path_length = traversal_queue.popleft()

            # We've visited all nodes in graph G at least once
            if cur_state == all_node_visited:
                return path_length
            
            # Visit neighbor of current node
            for neighbor_idx in graph[cur_node]:

                next_state = cur_state | (1 << neighbor_idx)
                next_length = path_length + 1

                # If pair (neighbor index, next state) is not seen before
                if (neighbor_idx, next_state) not in visited:

                    traversal_queue.append( (neighbor_idx, next_state, next_length) )
                    visited.add( (neighbor_idx, next_state) )

        
        return -1