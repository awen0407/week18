// week18-2.cpp 二合一
// Leetcode 54. Spiral Matrix
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int M = matrix.size(), N = matrix[0].size();
        int i=0,j=0;
        int di[4] = {0, 1, 0 ,-1};
        int dj[4] = {1, 0, -1, 0};
        int d = 0;
        vector<int> ans;
        while(ans.size() < M * N){
            ans.push_back( matrix[i][j]);
            matrix[i][j] = 999;
            int i2 = i+di[d], j2 = j+dj[d];
            if(i2>=M || j2>=N || i2<0 || j2<0 || matrix[i2][j2]==999){
               d=(d+1)%4; 
            }
            i=i+di[d];
            j=j+dj[d];
        }
        return ans;
    }
};