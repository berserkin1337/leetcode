class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        // 100  & (1 << 31) = 1  << i  ;  i ++ 
        uint32_t x  = 1  << 31;
        uint32_t res = 0;
        int currPower = 0;
        while (x!=0) {
            uint32_t bit = (x & n) > 0? 1:0 ;
            // cout << bit <<  " " << x <<  endl;
            res |= (bit << currPower);
            currPower++;
            x >>= 1;
        }
        return res;
    }
};