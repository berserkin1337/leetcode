class Solution {
  vector<int> parent;
  int findParent(int x) { return (parent[x] == x) ? x : findParent(parent[x]); }

public:
  int findCircleNum(vector<vector<int>> &isConnected) {

    int n = isConnected.size();
    parent.resize(n, 0);
    for (int i = 0; i < n; ++i)
      parent[i] = i;
    int ans = n;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < i; ++j) {
        if (isConnected[i][j]) {
          int x = findParent(i);
          int y = findParent(j);
          if (x != y) {
            parent[y] = x;
            ans--;
          }
        }
      }
    }
    
    // for (int i = 0; i < (int)parent.size(); ++i) {
    //   if (parent[i] == i)
    //     ans++;
    // }
    return ans;
  }
};
