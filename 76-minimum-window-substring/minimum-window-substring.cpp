class Solution {
public:
    string minWindow(string s, string t) {
        vector<int> map(128,0);
        for(auto c: t) 
            map[c]++;
        int count=t.size(), begin=0, end=0, minSize=INT_MAX, head=0;
        //Traverse through string s.
        while(end<s.size()){
            //if value of char at index end in map is greater than 0
            //means it is part of string t, decrease counter
            //as we include it in current window.
            if(map[s[end++]]-- > 0) 
                count--;
            while(count==0){
                if(end-begin<minSize)  
                    minSize=end-(head=begin);
                //if value of char at index begin in map is 0
                //means it is part of string t (rest of chars will have negative map value), 
                //increase counter as we remove it from current window.
                if(map[s[begin++]]++ == 0) 
                    count++;
            }  
        }
        return minSize==INT_MAX? "":s.substr(head, minSize);
    }
};
