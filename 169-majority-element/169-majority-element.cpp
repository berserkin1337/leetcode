class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int,int> counter;
        for(int i=0;i<nums.size();++i) {
            counter[nums[i]]++;
        }
        
        int max_element;
        int max_num = INT_MIN;
        for(auto it = counter.begin();it!= counter.end();++it){
            if(it->second > max_num){
                max_element = it->first;
                max_num = it->second;
            }
        }
        
        return max_element;
    }
};