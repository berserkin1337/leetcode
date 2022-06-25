class Solution {
public:
    int minSteps(int n) {
        if (n == 1) return 0;
        int x[] = {3, 5, 7, 11, 13, 17, 19, 23, 29, 31};
        int sz = sizeof(x)/sizeof(int);
        int numops = 0;
        while (n > 1) {
            if (! (n&1)) {
                numops += 2;
                n >>= 1;
            }
            else {
                int i = 0;
                for (; i < sz && (n % x[i]); ++i); 
                if (i == sz) {
                    return numops + n;
                }
                else {
                    numops += x[i];
                    n /= x[i];
                }
            }
        }
        return numops;
    }};