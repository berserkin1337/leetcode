class Solution {
public:
    int nextGreaterElement(int n) {
        string s = to_string(n);
        if(!next_permutation(s.begin(),s.end())){
            return -1;
        }
        else {
            try {
                int x = stoi(s);
                return x;
            }
            catch(...) {
                return -1;
            }
        }
        
    }
};