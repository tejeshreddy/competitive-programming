class Solution {
    public int peakIndexInMountainArray(int[] arr) {
     int maxAt = 0;
        
    for (int i = 0; i < arr.length; i++) {
        maxAt = arr[i] > arr[maxAt] ? i : maxAt;
    }
    
    return maxAt;
        
    }
}