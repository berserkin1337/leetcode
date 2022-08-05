class Solution {
public:
  int divide(int dividend, int divisor) {
     if (dividend == INT_MIN && divisor == -1) {
            return INT_MAX;
        }
    long divi = labs(dividend),dvs = labs(divisor),ans = 0;
    if(dividend==0){
        return 0;
    }
    
    int sign = dividend>0^divisor>0?-1:1;
    if(divi<dvs){
        return 0;
    }
    while(divi>=dvs){
        long tmp = dvs,m=1;
        while(tmp<<1 <=divi){
            tmp <<=1;
            m<<=1;
        }
        divi-=tmp;
        ans+=m;
    }
      return sign * ans;
  }
};
