#include <bits/stdc++.h>
using namespace  std;
// https://leetcode.com/problems/top-k-frequent-elements/
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int n = nums.size();
        unordered_map<int,int> mp;
        for(int i=0;i<n;++i){
            mp[nums[i]]++;
        }
        priority_queue<pair<int,int> > pq;
        for(auto it = mp.begin(); it != mp.end();it++){
            pq.push({it->second,it->first});
        }
        vector<int> ans;
        for(int i=0;i<k;++i){
            auto top = pq.top();
            ans.push_back(top.second);
            pq.pop();
        }

        return ans;

    }
};

int main() {
    Solution solution;
    vector<int> nums = {1};
    int k = 1;

    vector<int> ans = solution.topKFrequent(nums,k);
    for(int i=0;i<ans.size();++i){
        cout << ans[i] << " ";
    }

    return 0;
}
