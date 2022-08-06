class Solution {
public:
       int findPairs(vector<int>& v, int k) {
        sort(v.begin(),v.end());
        int ans=0,n=v.size();
        int j=1;
        for(int i=0;i<n-1;i++){
            while(j<=i || (j<n && v[j]-v[i]<k))j++;
            if(v[j]-v[i]==k)ans++;
            while(i+1<n && v[i+1]==v[i])i++;
        }
        return ans;
    }

};