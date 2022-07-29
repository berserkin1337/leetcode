class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int n = nums.size();
        int count1(0),candidate1(INT_MIN),count2(0),candidate2(INT_MIN); 
        for(int  i=0;i<nums.size();++i) {
            if(nums[i] == candidate1) count1++;
            else if(nums[i] == candidate2) count2++;
            else if(!count1) candidate1 = nums[i],count1 = 1;
            else if(!count2) candidate2 = nums[i],count2 = 1;
            else count1-- , count2--;
        }
        int x = count(nums.begin(),nums.end(),candidate1);
        int y = count(nums.begin(),nums.end(),candidate2);
        vector<int> res;
        if(x>nums.size()/3) res.push_back(candidate1);
        if (y>nums.size()/3) res.push_back(candidate2);
        return res;

    }
};