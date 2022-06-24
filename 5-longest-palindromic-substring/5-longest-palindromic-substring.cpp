class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        vector<vector<bool>> dp(n,vector<bool>(n,false));
        
        for(int i=0;i<n;++i){
            dp[i][i] = true;
            for(int j = i-1;j>=0;--j){
                if(s[i]==s[j]){
                    dp[i][j] =  (i==j+1)? true : dp[i-1][j+1];
                }
                else{
                    dp[i][j] = false;
                }
            }
        }
        string curr = "";
        for(int i=0;i<n;++i){
            for(int j=0;j<=i;++j){
                
                if (dp[i][j]&& curr.size()<i-j+1){
                    
                    curr = s.substr(j,i-j+1);
                }
            }
        }
        return curr;
    }
};