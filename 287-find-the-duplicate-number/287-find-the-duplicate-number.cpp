class Solution {
public:
  int findDuplicate(vector<int> &nums) {
    for (int i = 0; i < nums.size(); ++i) {
      if (nums[nums[i] - 1] == nums[i] && i != nums[i]-1) {
        return nums[i];
      }
      while (nums[nums[i] - 1] != nums[i]) {
        if (nums[nums[i] - 1] == nums[i]  && i != nums[i]-1) {
          return nums[i];
        }
        swap(nums[nums[i] - 1], nums[i]);
        if (nums[nums[i] - 1] == nums[i]&& i != nums[i]-1 ) {
          return nums[i];
        }
      }
    }
    return -1;
  }
};
