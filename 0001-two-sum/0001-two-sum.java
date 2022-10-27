import java.util.*;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        HashMap<Integer,Integer> mp = new HashMap<>();
        for(int i=0;i<nums.length;++i) {
            if( mp.containsKey(target-nums[i]) ) {
                int [] arr=  new int[] {mp.get(target-nums[i]) ,i};
                return arr;
            }
            mp.put(nums[i],i);
        }
        int [] arr=  new int[] {-1,-1};
        return arr;
    }
}