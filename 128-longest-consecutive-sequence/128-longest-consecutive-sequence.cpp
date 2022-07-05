class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
      if(nums.size()==0)return 0;
      unordered_set<int> s(nums.begin(),nums.end());
      int ans = 1;
      for(int n:nums){
        if(s.find(n)==s.end())continue;
        s.erase(n);
        int a  = n+1,b=n-1;
        while(s.find(a)!=s.end()){
          s.erase(a);
          a++;
        }
        while(s.find(b)!=s.end()) {
          s.erase(b);
          b--;
        }
        ans = max(ans,a-b-1);
      }
      return ans;
    }
};