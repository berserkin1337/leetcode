class Solution {
    class tuple {
        public:
        int node;
        int mask;
        int cost;
        tuple(int node,int mask,int cost) {
            this->node = node;
            this->mask = mask;
            this->cost = cost;
        }
    };
    
public:
    
    int shortestPathLength(vector<vector<int>>& graph) {
        int n = graph.size();
        queue<tuple> q;
        set<pair<int,int>> s;
        // int n = graph.size();
        int all = (1<<n ) - 1;
        for(int i=0;i<n;++i) {
            int temp = (1<<i);
            tuple curr(i,temp,1);
            // temp dist(i,temp,0);
            q.push(curr);
            s.insert({i,temp});
        }
        while(!q.empty()) {
            tuple curr = q.front();
            q.pop();
            if(curr.mask == all) return curr.cost - 1;
            
            for(auto i:graph[curr.node]) {
                int currMask = curr.mask;
                int mask = curr.mask | (1<<i);
                
                //node corresponding to this path 
                tuple currTuple(i,mask,curr.cost + 1);
                // tuple forSet(i,mask,0);
                if(s.find({i,mask}) == s.end()) {
                    s.insert({i,mask});
                    q.push(currTuple);
                }
                
            }
        }
        
        return -1;
    }
};