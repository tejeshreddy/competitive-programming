class Solution {
    public int countNegatives(int[][] grid) {
        int n = grid[0].length;
        int result = 0;
        
        for (int[] row: grid) {
            int left = 0, right = n - 1;
            while (left <= right) {
                int mid = (left + right) / 2;
                if (row[mid] < 0) {
                    right = mid - 1;
                } 
                else {
                    left = mid + 1;
                }
            }
            result += (n - left);
        }
        
        return result;
    }
}