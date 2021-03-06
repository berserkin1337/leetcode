class Solution {
public:
    int countTriplets(vector<int>& A) {
        int i, j;
        int N = A.size();
        int Result = 0;
        
        vector<int> Map(1 << 16);
        
        for(i = 0; i < N; i++)
        {
            for(j = 0; j < N; j++)
            {
                Map[(A[i] & A[j])]++;
            }
        }
        
        for(i = 0; i < N; i++)
        {
            for(j = 0; j < (1 << 16); j++)
            {
                if((A[i] & j) == 0)
                {
                    Result += Map[j];
                }
                else
                {
                    j += (A[i] & j) - 1;
                }
            }
        }
        
        return Result;
    }
};
