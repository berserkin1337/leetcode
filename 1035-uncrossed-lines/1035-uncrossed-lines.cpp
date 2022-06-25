class Solution {
public:
    int maxUncrossedLines(vector<int>& nums1, vector<int>& nums2) {
        vector<vector<int>> dp(nums1.size(),vector<int> (nums2.size(),0));
        dp[0][0] = (nums1[0]==nums2[0])?1:0;
        for(int i=1;i<nums1.size();++i){
            dp[i][0] = (nums1[i]==nums2[0])?1:dp[i-1][0];
        }
        for(int i = 1;i<nums2.size();++i){
            dp[0][i] = (nums2[i]==nums1[0]) ? 1:dp[0][i-1];
        }
        
        for(int i=1;i<nums1.size();++i){
            for(int j=1;j<nums2.size();++j){
                if(nums1[i]==nums2[j]){
                    dp[i][j] = dp[i-1][j-1] + 1 ;
                }
                else{
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1]);
                }
            }
        }
        
        // for(int i=0;i<dp.size();++i){
        //     for(int j=0;j<dp[i].size();++j){
        //         cout << dp[i][j] << " ";
        //     }
        //     cout << "\n";
        // }
        
        return dp[nums1.size()-1][nums2.size()-1];
    }
};