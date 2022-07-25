class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();
        int i = n-1;
        while (i>=0) {
            if(digits[i]  < 9 ){
                digits[i] += 1;
                return digits;
            }
            digits[i] = 0;
            i -=1;
        }
        digits[0] = 1;
        digits.push_back(0);
        return digits;
    }
};