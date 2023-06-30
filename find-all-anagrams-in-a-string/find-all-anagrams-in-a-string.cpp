class Solution {
public:
    string count_sort(string& s){
        int n=s.size();
        vector<int>mp(26,0);
        string ans;
        for(int i=0;i<n;i++){
            mp[s[i]-'a']++;
        }
        for(int i=0;i<26;i++){
           ans.append(mp[i],i+'a');
        }
        return ans;
    }
    
    vector<int> findAnagrams(string s2, string s1) {
        int n=s1.size(),m=s2.size();
        vector<int>v;
        sort(begin(s1),end(s1));
        for(int i=0;i<m-n+1;i++){
            string temp=s2.substr(i,n);
           
            if(s1==count_sort(temp))v.push_back(i);
        }
        return v;
    }
};