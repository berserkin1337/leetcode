class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        set<int> s1(nums1.begin() , nums1.end());
        set<int> s2(nums2.begin() , nums2.end());
        
        auto itr2 = s2.begin();
        vector<int> res;
        for(auto itr1 = s1.begin() ; itr1!= s1.end(); itr1 ++) {
            
            while ( itr2 != s2.end() && *itr2 <= *itr1 ) {
                if (*itr1 == *itr2){
                    res.push_back(*itr1);
                }
                itr2++;
            }
            
        }
        
        
        return res;
        
    }
};