class Solution {
private:
    class DisjointSet
    {
        private:
            vector <int> parent, size;
        public:
            DisjointSet (int n)
            {
                parent.resize(n + 1);
                size.assign(n + 1, 1);
                for(int i = 0; i <= n; i++)
                {
                    parent[i] = i;
                }
            }
            int findParent(int p)
            {
                if(p == parent[p])
                {
                    return p;
                }
                return parent[p] = findParent(parent[p]);
            }
            int findSize(int p)
            {
                return size[p];
            }
            void unionBySize (int u, int v)
            {
                int p = findParent(u), q = findParent(v);
                if(p == q)
                    return;
                if(size[p] < size[q])
                {
                    parent[p] = q;
                    size[q] += size[p];
                }
                else
                {
                    parent[q] = p;
                    size[p] += size[q];
                }
            }
    };
public:
    int makeConnected(int n, vector<vector<int>>& grid) {
        int connections = 0, m = grid.size(), moves = 0;
        DisjointSet ds(n);
        for(int i = 0; i < m; i++)
        {
            ds.unionBySize(grid[i][0], grid[i][1]);//connecting those components which are already connected.
            connections++;//counting those connections.
        }
        if(connections < n - 1)// if the number of connections is lesser than n - 1, it is impossible to form further connnections.
        {
            return -1;
        }
        int maxSize = 0, p = 0;
        for(int i = 0; i < n; i++)
        {
            if(ds.findSize(i) > maxSize)//finding the parent with maximum size.
            {
                p = i;
                maxSize = ds.findSize(i);
            }
        }
        for(int i = 0; i < n; i++)
        {
            if(ds.findParent(i) == i && i != p)
            {
                ds.unionBySize(i, p);
                moves++;
            }
        }   
        return moves;
    }
};