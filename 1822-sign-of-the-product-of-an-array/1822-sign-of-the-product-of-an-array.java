class Solution {
    public int arraySign(int[] nums) {
        int negative = 0;
        boolean zero = false;
        
        for (int i : nums) {
            if (i == 0) {
                zero = true;
            }
            else if (i < 0) {
                negative += 1;
            }
        }
        
        if (zero == true) {
            return 0;
        }
        else if (negative % 2 == 1) {
            return -1;
        }
        else {
            return 1;
        }
    }
}