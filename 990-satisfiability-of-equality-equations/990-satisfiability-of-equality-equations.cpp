#include <bits/stdc++.h>

using namespace std;

class Solution {
	vector<int> parent;
	int find(int x){
		return parent[x] == x ? x : find(parent[x]);
	}
public:
    bool equationsPossible(vector<string>& equations) {
		parent.resize(26,0);
		for(int i=0;i<parent.size();++i){
			parent[i] = i;
		}
		for(auto s: equations){
			if(s[1]=='='){
				int x = find(s[0]-'a');
				int y = find(s[3]-'a');
				if(x!=y)parent[x]=y;
			}
		}
		for(auto s: equations){
			if(s[1]=='!'){
				int x = find(s[0]-'a');
				int y = find(s[3]-'a');
				if(x==y) return false;
			}
		}
		return true;
    }
};