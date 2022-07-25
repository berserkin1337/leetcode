class Solution {
public:
    int minTimeToVisitAllPoints(vector<vector<int>>& points) {
      int n = points.size();
      long long res = 0;
      for(int i=0;i<n-1;++i){
        
        res += max(abs(points[i+1][0] - points[i][0]) , abs(points[i+1][1]-points[i][1]) );
        // cout << abs(points[i+1][0] - points[i][0]) <<" " << abs(points[i+1][1]-points[i][1]) <<" " <<  i << endl;
      }
      return res;
      
    }
};