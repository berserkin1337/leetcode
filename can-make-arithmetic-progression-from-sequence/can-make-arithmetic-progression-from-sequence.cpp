#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool canMakeArithmeticProgression(vector<int>& arr) {
        sort(arr.begin(),arr.end());
        int n= arr.size();
        bool ans = true;
        for (int i = 1; i < n-1; i++)
        {
         /* code */
            if(arr[i]-arr[i-1] != arr[i+1]-arr[i]){
                ans = false;
            }
        }
         
         return ans;
        }
};
