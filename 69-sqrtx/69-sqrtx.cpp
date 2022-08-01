class Solution {
public:
    int mySqrt(int x) {
        long long low = 0 , high =  INT_MAX;
        while(low<=high){
            long long mid = (low + high)/2;
            if(mid*mid == x) return mid;
            
            if(mid*mid < x && (mid+1)*(mid+1)>x) return mid;
            else if(mid*mid > x) high = mid -1;
            else low = mid + 1;
        }
        return -1;
    }
};