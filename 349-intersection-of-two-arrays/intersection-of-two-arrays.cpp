class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int> temp;
        int k = 0;
        for (int i = 0; i < nums1.size(); i++) {
            for (int j = 0; j < nums2.size(); j++) {
                if (nums1[i] == nums2[j]) {
                    temp.push_back(nums1[i]);
                    break;
                }
            }
        }
        vector<int> result ;
        for(int i=0;i<temp.size();i++){
            bool duplicate = false;
            for(int j=0;j<result.size();j++){
                if(temp[i]==result[j]){
                    duplicate = true ;
                    break;
                }
            }
            if(!duplicate){
                result.push_back(temp[i]);
            }
        }
       return result; 
    }
}; //