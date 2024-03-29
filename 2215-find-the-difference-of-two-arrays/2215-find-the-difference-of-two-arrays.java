class Solution {
    List<Integer> getElementsPresentInOneList(int[] nums1, int[] nums2) {
        Set<Integer> onlyInNums1 = new HashSet<> ();
        Set<Integer> existInNums2 = new HashSet<> ();
        
        for (int num : nums2) {
            existInNums2.add(num);
        }
        
        for (int num : nums1) {
            if (!existInNums2.contains(num)) {
                onlyInNums1.add(num);
            }
        }
        
        return new ArrayList<>(onlyInNums1);
    } 
    
    
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        return Arrays.asList(getElementsPresentInOneList(nums1, nums2), getElementsPresentInOneList(nums2, nums1));
    }
}