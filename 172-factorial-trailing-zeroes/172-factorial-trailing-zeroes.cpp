class Solution {
public:
    int trailingZeroes(int n) {
        // n_2 >= n_5
        long long res = 0;
        int i = 5;
        while (i<=n){
            
            res += (long long)((int)n/(int)i);
            i*=5;
        }
        return res;
    }
};