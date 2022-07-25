class Solution {
public:
    vector<int> getRow(int rowIndex) {
        
        vector<vector<int> > pascTriangle;
        pascTriangle.push_back({1});
        pascTriangle.push_back({1,1});
        if (rowIndex <=1){
            return pascTriangle[rowIndex];
        }
        
        for(int i=2;i<=rowIndex;++i){
            vector<int> curr = {1};
            for(int j=1;j<i;++j){
                curr.push_back(pascTriangle[pascTriangle.size()-1][j] + pascTriangle[pascTriangle.size()-1][j-1] );
            }
            curr.push_back(1);
            pascTriangle.push_back(curr);
        }
        return pascTriangle[rowIndex];
    }
};