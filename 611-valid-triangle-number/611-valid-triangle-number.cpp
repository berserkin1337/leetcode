class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        int n = nums.size();
        long long res = 0;
        sort(nums.begin(), nums.end());
        for (int i=1;i<nums.size()-1; ++i) {
            int k = i + 1;
            for(int j = 0;j < i ; ++j) {
                while ( k < n &&  nums[i] + nums[j]  > nums[k]) {
                    
                    res += (i - j);
                    k++;
                }
            }
        }
        return res;
    }
};