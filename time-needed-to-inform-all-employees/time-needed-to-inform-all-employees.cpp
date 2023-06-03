class Solution {
  int ans = 0;
  int curr_sum = 0;
  vector<bool> visited;
  void dfs(int x,vector<vector<int>>&adj, vector<int>& informTime){
    if(visited[x])return;
    visited[x] =  true;
    curr_sum+=informTime[x];
    for(auto i: adj[x]){
      dfs(i,adj,informTime);
    }
    ans = max(ans,curr_sum);
    curr_sum -=informTime[x];
  }
public:
    int numOfMinutes(int n, int headID, vector<int>& manager, vector<int>& informTime) {
        vector<vector<int>> adj(n,vector<int>(0));
        visited.resize(n,false);
        for(int i=0;i<n;++i){
          if(manager[i]!=-1)adj[manager[i]].push_back(i);
        }
        dfs(headID,adj,informTime);
        return ans;
    }
};
