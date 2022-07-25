class Solution {
public:
    bool canThreePartsEqualSum(vector<int>& arr) {
        long long totalSum = accumulate(arr.begin(),arr.end(),0);
        if (totalSum % 3 != 0) return false;
        int state = 0;
        int sum = 0;
        for(int i=0;i<arr.size();++i){
            sum += arr[i];
            if (sum == (state+1)*(totalSum/3)) {
                state += 1;
            }
        }
        return state>=3;
    }
};