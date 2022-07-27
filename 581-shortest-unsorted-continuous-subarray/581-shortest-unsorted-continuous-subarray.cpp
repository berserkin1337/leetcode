class Solution {
public:
  int findUnsortedSubarray(vector<int> &nums) {
    if (nums.size()<=1)return 0;
    vector<int> nums0(nums.begin(),nums.end());
    sort(nums0.begin(),nums0.end());
    int start= nums.size() , end = 0;
    for(int i=0;i<nums.size();++i){
      if(nums[i]!=nums0[i]){
        start = min(start,i);
        end = max(end,i);
      }
    }
    return (end - start >= 0 ? end - start + 1 : 0);
  }
};
