class Solution {
    public int[][] generateMatrix(int n) {
        int[][] matrix = new int[n][n];
        int count = 1;
        
        int l = 0;
        int u = 0;
        int d = n - 1;
        int r = n - 1;
        
        while (l <= r && u <= d) {
            for (int i=l; i <= r; i++) {
                matrix[u][i] = count++;
            }
            u += 1;
                
            for (int i=u; i <= d; i++) {
                matrix[i][r] = count++;
            }
            r -= 1;
            
            for (int i=r; i >= l; i--) {
                matrix[d][i] = count++;
            }
            d -= 1;
            
            for (int i=d; i>=u; i--) {
                matrix[i][l] = count++;
            }
            l += 1;
        }
        return matrix;
    }
}