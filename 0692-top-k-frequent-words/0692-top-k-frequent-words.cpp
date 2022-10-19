class Solution {
public:
    struct compare {
        bool operator()(pair<int,string> p1,pair<int,string>p2) {
            return p1.first == p2.first ? p1.second > p2.second : p1.first < p2.first;
        }
    };
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string,int> mp;
        for(int i=0;i<words.size();++i) {
            if(mp.find(words[i]) == mp.end()) mp[words[i]] = 0;
            mp[words[i]]++;
        }
        priority_queue<pair<int,string>,vector<pair<int,string>> , compare> pq;
        for(auto itr=mp.begin();itr!= mp.end();++itr) {
            string str = itr->first;
            int freq = itr->second;
            pq.push({freq,str});
            // cout << freq << " " << str << endl;
        }
        int t = 0;
        vector<string> ans;
        
        while (t < k) {
            string str = pq.top().second;
            ans.push_back(str);
            pq.pop();
            t++;
        }
    
        return ans;
    }
};