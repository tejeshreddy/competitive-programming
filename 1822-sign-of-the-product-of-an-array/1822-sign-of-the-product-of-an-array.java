class Solution {
    public int arraySign(int[] nums) {
        int negativeNumbers = 0;
        
        for (int num : nums) {
            if (num == 0) {
                return 0;
            }
            if (num < 0) {
                negativeNumbers += 1;
            }
        }
        return negativeNumbers % 2 == 0 ? 1 : -1;
        
    }
}