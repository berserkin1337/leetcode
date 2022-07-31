
class Solution {

  bool checkIndex(vector<int> &nums, int index, int target, bool left) {
    if (left) {
      if (index == 0)
        return true;
      if (nums[index - 1] != target)
        return true;
      return false;
    } else {
      if (index == nums.size()-1)
        return true;
      if( nums[index+1]!= target){
        return true;
      }
      return false;
    }
  }

public:
  vector<int> searchRange(vector<int> &nums, int target) {
    // Maybe first check if the target is there in the array
    int n = nums.size();
    int low = 0, high = n - 1;
    bool found = false;
    while (low <= high) {

      int mid = low + (high - low) / 2;
      // cout << mid << endl;
      if (nums[mid] == target) {
        found = true;
        break;
      } else if(nums[mid]> target) high = mid -1;
      else low = mid + 1;
      
    }
    if (!found) {
      vector<int> notFound = {-1, -1};
      return notFound;
    }
    // nums = [5,7,7,8,8,10], target = 8
    // find index such that  nums[index] == target && nums[index-1] != target
    low = 0, high = n - 1;
    int left = -1;
    while (low <= high) {
      int mid = low + (high - low) / 2;
      if (nums[mid] == target && checkIndex(nums, mid, target, true)) {
        left = mid;
        break;
      } else if (nums[mid] >= target)
        high = mid - 1;
      else
        low = mid + 1;
    }
    low = 0, high = n - 1;
    int right = -1;
    while (low <= high) {
      int mid = low + (high - low) / 2;
      // cout << mid << endl;
      if (nums[mid] == target && checkIndex(nums, mid, target,false)) {
        right = mid;
        break;
      } else if (nums[mid] > target)
        high = mid - 1;
      else
        low = mid + 1;
    }
    vector<int> res = {left,right};
    return res;

  }
};