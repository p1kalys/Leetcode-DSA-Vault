class Solution // Unbounded Knapsack
{
public:
    map<vector<int>,int> m;
    int shoppingOffers(vector<int>& price, vector<vector<int>>& special, vector<int>& needs) 
    {
        int n=price.size();
        int withoutOffer=0;
        for(int x=0; x<n; x++) withoutOffer+=price[x]*needs[x];
        int mn=withoutOffer;
        if(m.find(needs)!=m.end()) return m[needs];
        for(int x=0; x<special.size(); x++)
        {
            int f=1;
            for(int y=0; y<n; y++) 
            {
                if(special[x][y]>needs[y])
                {
                    f=0; break;
                }
            }
            if(f)
            {
                vector<int> newneeds(n);
                for(int y=0; y<n; y++)
                {
                    newneeds[y]=needs[y]-special[x][y];
                }
                int offer=special[x][n]+shoppingOffers(price,special,newneeds);
                if(offer<mn) mn=offer;
            }
        }
        return m[needs]=mn;
    }
};