class Solution {
public:
  bool searchMatrix(vector<vector<int>> &matrix, int target) {
    int m = matrix.size();
    int n = matrix[0].size();
    // find the row where target could be then find the column
    int low = 0, high = m - 1;
    int mid=0;
    while (low <= high) {
      mid = low + (high - low) / 2;
      if (matrix[mid][0] <= target &&
          matrix[mid][n - 1] >= target) {
        break;
      } else if (target > matrix[mid][n - 1])low = mid + 1;
       else high = mid-1;
      
    }
    
    if (low > high){
        cout   << "yo";    
        return false;
    }
    low = 0, high = n-1;
    while (low <= high) {
      int middle = low + (high -low)/ 2;
      int medium = matrix[mid][middle];
      cout  << low << " "<< high << endl;
      if(medium==target) return true;
      else if(medium> target) high = middle-1;
      else low = middle + 1;
      cout  << low << " "<< high << endl;   
    }
    // cout << "hi";
    return false;
  }
};
