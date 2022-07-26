bool sortFunc(int num1,int  num2){
  string str1 = to_string(num1);
  string str2 = to_string(num2);
  return stoll(str1+str2) < stoll(str2+str1);
}

class Solution {
public:
  string largestNumber(vector<int>& nums) {
    sort(nums.begin(),nums.end(),sortFunc);
    for(int i=0;i<nums.size();++i) {
      cout << nums[i] << " ";
    }
    cout << endl;
    string ans = "";
    for (int i= nums.size()-1;i>=0;--i){
      ans += to_string(nums[i]);
    }
    int i = 0;
    while (ans[i] == '0' && i < ans.size() -1 ) {
      i++;
    }
    
    return ans.substr(i);
    }
};

