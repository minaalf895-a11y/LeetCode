class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(),g.end());
        sort(s.begin(),s.end());
        int count=0;
        int i=0;
        int j=0;
        while(i<g.size()&&j<s.size()){
            if(s[j]>=g[i]){
                count++;
                i++;
                j++;
            }
            else{
                j++;
            }
        }
        return count;
    }
};
// A nested loops approach typically iterates through every possible pair of elements, resulting in a time complexity of O(n²), whereas a two pointers approach uses two pointers that often traverse the data structure in a single pass or in a way that avoids redundant comparisons, achieving a more efficient time complexity, typically O(n) or O(n log n) [1]. Two pointer approch is much betterv than using nested loops 