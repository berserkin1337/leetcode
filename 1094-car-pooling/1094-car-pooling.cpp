class Solution {
public:
  bool carPooling(vector<vector<int>> &trips, int capacity) {
    int n = trips.size();
    multiset<pair<int,int>> inco_times;
    for(int i=0;i<trips.size();++i){
      inco_times.insert({trips[i][1],trips[i][0]});
      inco_times.insert({trips[i][2],-trips[i][0]});
    }
    int currPassengers=0;
    for(auto itr = inco_times.begin();itr!=inco_times.end();++itr){
      currPassengers += itr->second; 
      if(currPassengers>capacity)return false;
    }
    return true;
  }
};
